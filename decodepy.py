import struct
import os
import pygame


pygame.init()
scherm1 = pygame.display.set_mode((1100,1100))
scherm1.fill((255,255,255))


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


def drawpmd(filename, scherm, c):

    size = os.path.getsize(filename)

    t = 0
    file =  open(filename,"rb")

    xy = []

    p = 0

    while True:
        v = float(struct.unpack('i', file.read(4))[0])/1000000
        if p == 0:
            p = 1
            x = v
        else:
            p = 0
            y = v
            xy.append([x,y])

            pygame.draw.circle(scherm, c, (int(x/4)+500,int(y/4)+400), 10)
            
            
        t = t + 1
        if t == int(size/4):
            break
c = 300

drawpmd("D:\\quincy\\apple00\\LA.pmd", scherm1, red)
c = c + 100
drawpmd("D:\\quincy\\apple00\\LE.pmd", scherm1, purple)
c = c + 100
drawpmd("D:\\quincy\\apple00\\LP.pmd", scherm1, orange)
c = c + 100
drawpmd("D:\\quincy\\apple00\\LL.pmd", scherm1, yellow)



pygame.display.flip()



    
