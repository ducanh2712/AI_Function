import cv2
import os
import shutil
from tqdm import tqdm

# ROOT = os.path.join('my_data', 'videos')
VIDEO_ROOT = os.path.join('videos')
VIDEO_FRAME_ROOT = os.path.join('videos_frames')
DIVIDE_N = 40

if __name__ == '__main__':
    video_paths = os.listdir(VIDEO_ROOT)

    try:
        shutil.rmtree(VIDEO_FRAME_ROOT)
    except:
        pass
    os.mkdir(VIDEO_FRAME_ROOT)



    for p in tqdm(video_paths):
        # Write video
        mkdir_name = os.path.join(VIDEO_FRAME_ROOT, p[:-4])
        os.mkdir(mkdir_name)
        os.mkdir(os.path.join(mkdir_name, 'images'))
        os.mkdir(os.path.join(mkdir_name, 'labels'))
        shutil.copy(os.path.join(VIDEO_ROOT, p), os.path.join(mkdir_name, p))

        # Extract Frame
        cap = cv2.VideoCapture(os.path.join(mkdir_name, p))
        success, img = cap.read()
        cnt = 0
        while success:
            if cnt % DIVIDE_N == 0:
                print(f'{p} - FRAME {cnt}')
                cv2.imwrite(os.path.join(os.path.join(mkdir_name, 'images', f'frame_{p[:-4]}_{cnt}.png')), img)
            success, img = cap.read()
            cnt += 1




