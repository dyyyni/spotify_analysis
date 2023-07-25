import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

df = pd.read_json("../data/interim/interim_data.json")

# First, convert the timestamp to datetime
df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

# Convert the 'ms_played' to minutes
df['minutes_played'] = df['ms_played'] / 60000

# Then, apply the filter
df = df.query('timestamp > 0 and datetime.dt.year >= 2020')

# Define day_dict
day_dict = {i: day for i, day in enumerate(calendar.day_name)}

df['weekday'] = df['datetime'].dt.dayofweek
df['weekday'] = df['weekday'].map(day_dict)

# Define the order of days in a week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Set 'weekday' column to categorical data type and specify the order
df['weekday'] = pd.Categorical(df['weekday'], categories=day_order, ordered=True)

# Aggregate the data by weekday
heatmap_data_total_weekly = df.groupby('weekday')['minutes_played'].sum()

# Total Listening by Weekday
plt.figure(figsize=(10, 8))
sns.barplot(x=heatmap_data_total_weekly.index,
            y=heatmap_data_total_weekly.values, palette="Reds_r", order=day_order)
plt.title('Total Listening by Weekday')
plt.ylabel('Minutes')
plt.xlabel('Weekday')
plt.show()

