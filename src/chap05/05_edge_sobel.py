import numpy as np, cv2
from Common.filters import filter

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)

    dst = cv2.magnitude(dst1, dst2)
    dst1, dst2 = np.abs(dst1), np.abs(dst2)

    dst = cv2.convertScaleAbs(dst)
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")
    return dst, dst1, dst2

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1, # 프리윗 수직 마스크
         -2, 0, 2,
         -1, 0, 1]
data2 = [-1, -2, -1, # 프리윗 수평 마스크
          0, 0, 0,
          1, 2, 1]

dst, dst1, dst2 =differential(image, data1, data2)

# openCV 제공 소벨 에지 계산
dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0)
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1)
dst3 = cv2.convertScaleAbs(dst3)
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("image", image)
cv2.imshow("prewitt edge", dst)
cv2.imshow("dst1 - vertical mask", dst1)
cv2.imshow("dst2 - horizontal mask", dst2)
cv2.imshow("dst3 - vertical_openCV", dst3)
cv2.imshow("dst4 - horizontal_openCV", dst4)
cv2.waitKey(0)
