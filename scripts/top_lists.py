import pandas as pd

def main():
    df = pd.read_json("./data/interim/interim_data.json")
    df['minutes_played'] = df['ms_played'] / 1000 / 60  
    df['artist_song'] = df['artist_name'] + " - " + df['song_name'] 

    top_songs = df.groupby('artist_song')['minutes_played'] \
    .sum().sort_values(ascending=False).head(10).astype(int)
    top_artists = df.groupby('artist_name')['minutes_played'] \
    .sum().nlargest(10).astype(int)
    top_podcasts = df.groupby('show_name')['minutes_played'] \
    .sum().nlargest(10).astype(int)

    print(top_songs)
    print(top_artists)
    print(top_podcasts)

main()
