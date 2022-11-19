import os

DATA_ROOT = os.path.join('my_data', 'data_cam1')
DATA_TRAIN_ROOT = os.path.join(DATA_ROOT, 'train')
DATA_VAL_ROOT = os.path.join(DATA_ROOT, 'val')
DATA_TRAIN_IMAGES_ROOT = os.path.join(DATA_TRAIN_ROOT, 'images')
DATA_TRAIN_LABELS_ROOT = os.path.join(DATA_TRAIN_ROOT, 'labels')
DATA_VAL_IMAGES_ROOT = os.path.join(DATA_VAL_ROOT, 'images')
DATA_VAL_LABELS_ROOT = os.path.join(DATA_VAL_ROOT, 'labels')

train_images = os.listdir(DATA_TRAIN_IMAGES_ROOT)
val_images = os.listdir(DATA_VAL_IMAGES_ROOT)

print(len(val_images))
cnt = 0
for img in val_images:
	if img in train_images:
		cnt += 1
print(cnt)

print(len(train_images))
cnt = 0
for img in train_images:
	if img in val_images:
		cnt += 1
print(cnt)