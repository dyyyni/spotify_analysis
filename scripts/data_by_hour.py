import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_json("./data/interim/interim_data.json")

    df['timestamp'] = pd.to_datetime(df['ts'])

    df['hour'] = df['timestamp'].dt.hour
    df['minutes_played'] = df['ms_played'] / 1000 / 60
    heatmap_data_hourly = pd.pivot_table(
        df,
        values='minutes_played',
        columns='hour',
        aggfunc='sum',
    ).fillna(0).astype(int)

    plt.figure(figsize=(10, 4))
    sns.heatmap(
        heatmap_data_hourly,
        cmap="Reds",
        linewidths=1,
        cbar_kws={'label': 'Minutes'}
    )
    
    # Seaborn was being annoying. Had to manually overwrite the ticks to remove
    # all the default titles that popped up.
    plt.xticks(ticks=range(len(heatmap_data_hourly.columns)), labels=heatmap_data_hourly.columns)
    plt.yticks([], [])   

    plt.title('Total Listening by Hour')
    plt.xlabel('Time')
    plt.savefig('./reports/figures/by_hour.png', dpi=300)

main()

