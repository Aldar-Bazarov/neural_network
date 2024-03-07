import os
from PIL import Image
import shutil

def crop_and_save_images(source_dirs, dest_dir):
    for source_dir in source_dirs:
        for c in classes:
            label_dir = os.path.join(source_dir, "labels", c)
            image_dir = os.path.join(source_dir, "images", c)
            cropped_image_class_dir = os.path.join(dest_dir, "cropped_images", c)
            os.makedirs(cropped_image_class_dir, exist_ok=True)

            for label_file in os.listdir(label_dir):
                if label_file.endswith(".txt"):
                    image_file = label_file[:-4] + ".jpg"
                    image_path = os.path.join(image_dir, image_file)
                    label_path = os.path.join(label_dir, label_file)

                    with open(label_path, "r") as f:
                        data = f.readline().split(" ")
                        class_name = classes[int(data[0])]
                        x1, y1, width, height = map(float, data[1:])

                    with Image.open(image_path) as img:
                        img_width, img_height = img.size
                        left = int((x1 - (width / 2)) * img_width)
                        top = int((y1 - (height / 2)) * img_height)
                        right = int((x1 + (width / 2)) * img_width)
                        bottom = int((y1 + (height / 2)) * img_height)

                        cropped_img = img.crop((left, top, right, bottom))
                        cropped_img.save(os.path.join(cropped_image_class_dir, image_file))

# Пример использования:
source_dirs = ["/content/signs_vgg16/train", "/content/signs_vgg16/valid", "/content/signs_vgg16/test"]
dest_dir = "/content"
crop_and_save_images(source_dirs, dest_dir)
print("Обрезанные изображения успешно сохранены в новую папку.")