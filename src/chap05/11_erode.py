import numpy as np, cv2

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

data = [0, 1, 0,
        1, 1, 1,
        0, 1, 0]

mask = np.array(data, np.uint8).reshape(3, 3)
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
# 128보다 작은값은 0으로 큰 값은 255로 셋팅

dst = cv2.erode(th_img, mask)

cv2.imshow("image", image)
cv2.imshow("erod", dst)

cv2.waitKey(0)