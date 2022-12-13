import numpy as np, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)            # 목적 영상 생성
    rows, cols = img.shape[:2]

    for i in range(rows):                           # 목적 영상 순회 - 역방향 사상
        for j in range(cols):
            x = j - pt[0]                           # 좌표는 x, y 순서
            y = i - pt[1]
            if contain((y, x), img.shape): dst[i, j] = img[y, x]
    return dst

image = cv2.imread("images/translate.jpg", cv2.IMREAD_GRAYSCALE)        # 원본 크기 300*380
if image is None: raise Exception("영상 파일 읽기 오류")

dst1 = translate(image, (30, 80))
dst2 = translate(image, (-70, -50))

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)