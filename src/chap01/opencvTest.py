import numpy as np
import cv2 #opencv의 사용버전

image = np.zeros((300, 400), np.uint8) #300,400 크기의 데이터셋에 0으로 채우기
image.fill(200) #색상 200으로 채우기 (아마 회색)

cv2.imshow("window title", image)
cv2.waitKey(0)
cv2.destroyWindow() #이미자 창으로 띄우기