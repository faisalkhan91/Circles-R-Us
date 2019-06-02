#!/usr/local/bin/python3

import tkinter

def changecirclesize(radius) :

	bbox = drawarea.coords(circleid)
	centerx = (bbox[0] + bbox[2]) / 2
	centery = (bbox[1] + bbox[3]) / 2
	ulx = centerx - radiusvar.get()
	uly = centery - radiusvar.get()
	lrx = centerx + radiusvar.get()
	lry = centery + radiusvar.get()
	drawarea.coords(circleid, (ulx, uly, lrx, lry))

def hitleftmousebutton(ev) :

	newcenterx = ev.x
	newcentery = ev.y
	ulx = newcenterx - radiusvar.get()
	uly = newcentery - radiusvar.get()
	lrx = newcenterx + radiusvar.get()
	lry = newcentery + radiusvar.get()
	drawarea.coords(circleid, (ulx, uly, lrx, lry))

def changeoutlinecolor(color) :

	drawarea.itemconfig(circleid, outline = color)


root = tkinter.Tk()
root.title("Circle's R' Us")
root.lift()
root.minsize(600, 600)
root.configure(bg = "blue")

drawarea = tkinter.Canvas(root, height = 400, width = 400, bg = "light blue")
drawarea.grid(row = 0, column = 0)

circleid = drawarea.create_oval(100, 100, 200, 200, outline = "orange", fill = "")

radiusvar = tkinter.IntVar()
radiusbar = tkinter.Scale(root, from_ = 10, to = 100, resolution = 5, orient = tkinter.HORIZONTAL, variable = radiusvar, command = changecirclesize)
radiusbar.grid(row = 1, column = 0, sticky = "news")

drawarea.bind("<Button-1>", hitleftmousebutton)

ocolorvar = tkinter.StringVar()
ocolorvar.set("black")
colors = ["black", "blue", "red", "green", "purple", "orange", "yellow", "brown", "pink", "white" ]

outlinecolor = tkinter.OptionMenu(root, ocolorvar, *colors, command = changeoutlinecolor)
outlinecolor.grid(row = 2, column = 0, sticky = "news")
 
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.columnconfigure(0, weight = 1)

root.mainloop()

