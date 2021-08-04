# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:52:27 2021

@author: Marti
"""

# ssh pi@192.168.1.58
#python3 /home/pi/Documents/Python/tikibar/my_tiki_dj.py

import os
import random
#from playsound import playsound
import pygame


if __name__ == "__main__":
    # Take me to Kokomo
    print('takeoff')
    pygame.mixer.init()
    my_tracklist = os.listdir('/home/pi/Documents/Python/tikibar/tracklist')
    while True:
        random.shuffle(my_tracklist)
        for hit in my_tracklist:
            print('Now playing: {}'.format(hit))
            #playsound('tracklist/{}'.format(hit))
            pygame.mixer.music.load('/home/pi/Documents/Python/tikibar/tracklist/{}'.format(hit))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        
