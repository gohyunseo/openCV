import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200 # [:] 전체영역 선택

title1, title2 = 'position1', 'position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #윈도우 이름을 설정한 후 해당이름으로 윈도우 생성
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 윈도우 크기 재조정 가능

cv2.moveWindow(title1, 150, 150) #지정된 위치(150, 150)로 이동. 기준점은 좌측 상단
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destroyAllWindows()