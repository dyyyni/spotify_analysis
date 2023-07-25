import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_json("../data/interim/interim_data.json")

    # Convert the timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Apply the filter
    df = df.query('timestamp > 0 and datetime.dt.year >= 2020')

    # Get the hour information
    df['hour'] = df['datetime'].dt.hour
    df['minutes_played'] = df['ms_played'] / 60000  # convert milliseconds to minutes

    # Generate the pivot table
    heatmap_data_hourly = pd.pivot_table(df, values='minutes_played', columns='hour', aggfunc='sum').fillna(0).astype(int)

    # Create the heatmap
    plt.figure(figsize=(10, 4))
    sns.heatmap(heatmap_data_hourly, cmap="Reds", linewidths=1)
    plt.title('Total Listening by Hour')
    plt.show()

if __name__ == "__main__":
    main()

