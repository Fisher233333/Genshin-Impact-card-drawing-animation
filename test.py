import sys

import cv2
import win32con
import win32gui
from ffpyplayer.player import MediaPlayer
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            sys.exit()
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            sys.exit()
            break
        WindowName = "Video"
        cv2.namedWindow(WindowName, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(WindowName, frame)
        hwnd = win32gui.FindWindow(None, WindowName)  # 获取句柄，然后置顶
        CVRECT = cv2.getWindowImageRect(WindowName)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, CVRECT[2], CVRECT[3], win32con.SWP_SHOWWINDOW)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
