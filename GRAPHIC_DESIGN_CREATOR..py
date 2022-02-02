import tkinter as tk
from tkinter import *
import turtle


def onclock():

    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    t.penup()
    t.goto(-180, -100)
    t.pendown()
    c = 0
    d = 0
    t.pensize(2)
    run = True
    while run:
        if btn1:
            t.penup()
            t.goto(-10, 80)
            t.pendown()
            for i in range(4):
                t.forward(80)
                t.right(90)
            t.right(5)
            c+=1
            if c>=360/9:
                c = 2
                d += 2
                if d>=3:
                    break


def onclock2():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    t.penup()
    t.goto(-10, 80)
    t.pendown()
    c = 0
    d = 0
    t.pensize(2)
    run = True
    while run:
        if btn2:
            for i in range(5):
                t.pencolor('white')
                t.forward(120)
                t.right(60)
                # t.forward(50)
                # t.backward(10)
                # t.forward(50)
            t.left(50)
            t.right(30)
            t.forward(90)
            # t.right(25)
            c += 1
def onclock3():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    t.penup()
    t.goto(-180, -100)
    t.pendown()
    c = 0
    d = 0
    t.pensize(2)
    run = True
    while run:
        t.penup()
        t.goto(-10, 80)
        t.pendown()
        for i in range(10):
            t.forward(90)
            t.backward(30)
            t.left(60)
        # t.left(20)
        t.forward(50)
        t.right(50)
        c += 1
        if c >= 10:
            c = 1
            d += 1
            if d >= 5:
                break
def onclock4():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    t.penup()
    t.goto(30, -20)
    t.pendown()
    c = 0
    d = 0
    t.pensize(2)
    run = True
    while run:
        for i in range(6):
            t.forward(80)
            t.backward(60)
            t.forward(56)
            t.right(50)
            # t.backward(40)
        t.right(90)
        t.right(50)
        # t.forward(55)
        t.right(50)
        t.left(55)
        c += 1
        if c >= 50:
            c = 1
            d += 1
            if d >= 5:
                break
def onclock5():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    c = 0
    d = 0
    t.pensize(2)
    t.penup()
    t.goto(-50, 200)
    t.pendown()
    c = 0
    d = 0
    for i in range(250):
        t.forward(c)
        t.right(d)
        c += 3
        d += 1
        if d == 480:
            break

def onclock6():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    c = 0
    d = 0
    t.pensize(2)
    c = 0
    d = 0
    if btn6:
        import time
        t.penup()
        t.goto(10, 0)
        t.pendown()
        colours = ['red', 'yellow', 'green', 'purple', 'orange', 'white']
        s.bgcolor('black')
        for x in range(500):
            t.pencolor(colours[x % 6])
            t.width(x/100+1)
            t.forward(x)
            t.left(59)
        time.sleep(2)

        pass


mainwin = tk.Tk()
mainwin.title("hahaha")

btn1 = tk.Button(mainwin, text="button-1 ", command=onclock, width=12,pady=5)
btn1.grid(row=0, column=1)
l1 = Label(mainwin, text="DESIGN-1")
l1.grid(row=0,column=0)

btn2 = tk.Button(mainwin, text="button-2", command=onclock2, width=12,pady=5)
btn2.grid(row=2, column=1)
l2 = Label(mainwin, text="DESIGN-2")
l2.grid(row=2, column=0)

btn3 = tk.Button(mainwin, text="button-3", command=onclock3, width=12,pady=5)
btn3.grid(row=4, column=1)
l3 = Label(mainwin, text="DESIGN-3")
l3.grid(row=4, column=0)

btn4 = tk.Button(mainwin, text="button-4", command=onclock4, width=12,pady=5)
btn4.grid(row=6, column=1)
l4 = Label(mainwin, text="DESIGN-4")
l4.grid(row=6, column=0)

btn5 = tk.Button(mainwin, text="button-5", command=onclock5, width=12,pady=5)
btn5.grid(row=8, column=1)
l5 = Label(mainwin, text="DESIGN-5")
l5.grid(row=8, column=0)

btn6 = tk.Button(mainwin, text="button-6", command=onclock6, bg="black", fg="white", width=12,pady=5)
btn6.grid(row=10, column=1)
l6 = Label(mainwin, text="FINAL DESIGN.", bg="black", fg="white")
l6.grid(row=10, column=0)

mainwin.mainloop()