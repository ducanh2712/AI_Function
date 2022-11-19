import os

def check_empty(root):
	for label_name in os.listdir(root):
		label_path = os.path.join(root, label_name)
		if os.path.getsize(label_path) == 0:
			print(label_path)

if __name__ == '__main__':
	# check_empty(os.path.join('my_data', 'clean_data_cam1', 'labels'))
	# check_empty(os.path.join('my_data', 'clean_data_cam2', 'labels'))
	# check_empty(os.path.join('my_data', 'clean_data_cam3', 'labels'))
	check_empty(os.path.join('my_data', 'data_3cam', 'val', 'labels'))

	

