import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 좌클릭")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 우클릭")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 더블클릭 좌클릭")

image = np.full((200, 300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback('Mouse Event1', onMouse) #마우스 콜백 함수

cv2.waitKey(0)
cv2.destroyAllWindows()