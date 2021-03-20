from tkinter import filedialog,Tk,Button,Label,Scale,Spinbox,IntVar,StringVar
import circle_detection
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cv2 import cv2

color = 'white'
plt.rcParams['text.color'] = color
plt.rcParams['axes.labelcolor'] = color
plt.rcParams['xtick.color'] = color
plt.rcParams['ytick.color'] = color

dp = 1
minDist = 100
param1 = 50
param2 = 30
minRadius = 0
maxRadius = 0
filename = ""
root = Tk()
a_dp = StringVar()
a_dp.set(dp)
a_minDist = StringVar()
a_minDist.set(minDist)
a_param1 = StringVar()
a_param1.set(param1)
a_param2 = StringVar()
a_param2.set(param2)
a_minRadius = IntVar()
a_minRadius.set(minRadius)
a_maxRadius = IntVar()
a_maxRadius.set(maxRadius)
root.config(bg = "#0a0b11")
root.title("Actividad 1")
root.resizable(0, 0)
root.geometry("+100+75")
root.iconbitmap("icon.ico")

def set_values(a1,a2,a3,a4,a5,a6):
    global dp
    global minDist
    global param1
    global param2
    global minRadius
    global maxRadius
    dp = float(a1)
    minDist = float(a2)
    param1 = float(a3)
    param2 = float(a4)
    minRadius = a5
    maxRadius = a6

def analyze():
    if filename == "":
        circle_detection.no_file()
        return
    plt.close()
    set_values(a_dp.get(),a_minDist.get(),a_param1.get(),a_param2.get(),a_minRadius.get(),a_maxRadius.get())
    circle_detection.find_circles(filename,dp,minDist,param1,param2,minRadius,maxRadius)

def select_file():
    global filename
    filetypes = (
        ('PNG files', '*.png'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title = 'Abrir imagen',
        initialdir = '/',
        filetypes = filetypes
    )
    if filename == "":
        circle_detection.no_file()
        return
    img = mpimg.imread(filename)
    plt.figure(num = "Imagen original", facecolor = "#0a0b11")
    plt.imshow(img)
    plt.show(block=False)

Label(
    root,
    justify = "center",
    bg = "#0a0b11",
    padx = 125,
    pady = 2
).grid(row=0,column=0)

Button(
    root,
    text = 'Abrir imagen',
    command = select_file,
    bg = "#0063cc",
    fg = "white",
    bd = 5,
    padx = 30,
    pady = 5
).grid(row=1,column=0)

Label(
    root,
    justify = "center",
    bg = "#0a0b11",
    padx = 125,
    pady = 2
).grid(row=2,column=0)

div = Label(
    root,
    bg = "#0a0b11",
)

div.grid(row=3,column=0)

Label(
    div,
    text = "Dp",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=0,column=0)

Spinbox(
    div,
    from_ = 1, to = 2,
    textvariable = a_dp,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=0,column=1)

Label(
    div,
    text = "minDist",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=1,column=0)

Spinbox(
    div,
    textvariable = a_minDist,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=1,column=1)

Label(
    div,
    text = "param1",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=2,column=0)

Spinbox(
    div,
    textvariable = a_param1,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=2,column=1)

Label(
    div,
    text = "param2",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=3,column=0)

Spinbox(
    div,
    textvariable = a_param2,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=3,column=1)

Label(
    div,
    text = "minRadius",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=4,column=0)

Spinbox(
    div,
    textvariable = a_minRadius,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=4,column=1)

Label(
    div,
    text = "maxRadius",
    bg = "#0a0b11", fg = "white",
    justify = "left"
).grid(row=5,column=0)

Spinbox(
    div,
    textvariable = a_maxRadius,
    bg = "white",fg = "black",bd = 0,
    width = 5,
    wrap = True,
    justify = "left"
).grid(row=5,column=1)

Label(
    root,
    justify = "center",
    bg = "#0a0b11",
    padx = 125,
    pady = 2
).grid(row=4,column=0)

Button(
    root,
    text = 'Analizar',
    command = analyze,
    bg = "#0063cc",
    fg = "white",
    bd = 5,
    padx = 30,
    pady = 5
).grid(row=5,column=0)

Label(
    root,
    justify = "center",
    bg = "#0a0b11",
    padx = 125,
    pady = 2
).grid(row=6,column=0)

root.mainloop()