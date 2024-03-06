import os
import shutil

classes = ["crosswalk", "speedlimit", "stop", "trafficlight"]

def process_folder(source_dir, dest_dir):
    for c in classes:
        os.makedirs(os.path.join(dest_dir, "images", c), exist_ok=True)
        os.makedirs(os.path.join(dest_dir, "labels", c), exist_ok=True)

    for filename in os.listdir(os.path.join(source_dir, "labels")):
        if filename.endswith(".txt"):
            labelpath = os.path.join(source_dir, "labels", filename)
            with open(labelpath, "r") as f:
                lines = f.readlines()

            num_objects = len(lines)

            if num_objects == 1:
                imagepath = os.path.join(source_dir, "images", filename[:-4] + ".jpg")
                class_name = classes[int(lines[0].split(" ")[0])]

                target_image = '{0}/images/{1}/{2}'.format(dest_dir, class_name, filename[:-4] + ".jpg")
                target_labes = '{0}/labels/{1}/{2}'.format(dest_dir, class_name, filename)

                shutil.copy(imagepath, target_image)
                shutil.copy(labelpath, target_labes)

for split in ["train", "valid", "test"]:
    source_dir = os.path.join("../../Downloads/signs_vgg16", split)
    dest_dir = os.path.join("../../Downloads/signs_vgg16_1", split)

    process_folder(source_dir, dest_dir)

print("Файлы успешно разделены и перемещены.")