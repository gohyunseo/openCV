import cv2

image = cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

(x, y), (w, h) = (180, 37), (15, 10)
roi_img = image[y:y+h, x:x+w]

print("[roi_img] = ")
for row in roi_img:
    for p in row:
        print("%4d" % p, end='')
    print() # 줄바꿈용

cv2.rectangle(image, (x, y, h, w),255, 1)
