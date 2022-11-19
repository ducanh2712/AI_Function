import cv2
import os
import shutil
from tqdm import tqdm
from sklearn.model_selection import train_test_split

CLEAN_ROOT = os.path.join('clean_data')
CLEAN_IMAGES_ROOT = os.path.join(CLEAN_ROOT, 'images')
CLEAN_LABELS_ROOT = os.path.join(CLEAN_ROOT, 'labels')
DATA_ROOT = os.path.join('data')
DATA_TRAIN_ROOT = os.path.join(DATA_ROOT, 'train')
DATA_VAL_ROOT = os.path.join(DATA_ROOT, 'val')
DATA_TRAIN_IMAGES_ROOT = os.path.join(DATA_TRAIN_ROOT, 'images')
DATA_TRAIN_LABELS_ROOT = os.path.join(DATA_TRAIN_ROOT, 'labels')
DATA_VAL_IMAGES_ROOT = os.path.join(DATA_VAL_ROOT, 'images')
DATA_VAL_LABELS_ROOT = os.path.join(DATA_VAL_ROOT, 'labels')

if __name__ == '__main__':
    # MRDIR
    try:
        shutil.rmtree(DATA_ROOT)
    except:
        pass
    os.mkdir(DATA_ROOT)
    os.mkdir(DATA_TRAIN_ROOT)
    os.mkdir(DATA_VAL_ROOT)
    os.mkdir(DATA_TRAIN_IMAGES_ROOT)
    os.mkdir(DATA_TRAIN_LABELS_ROOT)
    os.mkdir(DATA_VAL_IMAGES_ROOT)
    os.mkdir(DATA_VAL_LABELS_ROOT)

    # make train val
    images = os.listdir(CLEAN_IMAGES_ROOT) 
    labels = os.listdir(CLEAN_LABELS_ROOT)
    images.sort()
    labels.sort()

    images_train, images_val, labels_train, labels_val = train_test_split(images, labels, test_size=0.2)

    # print(images_train[12])
    # print(labels_train[12])

    # Write train path
    for i in tqdm(range(len(images_train))):
        # image
        img_path = os.path.join(CLEAN_IMAGES_ROOT, images_train[i])
        img = cv2.imread(img_path)
        cv2.imwrite(os.path.join(DATA_TRAIN_IMAGES_ROOT, images_train[i]), img)

        # label
        label_path = os.path.join(CLEAN_LABELS_ROOT, labels_train[i])
        shutil.copy(label_path, os.path.join(DATA_TRAIN_LABELS_ROOT, labels_train[i]))

        # check
        if labels_train[i][:-4] != images_train[i][:-4]:
            print(labels_train[i][:-4], images_train[i][:-4])

    # Write val path
    for i in tqdm(range(len(images_val))):
        # image
        img_path = os.path.join(CLEAN_IMAGES_ROOT, images_val[i])
        img = cv2.imread(img_path)
        cv2.imwrite(os.path.join(DATA_VAL_IMAGES_ROOT, images_val[i]), img)

        # label
        label_path = os.path.join(CLEAN_LABELS_ROOT, labels_val[i])
        shutil.copy(label_path, os.path.join(DATA_VAL_LABELS_ROOT, labels_val[i]))

        # check
        if labels_val[i][:-4] != images_val[i][:-4]:
            print(labels_val[i][:-4], images_val[i][:-4])

    train_images = os.listdir(DATA_TRAIN_IMAGES_ROOT)
    val_images = os.listdir(DATA_VAL_IMAGES_ROOT)

    print(len(val_images))
    cnt = 0
    for img in val_images:
        if img in train_images:
            cnt += 1
    print(cnt)

        

