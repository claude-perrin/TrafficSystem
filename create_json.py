import os
import json
 
def get_json():

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

def change_labels():
    current_path = os.path.dirname(os.path.abspath("__file__"))
    dataset_path = os.path.join(current_path, "..", "DatasetTraffic", "dataset", "sec1")

    for _, _, files in os.walk(dataset_path):
        for file in sorted(files):
            if ".txt" in file:
                adjusted_labels = {file: []}
                labels = ""
                with open(os.path.join(dataset_path, file), "r") as f:
                    labels = f.readlines()
                with open(os.path.join(dataset_path, file), "w") as f:
                    corrected_label = ""
                    for i in labels:
                        vehicle_type, x, y, width, height = i.split()
                        x = float(x)*1920
                        y = float(y)*1080
                        width = float(width)*1920
                        height = float(height)*1080

                        top_left_x = x - width / 2
                        top_left_y = y - height / 2
                        bottom_right_x = x + width / 2
                        bottom_right_y = y + height / 2
                        corrected_label += (f"{str(vehicle_type)} {str(top_left_x)} {str(top_left_y)} {str(bottom_right_x)} {str(bottom_right_y)}\n")
                    f.write(corrected_label)
    
                
        



if __name__ == "__main__":
    change_labels()
