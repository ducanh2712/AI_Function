import cv2
import os
import shutil
from tqdm import tqdm

VIDEOS_FRAMES_ROOT = os.path.join('videos_frames')
CLEAN_ROOT = os.path.join('clean_data')
CLEAN_IMAGES_ROOT = os.path.join(CLEAN_ROOT, 'images')
CLEAN_LABELS_ROOT = os.path.join(CLEAN_ROOT, 'labels')

# mkdir CLEAN_ROOT
try:
    shutil.rmtree(CLEAN_ROOT)
except:
    pass
os.mkdir(CLEAN_ROOT)
os.mkdir(CLEAN_IMAGES_ROOT)
os.mkdir(CLEAN_LABELS_ROOT)

videos_frames_paths = os.listdir(VIDEOS_FRAMES_ROOT)
cnt = 0

for p in videos_frames_paths:
    imgs_path = os.path.join(VIDEOS_FRAMES_ROOT, p, 'images')
    labels_path = os.path.join(VIDEOS_FRAMES_ROOT, p, 'labels')
    # print(labels_path)
    for l in os.listdir(labels_path):
        if l != 'classes.txt':
            # READ OLD FOLDER
            print(l[:-4])
            img_path = os.path.join(imgs_path, f'{l[:-4]}.png')
            img = cv2.imread(img_path)
            cnt += 1

            # WRITE NEW FOLDER
            cv2.imwrite(os.path.join(CLEAN_IMAGES_ROOT, f'{l[:-4]}.png'), img)
            shutil.copy(os.path.join(labels_path, l), os.path.join(CLEAN_LABELS_ROOT, l))



print(f'TOTAL IMG : {cnt}')
