import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the date range for data collection
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Initialize variables to store data
repository_counts = []
dates = []

# Make API requests to GitHub to get the data
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    url = f'https://api.github.com/search/repositories?q=hacktoberfest+created:{date_str}'

    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    data = response.json()

    repository_counts.append(data['total_count'])
    dates.append(date_str)

    current_date += timedelta(days=1)

# Create a DataFrame from the collected data
df = pd.DataFrame({'Date': dates, 'Repository Count': repository_counts})

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Repository Count'], marker='o', linestyle='-')
plt.title('Hacktoberfest Repository Count Over a Year')
plt.xlabel('Date')
plt.ylabel('Repository Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save or display the plot
plt.savefig('hacktoberfest_analysis.png')
plt.show()
