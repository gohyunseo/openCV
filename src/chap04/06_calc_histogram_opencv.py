import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]):   #행렬 원소의 1차원 히스토그랜 계산
    hist = np.zeros((hsize,1), np.float32)     #히스토그램 누적 행렬
    gap = ranges[1] / hsize     #계급 간격

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            idx = int(image.item(i, j) / gap)

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None :
    raise Exception("영상 파일 읽기 오류 발생")

hsize, ranges = [32], [0, 256]      # 히스토그램 간격수, 값 범위
gap = ranges[1] / hsize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap)          # 파이썬 기본 내장 range와 같음
hist1 = calc_histo(image, hsize[0], ranges)
hist2 = cv2.calcHist([image], [0], None, hsize, ranges)
hist3, bins = np.histogram(image, ranges_gap)

print("User 함수 : \n", hist1.flatten())
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수: \n", hist3.flatten())

cv2.imshow("image", image)
cv2.waitKey(0)