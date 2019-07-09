import cv2

VIDEO_PATH = 'video_path' 
EXTRACT_FOLDER = 'save_path'
EXTRACT_FREQUENCY = 10

def extract_frames(video_path, dst_folder, index):
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>03d}.jpg".format(dst_folder, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()

    print("Totally save {:d} pics".format(index-1))


def main():
    import shutil
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    import os
    os.mkdir(EXTRACT_FOLDER)
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()