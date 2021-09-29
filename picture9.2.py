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
yell2 = (255, 255, 203)
yell3 = (255, 255, 148)
yell1 = (255, 255, 240)
br = (90, 36, 0)

def main():
    layer()
    star()
    udop(140, 1200, 2)
    bear(140, 1200, 2)
    fish(300, 1150, 2)
    fish(200, 1200, 2)
    fish(110, 1170, 2)
    udop(300, 1200, 3)
    bear(300, 1200, 3)
    fish(300, 1200, 3)
    fish(540, 1100, 3)
    fish(440, 1200, 3)
    udop(1800, 1600, 4)
    bear(1800, 1600, 4)
    fish(1750, 1600, 4)
    fish(1700, 1700, 4)
    fish(1910, 1650, 4)

def layer():
    '''
    рисует фон
    '''
    rect(sc, blue, (0, 0, 600, 450))
    rect(sc, white, (0, 450, 600, 450))
    line(sc, black, (0, 450), (600, 450), 1)

def star():
    '''
    рисует звезду
    '''
    circle(sc, yell1, (300, 200), 100)
    circle(sc, blue, (300, 200), 95)
    line(sc, yell1, (200, 200), (400, 200), 5)
    line(sc, yell1, (300, 100), (300, 300), 5)
    for i in range(2):
        a = 200 + i * 200
        circle(sc, yell1, (a, 200), 30)
        circle(sc, yell2, (a, 200), 20)
        circle(sc, yell3, (a, 200), 10)
    for j in range(2):
        b = 100 + j * 200
        circle(sc, yell1, (300, b), 30)
        circle(sc, yell2, (300, b), 20)
        circle(sc, yell3, (300, b), 10)
    circle(sc, yell1, (300, 200), 40)
    circle(sc, yell2, (300, 200), 30)
    circle(sc, yell3, (300, 200), 20)

def bear(x, y, r):
    '''
    рисует медведа
    x, y - координаты
    r - размер медведа, в сколько раз уменьшится (r > 1) / увеличится (0 < r < 1)
    '''
    ellipse(sc, gray, (x / r, y / r, 180 / r, 360 / r))
    ellipse(sc, black, (x / r, y / r, 180 / r, 360 / r), 1)
    ellipse(sc, gray, ((x + 60) / r, (y - 50) / r, 140 / r, 75 / r))
    ellipse(sc, gray, ((x + 160) / r, (y + 110) / r, 80 / r, 40 / r))
    ellipse(sc, black, ((x + 160) / r, (y + 110) / r, 80 / r, 40 / r), 1)
    ellipse(sc, gray, ((x + 90) / r, (y + 250) / r, 160 / r, 120 / r))
    ellipse(sc, black, ((x + 90) / r, (y + 250) / r, 160 / r, 120 / r), 1)
    ellipse(sc, gray, ((x + 190) / r, (y + 330) / r, 100 / r, 50 / r))
    ellipse(sc, black, ((x + 60) / r, (y - 50) / r, 140 / r, 75 / r), 1)
    ellipse(sc, black, ((x + 190) / r, (y + 330) / r, 100 / r, 50 / r), 1)
    circle(sc, black, ((x + 130) / r, (y - 20) / r), 5 / r)
    circle(sc, black, ((x + 202) / r, (y - 15) / r), 5 / r)
    circle(sc, gray, ((x + 80) / r, (y - 35) / r), 15 / r)
    circle(sc, black, ((x + 80) / r, (y - 35) / r), 15 / r, 1)
    arc(sc, black, ((x + 115) / r, (y - 10) / r, 80 / r, 20 / r), 3.14, 2 * 3.14, 1)

def udop(x, y, r):
    '''
    рисует удочку и прорубь
    x, y - координаты
    r - размер медведа, в сколько раз уменьшится (r > 1) / увеличится (0 < r < 1)
    '''
    ellipse(sc, dgray, ((x + 310) / r, (y + 230) / r, 200 / r, 80 / r))
    ellipse(sc, black, ((x + 310) / r, (y + 230) / r, 200 / r, 80 / r), 1)
    ellipse(sc, green, ((x + 320) / r, (y + 250) / r, 180 / r, 60 / r))
    ellipse(sc, black, ((x + 320) / r, (y + 250) / r, 180 / r, 60 / r), 1)
    line(sc, black, ((x + 440) / r, (y - 50) / r), ((x + 440) / r, (y + 270) / r), 1)
    lines(sc, br, False, (((x + 190) / r, (y + 200) / r), ((x + 210) / r, (y + 150) / r), ((x + 240) / r, (y + 100) / r), ((x + 290) / r, (y + 50) / r), ((x + 350) / r, y / r), ((x + 440) / r, (y - 50) / r)), 5 // r)

def fish(x, y, r):
    '''
    рисует рыбу
    x, y - координаты
    r - размер медведа, в сколько раз уменьшится (r > 1) / увеличится (0 < r < 1)
    '''
    polygon(sc, red, (((x + 310) / r, (y + 330) / r), ((x + 330) / r, (y + 370) / r), ((x + 355) / r, (y + 350) / r)))
    polygon(sc, dgray, (((x + 310) / r, (y + 330) / r), ((x + 330) / r, (y + 370) / r), ((x + 355) / r, (y + 350) / r)), 1)
    polygon(sc, red, (((x + 375) / r, (y + 330) / r), ((x + 380) / r, (y + 340) / r), ((x + 415) / r, (y + 340) / r), ((x + 420) / r, (y + 330) / r)))
    polygon(sc, dgray, (((x + 375) / r, (y + 330) / r), ((x + 380) / r, (y + 340) / r), ((x + 415) / r, (y + 340) / r), ((x + 420) / r, (y + 330) / r)), 1)
    polygon(sc, red, (((x + 380) / r, (y + 365) / r), ((x + 390) / r, (y + 365) / r), ((x + 385) / r, (y + 375) / r)))
    polygon(sc, red, (((x + 400) / r, (y + 365) / r), ((x + 410) / r, (y + 365) / r), ((x + 405) / r, (y + 375) / r)))
    polygon(sc, dgray, (((x + 380) / r, (y + 365) / r), ((x + 390) / r, (y + 365) / r), ((x + 385) / r, (y + 375) / r)), 1)
    polygon(sc, dgray, (((x + 400) / r, (y + 365) / r), ((x + 410) / r, (y + 365) / r), ((x + 405) / r, (y + 375) / r)), 1)
    ellipse(sc, gold, ((x + 350) / r, (y + 338) / r, 100 / r, 30 / r))
    ellipse(sc, dgray, ((x + 350) / r, (y + 338) / r, 100 / r, 30 / r), 1)
    circle(sc, dblue, ((x + 430) / r, (y + 350) / r), 7 // r)
    ellipse(sc, white, ((x + 428) / r, (y + 348) / r, 2 // r, 5 // r))

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
