import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200 # [:] 전체영역 선택

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #윈도우 이름을 설정한 후 해당이름으로 윈도우 생성
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 윈도우 크기 재조정 가능


cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300) # 사이즈 리사이징 (크기변경)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()