import numpy as np, cv2

image = cv2.imread("images/affine.jpg", cv2.IMREAD_GRAYSCALE)        # 원본 크기 320*330
if image is None: raise Exception("영상 파일 읽기 오류")

center = (200, 200)
angle, scale = 30, 1
size = image.shape[::-1]

pt1 = np.array([(30, 70), (20, 240), (300, 110)], np.float32)
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)

aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

dst1 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
dst2 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)