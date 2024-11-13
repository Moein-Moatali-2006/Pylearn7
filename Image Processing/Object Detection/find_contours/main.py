import cv2
import numpy as np


def findContours(image, mode, method):
    image = image.astype(np.uint8)
    
    contours = []
    visited = np.zeros_like(image, dtype=bool)  
    
    def trace_contour(start_point):
        contour = []
        current_point = start_point
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        direction_idx = 0
        
        while True:
            for i in range(4):
                next_direction = (direction_idx + i) % 4
                dy, dx = direction[next_direction]
                next_point = (current_point[0] + dy, current_point[1] + dx)
            
                if (0 <= next_point[0] < image.shape[0] and
                    0 <= next_point[1] < image.shape[1] and
                    image[next_point] == 255 and not visited[next_point]):
                    
                    contour.append(next_point)
                    visited[next_point] = True
                    current_point = next_point
                    direction_idx = next_direction  
                    break
            else:
                break

        return contour
    
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 255 and not visited[(y, x)]:
                visited[(y, x)] = True
                contour = trace_contour((y, x))
                if contour:
                    contours.append(np.array(contour))
   
    
    hierarchy = np.array([]) 
    return contours, hierarchy

if __name__ == "__main__":
    image = cv2.imread('wolf.jpg', cv2.IMREAD_GRAYSCALE)
    
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = findContours(binary_image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    
    result_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    for contour in contours:
        for point in contour:
            cv2.circle(result_image, (point[1], point[0]), 1, (0, 0, 255), -1)  
    
    cv2.imwrite('Contours.jpg', result_image)
