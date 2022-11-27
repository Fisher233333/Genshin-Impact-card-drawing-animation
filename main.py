import cv2
import pyautogui

import test
import test1
import test2

while True:
    pyautogui.screenshot('1.png')
    img1 = cv2.imread('1.png')
    # 第一步：更换图片名字   img2 = cv2.imread('img/***.png')
    img2 = cv2.imread('img/gongzi.png')
    # 第一步：更换要播放的视频   video_path='mp4/***.mp4'
    video_path='mp4/gongzi.mp4'
    Windowdname = 'Windowdname'
    degree = test2.classify_gray_hist(img1, img2)
    # print(degree[0])
    if degree[0] > 0.35:
        print("两张图片一样")
        test1.PlayVideo(video_path)
    else:
        pass