# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:31:03 2021

@author: 이예빈
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
cv2.imread('이미지 파일명')
index = random.randint(len(img))

img = img[index]

#cv2.imshow(img)

img, region = Cannyedge()
img = cv2.rectangel(region)

cv2.imshow(img)

'''
count=1
while True:
    image = cv2.imread('C:/video/05/%d.png' %count)

    median_intensity = np.median(image) # 픽셀 강도의 중간값을 계산
    
    # 중간 픽셀 강도에서 위아래 1 표준 편차 떨어진 값을 임계값으로 지정
    lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
    upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
    
    # 캐니 경계선 감지
    image_canny = cv2.Canny(image, 50,100)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.axis("off")
    plt.show()
    
    plt.imshow(cv2.cvtColor(image_canny, cv2.COLOR_BGR2RGB)), plt.axis("off") # 이미지 출력
    plt.show()

    cv2.imwrite('C:/video/06/%d.png' %(count*100), image_canny)
    count+=1