# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:59:03 2021

@author: 이예빈
"""
import cv2, pafy, youtube_dl
 
url = 'https://youtu.be/o4tw2V2_oY8?list=PLZkE0VCtPw3Oma19Qb9HMvR63DWa4-CLt'
video = pafy.new(url)
print('title = ', video.title)
print('author = ', video.author)
print('video.rating = ', video.rating)
print('video.likes = ', video.likes)
print('video.dislikes = ', video.dislikes)
print('video.duration = ', video.duration)

count=0
img=[]

# 1분: 1800, 2분: 3600 3분: 5400 4분: 7200 50초:1500
a = 16*30 # 구간 시작지점 (1초*16)
b = 23*30 # 구간 끝 지 (1초*30)

best = video.getbest(preftype='mp4') # 'webm','3gp'
print('best.resolution= ', best.resolution)
cap=cv2.VideoCapture(best.url)
while(True):
    ret, image = cap.read() # 이미지 사이즈 960x540
    image = cv2.resize(image, (960, 540)) # 30프레임당(1초당) 하나씩 이미지 추출
    if int(cap.get(1))>=a and int(cap.get(1)) <= b: # 프레임 저장할 구간 설
        if(int(cap.get(1)) % 30 == 0): # 30프레임당(1초당) 하나씩 이미지 추출
            count+=1
            print('Saved frame number : ' + str(int(cap.get(1)))) # 프레임 
            img.append(image)
            # cv2.imshow("image", image)
            cv2.imwrite('C:/video/%d.png' %count, image) # 추출된 이미지가 저장되는 경로