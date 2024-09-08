print(2)
        eyes=eyes_detect_left.detectMultiScale(gray,1.1,5)
        print(eyes)
        for eye in eyes:
            x,y,w,h = eye
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),4)