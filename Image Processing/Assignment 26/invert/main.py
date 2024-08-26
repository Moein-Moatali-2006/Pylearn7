import cv2 as cv

def invert_color(file_path,name):
    image = cv.imread(file_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    row, col = image.shape
    for i in range(row):
        for j in range(col):
            image[i,j] = 255 - image[i,j]

    cv.imwrite(f'{name}.png', image)


invert_color('invert\img_1.png',"invert\woman")
invert_color('invert\img_2.png',"invert\man")