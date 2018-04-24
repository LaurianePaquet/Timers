#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import time
import webbrowser
import random as rd

def writeHTML(pathImg, pathHTLM):
    f = open(pathHTLM, 'w')
    
    message = """<!DOCTYPE html>
    <html>
    <style>
    html, body {
        height: 100%;
    }

    img {
        display: block;
        margin: auto;
        height: 97%;
        width: auto;
    }
    </style>

    <body>
    <img src=" """ + pathImg + """ " alt="">
    </body>
    </html>"""

    f.write(message)
    f.close()

def popupImg(imgName, dirPath):
    """
    create HTML popup and activate it
    """
    pathImg = dirPath + '/img/' + str(imgName)
    pathHTLM = dirPath + '/imgTimer.html'

    writeHTML(pathImg, pathHTLM)

    #Change path to reflect file location
    filename = 'file://' + pathHTLM
    webbrowser.open_new_tab(filename)

def timer(dirPath, minutes, typePause):
    timeWaiting = minutes*60
    if timeWaiting == 0:
        timeWaiting = 1

    # Initial call to print 0% progress
    printProgressBar(0, timeWaiting, prefix = typePause, suffix = 'Complete', length = 50)
    for t in range(0, timeWaiting):
        time.sleep(1)
        # Update Progress Bar
        printProgressBar(t + 1, timeWaiting, prefix = typePause, suffix = 'Complete', length = 50)

    listFiles = os.listdir(dirPath + '/img/')
    popupImg(listFiles[rd.randint(0, len(listFiles) - 1)], dirPath)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def main(minutesWork, minutesBreak=0, nbRepet=1, sound=0):
    dirPath = os.path.dirname(os.path.abspath(__file__))

    for i in range(nbRepet):
        for j in [[minutesWork, "afplay /System/Library/Sounds/Purr.aiff", "  Boulot:"], 
                 [minutesBreak, "afplay /System/Library/Sounds/Submarine.aiff", "  Pause: "]]:
            if sound == 1:
                os.system(j[1])
            timer(dirPath, j[0], j[2])
            if sound == 1:
                os.system(j[1])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("pas assez d'arguments")
    elif len(sys.argv) < 3:
        main(int(sys.argv[1]))
    elif len(sys.argv) < 4:
        main(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) < 5:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) < 6:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        print("trop d'arguments")