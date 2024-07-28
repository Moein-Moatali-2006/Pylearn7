from moviepy import editor
import time

moveis_list=["Video_1.mp4","Video_2.mp4","Video_3.mp4","Video_4.mp4","Video_5.mp4"]

def download():
    for item in range(5):
        video = editor.VideoFileClip(moveis_list[item])
        video.audio.write_audiofile(f'test{item}.mp3')

start_time=time.time()
download()
end_time=time.time()

result=end_time - start_time
print(f"second:{result}")