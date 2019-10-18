from tkinter import *
from random import randrange as rnd, choice
import random
import math
import time


def new_ball():
    global obj_coords, l_obj

    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    vx = random.uniform(-5, 5)
    vy = random.uniform(-5, 5)
    obj_coords.append([x, y, r, vx, vy])
    a = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    l_obj.append(a)
    if time.perf_counter() - time1 > 60:
        table()
        exit()
    root.after(2000, new_ball)


def motion():
    global obj_coords, l_obj
    for i in range(len(l_obj)):
        if (obj_coords[i][0] - obj_coords[i][2] + obj_coords[i][3] < 0) or (
                obj_coords[i][0] + obj_coords[i][3] + obj_coords[i][2] > 800):
            obj_coords[i][3] *= -random.uniform(0.5, 1.5)
        if (obj_coords[i][1] + obj_coords[i][4] - obj_coords[i][2] < 0) or (
                obj_coords[i][1] + obj_coords[i][4] + obj_coords[i][2] > 600):
            obj_coords[i][4] *= -random.uniform(0.5, 1.5)
        canv.move(l_obj[i], obj_coords[i][3], obj_coords[i][4])
        obj_coords[i][0] += obj_coords[i][3]
        obj_coords[i][1] += obj_coords[i][4]

    root.after(8, motion)


def click(event):
    global obj_coords, l_obj, score, score_text
    li = []
    for i in range(len(l_obj)):
        if math.sqrt((event.x - obj_coords[i][0]) ** 2 + (event.y - obj_coords[i][1]) ** 2) < obj_coords[i][2]:
            canv.delete(l_obj[i])
            li.append(i)
            canv.delete(score_text)
            score += 1
            score_text = canv.create_text(2, 0, text="Your Score: " + str(score), anchor=NW, font="Verdana 14")
    for j in li:
        obj_coords.pop(j)
        l_obj.pop(j)


def restart(event):
    global obj_coords, l_obj, score, score_text
    canv.delete(ALL)
    l_obj = []
    obj_coords = []
    score = 0
    score_text = canv.create_text(2, 0, text="Your Score: " + str(score), anchor=NW, font="Verdana 14")


def table():
    global name, score
    # read table
    f = open("table.txt", 'r', encoding='utf-8')
    l = f.readlines()
    f.close()
    flag = 0
    for i in range(len(l)):
        l[i] = list(l[i].split())
    for i in range(len(l)):
        if (l[i][0] == name):
            flag = 1
            if int(l[i][1]) < score:
                l[i][1] = str(score)
    # add new player
    if flag == 0:
        l.append([name, str(score)])
    # write new table
    f = open("table.txt", 'w', encoding='utf-8')
    for i in range(len(l)):
        f.write(l[i][0] + ' ' + l[i][1] + '\n')
    f.close()


def timer():
    global seconds, timer_text
    seconds += 1
    canv.delete(timer_text)
    timer_text = canv.create_text(800, 600, text="Time:" + str(seconds), anchor=SE, font="Verdana 14")
    root.after(1000, timer)


name = input("Enter your name: ")

# canva
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']

l_obj = []
obj_coords = []
score = 0
seconds = 0
score_text = canv.create_text(2, 0, text="Your Score: " + str(score), anchor=NW, font="Verdana 14")
timer_text = canv.create_text(800, 600, text="Time:" + str(seconds), anchor=SE, font="Verdana 14")
time1 = time.perf_counter()
new_ball()
motion()
timer()
canv.bind('<Button-1>', click)
canv.bind_all('<space>', restart)
mainloop()

table()
