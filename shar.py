from tkinter import *
from random import randrange as rnd, choice
import random
import math
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
label1 = Label(text="Количество очков: 0", fg="#eee", bg="#333")
label1.pack()
colors = ['red','orange','yellow','green','blue']

def new_ball():
    global obj_coords,l_obj

    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    vx=random.uniform(-5,5)
    vy=random.uniform(-5,5)
    obj_coords.append([x,y,r,vx,vy])
    a=canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    l_obj.append(a)
    root.after(1000,new_ball)


def motion():
    global obj_coords, l_obj
    for i in range(len(l_obj)):
        if (obj_coords[i][0]-obj_coords[i][2]+obj_coords[i][3]<0) or (obj_coords[i][0]+obj_coords[i][3]+obj_coords[i][2]>800):
            obj_coords[i][3]*=-random.uniform(0.5,1.5)
        if (obj_coords[i][1]+obj_coords[i][4]-obj_coords[i][2]< 0) or (obj_coords[i][1]+obj_coords[i][4] +obj_coords[i][2]> 600):
            obj_coords[i][4] *= -random.uniform(0.5, 1.5)
        canv.move(l_obj[i], obj_coords[i][3], obj_coords[i][4])
        obj_coords[i][0]+=obj_coords[i][3]
        obj_coords[i][1] += obj_coords[i][4]

    root.after(10, motion)

def click(event):
    global obj_coords, l_obj

    print(event.x,event.y)
    li=[]
    for i in range(len(l_obj)):
        if math.sqrt((event.x-obj_coords[i][0])**2+(event.y-obj_coords[i][1])**2)<obj_coords[i][2]:
            canv.delete(l_obj[i])
            li.append(i)
    for j in li:
        obj_coords.pop(j)
        l_obj.pop(j)
    print(obj_coords)



l_obj=[]
obj_coords=[]
new_ball()
motion()
canv.bind('<Button-1>', click)
mainloop()