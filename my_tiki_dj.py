# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:52:27 2021

@author: Marti
"""

# ssh pi@192.168.1.58

import os
import random
from playsound import playsound


if __name__ == "__main__":
    # Take me to Kokomo
    print('takeoff')
    my_tracklist = os.listdir('tracklist')
    while True:
        random.shuffle(my_tracklist)
        for hit in my_tracklist:
            print('Now playing: {}'.format(hit))
            playsound('tracklist/{}'.format(hit))
        
