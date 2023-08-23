import pandas as pd


def print_list(series, series_name, key_name, value_name):
    # Manual padding because why not
    longest_key = 0
    longest_val = 0
    for key, val in series.items():
        if len(key) > longest_key:
            longest_key = len(key)
        if len(str(val)) > longest_val:
            longest_val = len(str(val))

    max_length = longest_key + 3 + max(longest_val, len(value_name))
    divider = "=" * int((max_length - len(series_name)) / 2)
    extra = "" if (max_length - len(series_name)) % 2 == 0 else "="

    # Title
    print(f"{divider}{series_name}{divider}{extra}")
    print(f"{str(key_name).ljust(longest_key + 3)}{value_name}")

    # List
    for key, val in series.items():
        print(key.ljust(longest_key) + " " * 3 + str(val).rjust(max(len(value_name), len(str(val)))))
    print()


def main():
    df = pd.read_json("./data/interim/interim_data.json")
    df["minutes_played"] = df["ms_played"] / 1000 / 60
    df["artist_song"] = df["artist_name"] + " - " + df["song_name"]

    top_songs_by_playtime = (
        df.groupby("artist_song")["minutes_played"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .astype(int)
    )
    top_artists_by_playtime = (
        df.groupby("artist_name")["minutes_played"].sum().nlargest(10).astype(int)
    )
    top_podcasts_by_playtime = (
        df.groupby("show_name")["minutes_played"].sum().nlargest(10).astype(int)
    )

    top_songs_by_playcount = df['artist_song'].value_counts().head(10)
    top_artists_by_playcount = df['artist_name'].value_counts().head(10)
    top_podcasts_by_playcount = df['show_name'].value_counts().head(10)

    print_list(top_songs_by_playtime, "Top songs by playtime", "Song name", "Minutes")
    print_list(top_artists_by_playtime, "Top artists by playtime", "Artist", "Minutes")
    print_list(top_podcasts_by_playtime, "Top podcasts by playtime", "Podcast", "Minutes")

    print_list(top_songs_by_playcount, "Top songs by play count", "Song name", "Play count")
    print_list(top_artists_by_playcount, "Top artists by play count", "Artist", "Play count")
    print_list(top_podcasts_by_playcount, "Top podcasts by play count", "Podcast", "Play count")

main()
