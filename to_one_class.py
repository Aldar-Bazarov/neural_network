import os
import shutil

def process_folder(source_dir, dest_dir):
    shutil.copytree(source_dir, dest_dir)
    for split in ["train", "valid", "test"]:
        for filename in os.listdir(os.path.join(dest_dir, split, "labels")):
            if filename.endswith(".txt"):
                labelpath = os.path.join(dest_dir, split, "labels", filename)
                with open(labelpath, "r") as f:
                    lines = f.readlines()

                with open(labelpath, "w") as f:
                    for line in lines:
                        modified_line = "0" + line[1:]
                        f.write(modified_line)

source_dir = os.path.join("../../Downloads/signs_copy")
dest_dir = os.path.join("../../Downloads/signs_one_class")
process_folder(source_dir, dest_dir)

print("Файлы успешно изменены и перемещены.")