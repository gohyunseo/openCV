import numpy as np
import cv2

ch0 = np.zeros((2, 4), np.uint8) + 10
ch1 = np.ones((2, 4), np.uint8) * 20
ch2 = np.zeros((2, 4), np.uint8); ch2[:] = 30

list_bar = [ch0, ch1, ch2]
merge_bgr = cv2.merge(list_bar) # 채널 합성
split_bgr = cv2.split(merge_bgr) # 채널 분리 : 컬러영상 -> 3채널 분리

print('split_bgr 행렬 형태 : ', np.array(split_bgr).shape)
print('merge_bgr 행렬 형태 : ', merge_bgr.shape)

print('[ch0] = \n%s' % ch0) # 단일 채널 원소 출력
print('[ch1] = \n%s' % ch1)
print('[ch2] = \n%s' % ch2)
print('[merge_bgr] = \n%s\n' % merge_bgr) # 다중 채널 원소 출력

print('[split_bgr[0]] = \n%s' % split_bgr[0])
print('[split_bgr[1]] = \n%s' % split_bgr[1])
print('[split_bgr[2]] = \n%s' % split_bgr[2])
