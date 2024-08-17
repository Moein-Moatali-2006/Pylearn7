import cv2 
import numpy as np

def create_chessboard(board_size, square_size):
    chessboard = np.zeros((board_size * square_size, board_size * square_size))
    
    for i in range(board_size):
        for j in range(board_size):
            start_x = j * square_size
            start_y = i * square_size
            end_x = start_x + square_size
            end_y = start_y + square_size
            
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)  
            
            cv2.rectangle(chessboard, (start_x, start_y), (end_x, end_y), color, -1)
    
    return chessboard


chessboard_image = create_chessboard(8,50)

cv2.imshow('Chessboard', chessboard_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('chess/chess.png', chessboard_image)
