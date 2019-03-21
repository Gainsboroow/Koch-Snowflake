"""
Made by Gainsboroow 
Github account : https://github.com/Gainsboroow
Github repository : https://github.com/Gainsboroow/Koch-Snowflake

Right click to display the next step.
"""

import pygame
from math import *
from pygame.locals import *

height, width = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Koch Snowflake")

debX, debY = 50, 150
dist = 500
x = debX + dist*cos(pi/3)
y = debY + dist*sin(pi/3)
points = [ [(debX, debY), (debX+dist,debY)], [(x,y), (debX,debY)], [(debX+dist,debY),(x,y)] ]

def nextGen():
    for b in range(len(points)):
        nextPoints = []
        for pt1, pt2 in zip(points[b][:-1], points[b][1:]):
            vect = tuple((pt2[a] - pt1[a])/3 for a in range(2))
            nPt1 = tuple(pt1[a] + vect[a] for a in range(2))
            nPt3 = tuple(pt2[a] - vect[a] for a in range(2))

            nPt2 = (nPt1[0] + vect[0]*cos(-pi/3) - vect[1]*sin(-pi/3),
                    nPt1[1] + vect[0]*sin(-pi/3) + vect[1]*cos(-pi/3))

            #print("Pt 1 :", pt1, "Pt 2 :", pt2, "\nVect :", vect, "\nnPt1", nPt1, "\nnPt2", nPt2, "\nnPt3", nPt3)
            nextPoints.extend([pt1, nPt1, nPt2, nPt3, pt2])
        
        points[b] = list(nextPoints)

def update():
    for b in range(len(points)):
        for pt1, pt2 in zip(points[b][:-1], points[b][1:]):
            pygame.draw.line(screen, (255,255,255), pt1, pt2, 1)

    pygame.display.update()

update()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            nextGen()
            screen.fill((0,0,0))
            update()
