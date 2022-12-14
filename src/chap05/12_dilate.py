import numpy as np, cv2

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask)
dst3 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)   #팽창 -> 침식
dst4 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask)  #침식 -> 팽창

cv2.imshow("image", image)
cv2.imshow("OpenCV dilate", dst2)
cv2.imshow("OpenCV open", dst3)
cv2.imshow("OpenCV close", dst4)
cv2.waitKey(0)