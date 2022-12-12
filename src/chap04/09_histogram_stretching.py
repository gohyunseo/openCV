import numpy as np, cv2
from Common.histogram import draw_histo

def search_value_idx(hist, bias = 0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)  #abs: 절대값구하기
        if hist[idx] > 0:
            return idx
    return -1


image = cv2.imread("dst.jpg",cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상 파일 읽기 오류 발생") #예외처리

bsize, ranges = [64],[0, 256]
hist = cv2.calcHist([image], [0], None, bsize, ranges)

bin_width = ranges[1] /bsize[0]
high = search_value_idx(hist, bsize[0] - 1) * bin_width
low = search_value_idx(hist, 0) * bin_width

idx = np.arange(0, 256)
idx = (idx - low) * 255 / (high - low)
idx[0:int(low)] = 0
idx[int(high+1):] = 255

dst = cv2.LUT(image, idx.astype('uint8'))
hist_dst = cv2.calcHist([dst], [0], None, bsize, ranges)


hist_img = draw_histo(hist, (200, 360))
hist_dst_img = draw_histo(hist_dst, (200, 360))

print("high_value=", high)
print("low_value=", low)

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.imshow("hist_image", hist_img)
cv2.imshow("hist_dst_image", hist_dst_img)
cv2.waitKey(0)