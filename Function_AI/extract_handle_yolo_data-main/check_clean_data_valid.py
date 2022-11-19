import cv2
import os
import shutil
from tqdm import tqdm

CLEAN_ROOT = os.path.join('my_data', 'data_3cam', 'val')
CLEAN_IMAGES_ROOT = os.path.join(CLEAN_ROOT, 'images')
CLEAN_LABELS_ROOT = os.path.join(CLEAN_ROOT, 'labels')

images = os.listdir(CLEAN_IMAGES_ROOT)
images = [i[:-4] for i in images]
labels = os.listdir(CLEAN_LABELS_ROOT)
labels = [l[:-4] for l in labels]

print(labels == images)
