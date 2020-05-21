import struct
import os
import pygame
import time


pygame.init()

screen = pygame.display.set_mode((800, 800))



white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))



smallestX = 0
smallestY = 0
BiggestX = 0
BiggestY = 0


def drawpmd(filename, scherm, c):

    size = os.path.getsize(filename)
    scale = 6
    print ("Drawing {} size is {}".format(filename, size))
    t = 0
    file =  open(filename,"rb")

    xy = []

    p = 0
    smallestX = 0
    smallestY = 0


    while True:
        f = struct.unpack('i', file.read(4))[0]
        v = int(f / 10000000)

        if t < 8:
            print (v)
        if p == 0:
            p = 1
            x = v
            if x < smallestX:
                smallestX = x

        else:
            p = 0
            y = v
            if y < smallestY:
                smallestY = y

            xy.append([x,y])
            try:
                pygame.draw.circle(scherm, c, (int(x) + 360, int(y) + 360), 3)
            except:
                print ("err; {} - {}".format(x,y))

        t = t + 1
        if t == int(size/4):
            print ("SmallestX: {}   SmallestY: {}".format(smallestX, smallestY))
            break


screen.fill(black)

drawpmd("sd//cup0000//LC.pmd", screen, red)
drawpmd("sd//cup0000//LU.pmd", screen, purple)
drawpmd("sd//cup0000//LP.pmd", screen, orange)
drawpmd("sd//testbur//S01.pmd", screen, blue)

pygame.display.flip()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    
