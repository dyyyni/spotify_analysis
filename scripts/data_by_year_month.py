import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_json("./data/interim/interim_data.json")

    df = df[df['timestamp'] != 0]

    df['minutes_played'] = (df['ms_played'] / 1000 / 60).astype(int)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month

    df = df[df['year'] >= 2020]

    df_music = df[df['podcast'] == False]
    df_podcast = df[df['podcast'] == True]

    cmap = sns.color_palette("Reds", as_cmap=True) 

    heatmap_data_total = pd.pivot_table(
        df,
        values='minutes_played',
        index='year',
        columns='month',
        aggfunc='sum'
    ).fillna(0).astype(int)

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        heatmap_data_total,
        cmap=cmap,
        annot=True,
        annot_kws={"size": 8},
        fmt="d", linewidths=1,
        cbar_kws={'label': 'Minutes'})
    ax.figure.axes[-1].yaxis.label.set_size(10)
    plt.title('Total Listening by Year and Month')
    plt.ylabel('Year')
    plt.xlabel('Month')
    plt.savefig('./reports/figures/total_by_year.png', dpi=300)

    heatmap_data_music = pd.pivot_table(
        df_music,
        values='minutes_played',
        index='year',
        columns='month', 
        aggfunc='sum'
    ).fillna(0).astype(int)

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        heatmap_data_music,
        cmap=cmap,
        annot=True,
        annot_kws={"size": 8},
        fmt="d",
        linewidths=1,
        cbar_kws={'label': 'Minutes'}
    )
    ax.figure.axes[-1].yaxis.label.set_size(10)
    plt.title('Music Listening by Year and Month')
    plt.ylabel('Year')
    plt.xlabel('Month')
    plt.savefig('./reports/figures/music_by_year.png', dpi=300)

    heatmap_data_podcast = pd.pivot_table(
        df_podcast,
        values='minutes_played',
        index='year',
        columns='month',
        aggfunc='sum'
    ).fillna(0).astype(int)

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        heatmap_data_podcast,
        cmap=cmap,
        annot=True,
        annot_kws={"size": 8},
        fmt="d",
        linewidths=1,
        cbar_kws={'label': 'Minutes'}
    )
    ax.figure.axes[-1].yaxis.label.set_size(10)
    plt.title('Podcast Listening by Year and Month')
    plt.ylabel('Year')
    plt.xlabel('Month')
    plt.savefig('./reports/figures/podcast_by_year.png', dpi=300)

main()
