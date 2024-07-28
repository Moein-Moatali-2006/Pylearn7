import time
import threading
import random
from moviepy import editor


moveis_list=["Video_1.mp4","Video_2.mp4","Video_3.mp4","Video_4.mp4","Video_5.mp4"]

def download(url):
        video = editor.VideoFileClip(url)
        link=url[:-4]
        video.audio.write_audiofile(f'{link}.mp3')

start_time=time.time()

threads=[]
for url in moveis_list:
    new_thread=threading.Thread(target=download,args=[url])
    threads.append(new_thread)

for thread in threads:
      thread.start()

for thread in threads:
      thread.join()

end_time=time.time()
result=end_time - start_time
print(f"second:{result}")