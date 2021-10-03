import time
import random
from subprocess import Popen, PIPE


olof_perc = float(input("Olof percent per second : "))
while True:
    time.sleep(1)
    if random.random() < (olof_perc / 100):
        process = Popen(['python3', 'olofcum.py'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()