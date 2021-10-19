from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x700')

canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple', 'pink', 'aquamarine', 'lime', 'teal', 'salmon', 'olive', 'khaki']

def new_ball():
    '''
    функция отрисовывающая шарик
    фиксирующая набранное кол-во очков
    двигающая шарики
    '''
    global x1, y1, x2, y2, x3, y3, x4, y4, r1, r2, r3, r4, o1, o2, o3, o4, text, nap
    canv.delete(ALL)
    x1 = rnd(100, 700)
    y1 = rnd(100, 500)
    x2 = rnd(100, 700)
    y2 = rnd(100, 500)
    x3 = rnd(100, 700)
    y3 = rnd(100, 500)
    x4 = rnd(100, 700)
    y4 = rnd(100, 500)
    r1 = rnd(30, 50)
    r2 = rnd(30, 50)
    r3 = rnd(30, 50)
    r4 = rnd(30, 50)
    o1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0)
    o2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=choice(colors), width=0)
    o3 = canv.create_oval(x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill=choice(colors), width=0)
    o4 = canv.create_oval(x4 - r4, y4 - r4, x4 + r4, y4 + r4, fill=choice(colors), width=0)
    root.after(1000, new_ball)
    canv.delete(text)
    text = canv.create_text(100, 50, text='Счёт : ' + str(sc), font='Arial 20', fill='white')


def move_ball():
    '''
    функция обеспечивающая движение шариков
    '''
    global o1, o2, o3, o4, x2, x1, y2, y1, y3, x3, y4, x4
    x2 = rnd(0, 5)
    y2 = rnd(0, 6)
    x1 = rnd(0, 7)
    y1 = rnd(0, 8)
    x3 = rnd(0, 5)
    y3 = rnd(0, 6)
    x4 = rnd(0, 7)
    y4 = rnd(0, 8)
    canv.move(o1, x1, y1)
    canv.move(o2, x2, y2)
    canv.move(o3, x3, y3)
    canv.move(o4, x4, y4)
    canv.after(20, move_ball)

def click(event):
    '''
    функция ведущая подсчет очков
    бомба и обнуление
    '''
    global sc, text
    a1 = ((event.x - x1) ** 2 + (event.y - y1) ** 2) ** 0.5
    a2 = ((event.x - x2) ** 2 + (event.y - y2) ** 2) ** 0.5
    a3 = ((event.x - x3) ** 2 + (event.y - y3) ** 2) ** 0.5
    a4 = ((event.x - x4) ** 2 + (event.y - y4) ** 2) ** 0.5
    if a1 < r1:
        sc += 1
    elif a2 < r2:
        sc += 1
    elif a3 < r3:
        sc += 1
    elif a4 < r4:
        sc = 0
        canv.delete(ALL)
        text = canv.create_text(200, 150, text='Счёт : 0. BOMB!!!', font='Arial 40', fill='red')
        bomb()

def bomb():
    '''
    рисунок бомбы
    '''
    canv.create_line(350, 500, 450, 200, fill='yellow', width=3)
    canv.create_oval(300, 400, 500, 600, fill='grey', width=0)
    canv.create_rectangle(370, 340, 410, 410, fill='grey', width=0)

def yourname():
    global name, sc
    root.title("ПОЙМАЙ ШАРИК")
    label = Label(root, font=("Ubuntu", 22))
    e = Entry(root, width=20)
    b = Button(root, text="Сохранить мой результат")
    e.pack()
    b.pack()
    name = e.get()
    string = name + str(sc) + '\n'
    file = open('results.txt', 'a')
    file.write(string)
    file.close()
    with open('results.txt', 'a') as f:
        f.write(string)

text = 0
sc = 0
canv.bind('<Button-1>', click)
new_ball()
move_ball()
yourname()
root.mainloop()