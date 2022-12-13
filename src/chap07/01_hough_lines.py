import numpy as np, cv2
from Common.hough import draw_houghLines

image = cv2.imread("images/hough.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

blur = cv2.GaussianBlur(image, (5, 5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1, np.pi /180

lines2 = cv2.HoughLines(canny, rho, theta, 80)
dst = draw_houghLines(canny, lines2, 7)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("detecated lines_OpenCV", dst)

cv2.waitKey(0)

