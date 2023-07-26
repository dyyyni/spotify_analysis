import os, json

def load_raw_data():
  raw_data_path = './data/raw'
  json_files = [file for file in os.listdir(raw_data_path) if file.endswith('.json')]

  all_data = []
  for file in json_files:
    with open(os.path.join(raw_data_path, file), 'r') as f:
      data = json.load(f)
      all_data.extend(data)


  return all_data

def transform_raw_data(data):
 interim_data = []
 for streamed_object in data:
  interim_object = {
     "podcast": bool,
     "timestamp": None,
     "ms_played": None,
     "song_name": None,
     "artist_name": None,
     "album_name": None,
     "show_name": None,
     "episode_name": None,
     "ts": None
   }

  # To figure out if we are dealing with a song or a podcast
  if streamed_object["episode_name"] == None:
    interim_object["podcast"] = False
  else: interim_object["podcast"] = True

  interim_object["timestamp"] = streamed_object["offline_timestamp"]
  interim_object["ms_played"] = streamed_object["ms_played"]
  interim_object["song_name"] = streamed_object["master_metadata_track_name"]
  interim_object["artist_name"] = streamed_object["master_metadata_album_artist_name"]
  interim_object["album_name"] = streamed_object["master_metadata_album_album_name"]
  interim_object["show_name"] = streamed_object["episode_show_name"]
  interim_object["episode_name"] = streamed_object["episode_name"]
  interim_object['ts'] = streamed_object['ts']

  interim_data.append(interim_object)

 return interim_data

def store_interim_data(interim_data):
  output_dir = './data/interim'
  output_file = os.path.join(output_dir, 'interim_data.json')

  with open(output_file, 'w') as outfile:
    json.dump(interim_data, outfile)

def main():
  data = load_raw_data()
  interim_data = transform_raw_data(data)
  store_interim_data(interim_data)

main()
