import pygame
from pygame.locals import *
import cv2
import sys
import time
import win32con
import win32gui
from ffpyplayer.player import MediaPlayer

def PlayVideo(video_path):
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    FPS = int(round(video.get(cv2.CAP_PROP_FPS)))
    Width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    Height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    pygame.init()
    pygame.display.set_caption('OpenCV Video Player on Pygame')
    screen = pygame.display.set_mode((Width, Height), 0, 32)
    screen.fill([0, 0, 0])
    hwnd = win32gui.FindWindow(None, 'OpenCV Video Player on Pygame')  # 获取句柄，然后置顶
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, -10, -38, 0, 0, win32con.SWP_NOSIZE)
    num = 0
    while True:
        if num == 0:
            T0 = time.time()
        audio_frame, val = player.get_frame()
        if time.time() - T0 > num * (1. / FPS):
            ret, frame = video.read()
            TimeStamp = video.get(cv2.CAP_PROP_POS_MSEC)
            if ret == False:
                print('Total Time:', time.time() - T0)
                pygame.quit()
                sys.exit()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.transpose(frame)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0, 0))
            pygame.display.update()
            num += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                sys.exit()

