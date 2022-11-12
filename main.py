import cv2
import pyautogui

import test
import test2

while True:
    pyautogui.screenshot('1.png')
    img1 = cv2.imread('1.png')
    img2 = cv2.imread('img/naxida.png')
    video_path='mp4/naxida.mp4'
    Windowdname = 'Windowdname'
    degree = test2.classify_gray_hist(img1, img2)
    print(degree[0])
    if degree[0] > 0.35:
        print("两张图片一样")
        test.PlayVideo(video_path)
    else:
        print("两张图片不一样")