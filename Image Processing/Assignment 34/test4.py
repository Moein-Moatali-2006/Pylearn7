import cv2
import multiprocessing

def show_video(video_path):
    video = cv2.VideoCapture(video_path)
    while True:
        ret,frame = video.read()
        if not ret :
            break
        cv2.imshow("video",frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    process_1=multiprocessing.Process(target=show_video,args=["vid1.mp4"])
    process_2=multiprocessing.Process(target=show_video,args=["vid2.mp4"])

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print("Done")