import cv2 as cv

def invert_color(file_path,name):
    image = cv.imread(file_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    row, col = image.shape
    for i in range(row):
        for j in range(col):
            if image[i,j] > 180 :
                image [i,j] = 0
            elif image [i,j] < 180 :
                image[i,j] = 255

    cv.imwrite(f'{name}.jpg', image)


invert_color('invert\img_1.jpg',"invert\woman")
invert_color('invert\img_2.jpg',"invert\man")