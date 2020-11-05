import struct
import os
import pygame
import time
import numpy as np
import coordcalc


pygame.init()
screen = pygame.display.set_mode((800, 800))

def readFloat(filepointer):
    rawbytes = filepointer.read(4)
    [f] = struct.unpack('f', rawbytes)
    return f

def writeFloat(filepointer, value):
    rawbytes = struct.pack('f', value)
    filepointer.write(rawbytes)

def readInt(filepointer):
    rawbytes = filepointer.read(4)
    [i] = struct.unpack('i', rawbytes)
    return i

def writeFloat(filepointer, value):
    rawbytes = struct.pack('i', value)
    filepointer.write(rawbytes)

def drawpmd(filename, outputscreen, drawcolor):
    file =  open(filename,"rb")
    magic = file.read(1) # Read first byte of file, should be 0x01

    segments = readInt(file)
    print ("Drawing {} with {} Segments".format(filename, segments))

    scale = 4
    segcount = 0
    while segcount < segments:
        segcount = segcount + 1
        points = readInt(file)
        print("== [ Segment {} - points: {} ] ==".format(segcount, points))
        pointcount = 0
        while pointcount < points:
            pointcount = pointcount + 1
            pointX = readFloat(file)
            pointY = readFloat(file)

            ax, ay = coordcalc.angles_to_coord(pointX, pointY)
            offset = 6
            ax = ax + offset
            ay = ay
            scale2 = 20

            print ("{}/{}: {} - {} = {} - {}".format(segcount, pointcount, pointX, pointY, ax, ay))

            pygame.draw.circle(outputscreen, drawcolor, (int(pointX*scale), int(pointY*scale) ), 2)
            pygame.draw.circle(outputscreen, (0,255,0), (int(ax * scale2), int(ay * scale2)), 2)
            pygame.display.flip()
            time.sleep(0.001)
        pygame.display.flip()
        time.sleep(1)




screen.fill((0,0,0))
color = (255,0,0)

drawpmd("sd//testbur//S01.pmd", screen, color)
#
# drawpmd("sd//cup0000//LC.pmd", screen, color)
# drawpmd("sd//cup0000//LU.pmd", screen, color)
# drawpmd("sd//cup0000//LP.pmd", screen, color)
#
# drawpmd("sd//cup0000//S1.pmd", screen, color)
# drawpmd("sd//cup0000//S2.pmd", screen, color)
# drawpmd("sd//cup0000//S3.pmd", screen, color)
# drawpmd("sd//cup0000//S4.pmd", screen, color)
# drawpmd("sd//cup0000//S5.pmd", screen, color)
# drawpmd("sd//cup0000//S6.pmd", screen, color)

drawpmd("test.pmd", screen, color)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    
