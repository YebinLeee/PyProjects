# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:03:44 2021

@author: 이예빈
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

count=1

while True:    
    img = cv2.imread('C:/video/05/%d.png' %count)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imwrite('C:/video/01-2/%d.png' %(count*1000), img_hsv)
    
    low_white = np.array([107, 107, 107])
    high_white = np.array([255, 255, 255])
    dst1 = cv2.inRange(img, low_white, high_white)
    
    # dst1_hsv=cv2.cvtColor(dst1, cv2.COLOR_BGR2HSV)
    # dst2 = cv2.inRange(img, (50, 150, 0), (80, 255, 255))
    
    
    # plt.imshow(img), plt.axis("off") # 이미지 출력
    # plt.show()
    
    plt.imshow(dst1), plt.axis("off") # 이미지 출력
    plt.show()
    
    # plt.imshow(dst2), plt.axis("off") # 이미지 출력
    # plt.show()
    
    count+=1