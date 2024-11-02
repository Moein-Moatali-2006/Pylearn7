# Convolution 2D and Histogram Equalization
cv2 \
numpy \
matplotlib
```
pip install -r requirements.txt
```
## Average
input:
!['input'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Average/1.tif)
output:
!['output'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Average/output/output.png)

## Convolution 2D
input:
!['input'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Convolution%202D/lion.png)
output:
!['output'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Convolution%202D/output/result.png)


## Histogram Equalization
results:
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Histogram%20Equalization/output/result_1_city.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Histogram%20Equalization/output/result_1_nature.png)

!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Histogram%20Equalization/output/result_1_room.png)
```
cv2.equalizeHist()
```
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Histogram%20Equalization/output/result_2_room.png)

CLAHE stands for Contrast Limited Adaptive Histogram Equalization. maybe this function helps you to improve the contrast of the last image. Try it.
```
cv2.createCLAHE()
```


## Median Filter
result:
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/board.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/celebrate.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/font.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/rectangle.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/woman.png)
!['result'](https://github.com/Moein-Moatali-2006/Pylearn7/blob/main/Image%20Processing/Convolution%202D%20and%20Histogram%20Equalization/Median%20Filter/output/x_ray.png)

