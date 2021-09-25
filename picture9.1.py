import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 1000))
gray = (241, 235, 255)
blue = (186, 254, 244)
red = (255, 160, 122)
dblue = (111, 144, 255)
white = (254, 254, 251)
gold = (175, 238, 238)
black = (1, 1, 0)
dgray = (154, 154, 154)
green = (0, 81, 66)
yell = (255, 255, 203)
br = (90, 36, 0)

def main():
    layer()
    star()
    udop()
    bear()
    fish()

def layer():
    rect(sc, blue, (0, 0, 600, 450))
    rect(sc, white, (0, 450, 600, 450))
    line(sc, black, (0, 450), (600, 450), 1)

def star():
    circle(sc, yell, (300, 200), 100)
    circle(sc, blue, (300, 200), 95)
    line(sc, yell, (200, 200), (400, 200), 5)
    line(sc, yell, (300, 100), (300, 300), 5)
    for i in range(2):
        a = 200 + i * 200
        circle(sc, yell, (a, 200), 10)
    for j in range(2):
        b = 100 + j * 200
        circle(sc, yell, (300, b), 10)
    circle(sc, yell, (300, 200), 20)

def bear():
    ellipse(sc, gray, (40, 350, 180, 360))
    ellipse(sc, black, (40, 350, 180, 360), 1)
    ellipse(sc, gray, (100, 300, 140, 75))
    ellipse(sc, gray, (200, 460, 80, 40))
    ellipse(sc, black, (200, 460, 80, 40), 1)
    ellipse(sc, gray, (130, 600, 160, 120))
    ellipse(sc, black, (130, 600, 160, 120), 1)
    ellipse(sc, gray, (230, 680, 100, 50))
    ellipse(sc, black, (100, 300, 140, 75), 1)
    ellipse(sc, black, (230, 680, 100, 50), 1)
    circle(sc, black, (170, 330), 5)
    circle(sc, black, (242, 335), 5)
    circle(sc, gray, (120, 315), 15)
    circle(sc, black, (120, 315), 15, 1)
    arc(sc, black, (155, 340, 80, 20), 3.14, 2 * 3.14, 1)

def udop():
    ellipse(sc, dgray, (350, 580, 200, 80))
    ellipse(sc, black, (350, 580, 200, 80), 1)
    ellipse(sc, green, (360, 600, 180, 60))
    ellipse(sc, black, (360, 600, 180, 60), 1)
    line(sc, black, (480, 300), (480, 620), 1)
    lines(sc, br, False, ((230, 550), (250, 500), (280, 450), (330, 400), (390, 350), (480, 300)), 5)

def fish():
    polygon(sc, red, ((350, 680), (370, 720), (395, 700)))
    polygon(sc, dgray, ((350, 680), (370, 720), (395, 700)), 1)
    polygon(sc, red, ((415, 680), (420, 690), (455, 690), (460, 680)))
    polygon(sc, dgray, ((415, 679), (420, 689), (455, 689), (460, 679)), 1)
    polygon(sc, red, ((420, 715), (430, 715), (425, 725)))
    polygon(sc, red, ((440, 715), (450, 715), (445, 725)))
    polygon(sc, dgray, ((420, 715), (430, 715), (425, 725)), 1)
    polygon(sc, dgray, ((440, 715), (450, 715), (445, 725)), 1)
    ellipse(sc, gold, (390, 688, 100, 30))
    ellipse(sc, dgray, (390, 688, 100, 30), 1)
    circle(sc, dblue, (470, 700), 7)
    ellipse(sc, white, (468, 698, 2, 5))

main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()