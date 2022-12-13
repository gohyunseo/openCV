import numpy as np, cv2

image = cv2.imread("images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

size = (350, 400)

dst1 = cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)         # cv2.INTER_NEAREST 최근접
dst2 = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)          # cv2.INTER_LINEAR 양선형
dst3 = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)           # cv2.INTER_CUBIC 3차회선

cv2.imshow("image", image)
cv2.imshow("openCV-Nearest", dst1)
cv2.imshow("openCV-bilinear", dst2)
cv2.imshow("openCV-cubic", dst3)
cv2.waitKey(0)