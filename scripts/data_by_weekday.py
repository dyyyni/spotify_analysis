import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

def main():
    df = pd.read_json("./data/interim/interim_data.json")

    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

    df['minutes_played'] = df['ms_played'] / 1000 / 60

    df = df.query('timestamp > 0 and datetime.dt.year >= 2020').copy()

    day_dict = {i: day for i, day in enumerate(calendar.day_name)}

    df['weekday'] = df['datetime'].dt.dayofweek
    df['weekday'] = df['weekday'].map(day_dict)

    day_order = ['Monday', 'Tuesday',
                 'Wednesday', 'Thursday',
                 'Friday', 'Saturday', 'Sunday']

    df['weekday'] = pd.Categorical(df['weekday'], categories=day_order, ordered=True)

    heatmap_data_total_weekly = df.groupby('weekday')['minutes_played'].sum()

    plt.figure(figsize=(10, 8))
    sns.barplot(x=heatmap_data_total_weekly.index,
                y=heatmap_data_total_weekly.values,
                palette="Reds_r",
                order=day_order)

    plt.title('Total Listening by Weekday')
    plt.ylabel('Minutes')
    plt.xlabel('Weekday')
    plt.savefig('./reports/figures/by_weekday.png', dpi=300)

main()

