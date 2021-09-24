# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:59:03 2021

@author: 이예빈
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture('C:/video/05.mp4')

count=0
img=[]
'''
3:16~3:23
4:23~4:27
5:39~5:47
6:14~6:20 => 25초

'''

# 1분: 1800, 2분: 3600 3분: 5400 4분: 7200 50초:1500
a = 16*30 # 35x30  = 1050+60040초 구간~
b = 23*30 # 초 구



while(vid.isOpened()):
    ret, image = vid.read() # 이미지 사이즈 960x540
    image = cv2.resize(image, (960, 540)) # 30프레임당 하나씩 이미지 추출
    if int(vid.get(1))>=a and int(vid.get(1)) <= b:
        if(int(vid.get(1)) % 15 == 0):
            count+=1
            print('Saved frame number : ' + str(int(vid.get(1)))) # 추출된 이미지가 저장되는 경로
            img.append(image)
            # cv2.imshow("image", image)
            cv2.imwrite('C:/video/%d.png' %count, image)

vid.release()