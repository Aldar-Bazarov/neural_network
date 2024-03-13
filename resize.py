import cv2
import os

# Путь к папке с изображениями
input_folder = "путь_к_папке_с_изображениями"
# Путь к папке, куда будут сохранены измененные изображения
output_folder = "путь_к_папке_сохранения"

# Создаем выходную папку, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходим по всем файлам в папке с изображениями
for filename in os.listdir(input_folder):
    # Проверяем, что файл - изображение
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Открываем изображение с помощью OpenCV
        img = cv2.imread(os.path.join(input_folder, filename))
        # Изменяем размер изображения до 250x250
        resized_img = cv2.resize(img, (250, 250))
        # Сохраняем измененное изображение в выходную папку
        cv2.imwrite(os.path.join(output_folder, filename), resized_img)

print("Изменение размера завершено!")
