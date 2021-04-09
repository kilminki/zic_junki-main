import sys
import numpy as np
import cv2
from ffpyplayer.tests.common import get_media
from ffpyplayer.player import MediaPlayer
import time

    
player = MediaPlayer(get_media('ch09//parasite.mp4'))
val = ''

while val != 'eof':
    frame, val = player.get_frame()
    if val != 'eof' and frame is not None:
        img, t = frame
        # display img