#Moein Moatali
"""   Making a gif  """
import os 
import imageio


def making_gif_from_dir(url):
    
    file_list=sorted(os.listdir(url))

    IMAGES=[]

    for item in file_list:
        file_path=url+item
        image=imageio.imread(file_path)
        IMAGES.append(image)

    imageio.mimsave("Gif/output.gif",IMAGES)



making_gif_from_dir("Gif/images/")


