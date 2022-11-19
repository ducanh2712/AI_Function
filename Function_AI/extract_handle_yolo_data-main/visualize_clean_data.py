import cv2
import os
import shutil
from tqdm import tqdm

CLEAN_ROOT = os.path.join('my_data', 'clean_data_cam3')
CLEAN_IMAGES_ROOT = os.path.join(CLEAN_ROOT, 'images')
CLEAN_LABELS_ROOT = os.path.join(CLEAN_ROOT, 'labels')
CLEAN_VISUAL_ROOT = os.path.join(CLEAN_ROOT, 'visual_images')
try:
    shutil.rmtree(CLEAN_VISUAL_ROOT)
except:
    pass
os.mkdir(CLEAN_VISUAL_ROOT)

images = os.listdir(CLEAN_IMAGES_ROOT)
labels = os.listdir(CLEAN_LABELS_ROOT)

for i in tqdm(range(len(images))):
    img = cv2.imread(os.path.join(CLEAN_IMAGES_ROOT, images[i]))

    # print(images[i])
    f = open(os.path.join(CLEAN_LABELS_ROOT, labels[i]), "r")
    while True:
        try:
            data = f.readline()
            # print(data)
            # _, x, y, w, h = labels[i].split(".")
            # print(data.split(' '))
            _, x, y, w, h = data.split(' ')
            x, y, w, h = float(x), float(y), float(w), float(h)
            x_min, y_min = (x - w/2)*img.shape[1], (y - h/2)*img.shape[0]
            x_max, y_max = (x + w/2)*img.shape[1], (y + h/2)*img.shape[0]

            img = cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 0, 255), 2)
            cv2.imwrite(os.path.join(CLEAN_VISUAL_ROOT, f'visual_{images[i]}'), img)
        except:
            break
