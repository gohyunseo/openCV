import numpy as np
import cv2

# switch case 문을 dictionary로 구현
switch_case = {
    ord('a'):"a키 입력", #ord() 함수 - 문자를 아스키코드로 변환
    ord('b'):"b키 입력",
    0x41:'A키 입력', #16진수 41번 매핑
    int('0x42', 16):'B키 입력',
    37:"왼쪽 화살표키 입력", #0x250000
    38:"윗쪽 화살표키 입력", #0x260000
    39:"오른쪽 화살표키 입력", #0x270000
    40:"아랫쪽 화살표키 입력" #0x280000
}

image = np.ones((200, 300), np.float64) #np.ones 행렬의 크기만큼 1로 채워넣기
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', image)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27:   # 27 : ESC키가 매핑되어있음
        break       #ESC키 누르면 종료
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()