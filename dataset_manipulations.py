import os
import json
import random

TRAIN_SET = 0.7
TEST_SET = 0.2
VALIDATE_SET = 0.1


def generate_json(sec1):
    frame_txt_sec1 = []

    for _, _, files in os.walk(sec1):
        sorted_files = sorted(files)
        for id, file in enumerate(sorted_files[1::2]):
            txt = os.path.join(sec1, file)
            frame = os.path.join(sec1, sorted_files[id * 2])
            frame_txt_sec1.append([frame, txt])
    num_elements = len(frame_txt_sec1)
    training_set = frame_txt_sec1[:int(num_elements * TRAIN_SET)]
    test_set = frame_txt_sec1[int(num_elements * TRAIN_SET):int(num_elements * (TRAIN_SET + TEST_SET))]
    validate_set = frame_txt_sec1[int(num_elements * (TRAIN_SET + TEST_SET)):]

    dataset_json = {"training_set": training_set, "test_set": test_set, "validate_set": validate_set}
    with open("frame_txt_sec1.json", "w") as outfile:
        json.dump(dataset_json, outfile)


def change_labels(dataset_path):
    for _, _, files in os.walk(dataset_path):
        for file in sorted(files):
            if ".txt" in file:
                labels = ""
                with open(os.path.join(dataset_path, file), "r") as f:
                    labels = f.readlines()
                with open(os.path.join(dataset_path, file), "w") as f:
                    corrected_label = ""
                    for i in labels:
                        vehicle_type, x, y, width, height = i.split()
                        x = float(x) * 1920
                        y = float(y) * 1080
                        width = float(width) * 1920
                        height = float(height) * 1080

                        top_left_x = x - width / 2
                        top_left_y = y - height / 2
                        bottom_right_x = x + width / 2
                        bottom_right_y = y + height / 2
                        corrected_label += (f"{str(vehicle_type)} {str(top_left_x)} {str(top_left_y)} {str(bottom_right_x)} {str(bottom_right_y)}\n")
                    f.write(corrected_label)



if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath("__file__"))
    dataset_path = os.path.join(current_path, "..", "DatasetTraffic", "dataset", "sec1")
    generate_json(dataset_path)
    #  change_labels(dataset_path)
