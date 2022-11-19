import cv2
import os
import shutil
from tqdm import tqdm
from sklearn.model_selection import train_test_split

OLD_ROOTS = [os.path.join('my_data', 'clean_data_cam1'), os.path.join('my_data', 'clean_data_cam2'),os.path.join('my_data', 'clean_data_cam3')]

DATA_ROOT = os.path.join('my_data', 'data_3cam')
DATA_TRAIN_ROOT = os.path.join(DATA_ROOT, 'train')
DATA_VAL_ROOT = os.path.join(DATA_ROOT, 'val')
DATA_TRAIN_IMAGES_ROOT = os.path.join(DATA_TRAIN_ROOT, 'images')
DATA_TRAIN_LABELS_ROOT = os.path.join(DATA_TRAIN_ROOT, 'labels')
DATA_VAL_IMAGES_ROOT = os.path.join(DATA_VAL_ROOT, 'images')
DATA_VAL_LABELS_ROOT = os.path.join(DATA_VAL_ROOT, 'labels')

if __name__ == '__main__':

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

	total_images_train = [] 
	total_images_val = []
	total_labels_train = []
	total_labels_val = []

	for old_root in OLD_ROOTS:
		img_root = os.path.join(old_root, 'images')
		label_root = os.path.join(old_root, 'labels')
		print(img_root, label_root)

		images = os.listdir(img_root) 
		labels = os.listdir(label_root)

		images = [os.path.join(img_root, name) for name in images]
		labels = [os.path.join(label_root, name) for name in labels]

		images.sort()
		labels.sort()

		images_train, images_val, labels_train, labels_val = train_test_split(images, labels, test_size=0.3)

		# print(images_train[12])
		# print(labels_train[12])

		print(len(images_train), len(images_val))
		total_images_train += images_train
		total_images_val += images_val
		total_labels_train += labels_train
		total_labels_val += labels_val

		print("----------")

	print(len(total_images_train), len(total_images_val))
	print(len(total_labels_train), len(total_labels_val))

	

	total_images_train.sort()
	total_images_val.sort()
	total_labels_train.sort()
	total_labels_val.sort()

	print(total_images_train[40])
	print(total_labels_train[40])

	print(total_images_val[40])
	print(total_labels_val[40])

	# Write train path
	for i in tqdm(range(len(total_images_train))):
		# image
		img = cv2.imread(total_images_train[i])
		cv2.imwrite(os.path.join(DATA_TRAIN_IMAGES_ROOT, total_images_train[i].split('/')[-1]), img)

		# label
		shutil.copy(total_labels_train[i], os.path.join(DATA_TRAIN_LABELS_ROOT, total_labels_train[i].split('/')[-1]))

		# check
		if total_labels_train[i].split('/')[:-4] != total_images_train[i].split('/')[:-4]:
			print(total_labels_train[i].split('/')[:-4], total_images_train[i].split('/')[:-4])

	# Write train path
	for i in tqdm(range(len(total_images_val))):
		# image
		img = cv2.imread(total_images_val[i])
		cv2.imwrite(os.path.join(DATA_VAL_IMAGES_ROOT, total_images_val[i].split('/')[-1]), img)

		# label
		shutil.copy(total_labels_val[i], os.path.join(DATA_VAL_LABELS_ROOT, total_labels_val[i].split('/')[-1]))

		# check
		if total_labels_val[i].split('/')[:-4] != total_images_val[i].split('/')[:-4]:
			print(total_labels_val[i].split('/')[:-4], total_images_val[i].split('/')[:-4])


	check_train_images = os.listdir(DATA_TRAIN_IMAGES_ROOT)
	check_val_images = os.listdir(DATA_VAL_IMAGES_ROOT)

	print(len(check_val_images))
	cnt = 0
	for name in check_val_images:
		if name in check_train_images:
			cnt += 1

	print(cnt)