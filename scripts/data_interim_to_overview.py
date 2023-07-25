import json


def load_data(path_to_data):
    with open(path_to_data, 'r') as file:
        data = json.load(file)
        return data

def time_listened(data):
    overview_listened = {
        "total_time_listened"       : 0,
        "music_time_listened"       : 0,
        "podcasts_time_listened"    : 0
    }

    for stream in data:
        overview_listened["total_time_listened"] += stream["ms_played"]
        if(stream["podcast"] == False):
             overview_listened["music_time_listened"] += stream["ms_played"]
        else:
            overview_listened["podcasts_time_listened"] += stream["ms_played"]

    return overview_listened 

    
def main():
    data = load_data('../data/interim/interim_data.json')
    overview_listened = time_listened(data)
    for key, value in overview_listened.items():
        print(key, int(value / 1000 / 60), "minutes")
main()
