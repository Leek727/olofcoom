import time
import random
from subprocess import Popen, PIPE
from pygame import mixer  # Load the popular external library
import pygame

mixer.init()
mixer.music.load('resources/olofyaoi.ogg')

olof_perc = float(input("Olof percent per second : "))
while True:
    time.sleep(1)
    if random.random() < (olof_perc / 100):
        process = Popen(['python3', 'olofcum.py'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        mixer.music.play()

        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)