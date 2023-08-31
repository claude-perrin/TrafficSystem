import os
import json
 
current_path = os.path.dirname(os.path.abspath("__file__"))
dataset_path = os.path.join(current_path, "..", "DatasetTraffic", "dataset")

sec1 = os.path.join(dataset_path, "sec1")

frame_txt_sec1 = {}

for _, _, files in os.walk(sec1):
    sorted_files = sorted(files)
    for id, file in enumerate(sorted_files[0::2]):
        frame = os.path.join(sec1, file)
        txt = os.path.join(sec1, sorted_files[id*2])
        frame_txt_sec1[frame] = txt
with open("frame_txt_sec1.json", "w") as outfile:
    json.dump(frame_txt_sec1, outfile) 
