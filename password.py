import Tkinter as tk
from Tkinter import *
import random
import time

#the function to create the assigned password
def random_colour():
	colours = ["red", "blue", "green", "pink", "yellow", "black", "white"]
	hair = random.choice(colours)
	face = random.choice(colours)
	nose = random.choice(colours)
	leftc = random.choice(colours)
	rightc = random.choice(colours)
	mouth = random.choice(colours)
	lefteye = random.choice(colours)
	righteye = random.choice(colours)
	lefteyebow = random.choice(colours)
	righteyebow = random.choice(colours)
	hat = random.choice(colours)
	conhat = random.choice(colours)
	return hair, face, nose, leftc, rightc, mouth, lefteye, righteye, lefteyebow, righteyebow, hat, conhat

#the function to create the GUI of the dropbox(password enter space), and return the selected value from the dropbox
def dropbox(frame):
	#get the value from each drop box and stored into an array
	def command(*args):
		list[0] = var_1.get()
	def command2(*args):
		list[1] = var_2.get()
	def command3(*args):
		list[2] = var_3.get()
	def command4(*args):
		list[3] = var_4.get()
	def command5(*args):
		list[4] = var_5.get()
	def command6(*args):
		list[5] = var_6.get()
	def command7(*args):
		list[6] = var_7.get()
	def command8(*args):
		list[7] = var_8.get()
	def command9(*args):
		list[8] = var_9.get()
	def command10(*args):
		list[9] = var_10.get()
	def command11(*args):
		list[10] = var_11.get()
	def command12(*args):
		list[11] = var_12.get()
		
	color = ["red", "blue", "green", "pink", "yellow", "black", "white"]
	var_1 = StringVar(frame)
	data_1 = OptionMenu(frame, var_1, *color)
	data_1.place(x=10, y=20, anchor="nw")
	Label(frame, text="<-hair", font=("Times", "12")).place(x=100,y=20,anchor="nw")
	
	var_2 = StringVar(frame)
	data_2 = OptionMenu(frame, var_2, *color)
	data_2.place(x=10, y=50, anchor="nw")
	Label(frame, text="<-face", font=("Times", "12")).place(x=100,y=50,anchor="nw")
		
	var_3 = StringVar(frame)
	data_3 = OptionMenu(frame, var_3, *color)
	data_3.place(x=10, y=80, anchor="nw")
	Label(frame, text="<-nose", font=("Times", "12")).place(x=100,y=80,anchor="nw")
		
	var_4 = StringVar(frame)
	data_4 = OptionMenu(frame, var_4, *color)
	data_4.place(x=10, y=110, anchor="nw")
	Label(frame, text="<-left cheek", font=("Times", "12")).place(x=100,y=110,anchor="nw")
		
	var_5 = StringVar(frame)
	data_5 = OptionMenu(frame, var_5, *color)
	data_5.place(x=10, y=140, anchor="nw")
	Label(frame, text="<-right cheek", font=("Times", "12")).place(x=100,y=140,anchor="nw")
	
	var_6 = StringVar(frame)
	data_6 = OptionMenu(frame, var_6, *color)
	data_6.place(x=10, y=170, anchor="nw")
	Label(frame, text="<-mouth", font=("Times", "12")).place(x=100,y=170,anchor="nw")
		
	var_7 = StringVar(frame)
	data_7 = OptionMenu(frame, var_7, *color)
	data_7.place(x=10, y=200, anchor="nw")
	Label(frame, text="<-left eye", font=("Times", "12")).place(x=100,y=200,anchor="nw")
		
	var_8 = StringVar(frame)
	data_8 = OptionMenu(frame, var_8, *color)
	data_8.place(x=10, y=230, anchor="nw")
	Label(frame, text="<-right eye", font=("Times", "12")).place(x=100,y=230,anchor="nw")
		
	var_9 = StringVar(frame)
	data_9 = OptionMenu(frame, var_9, *color)
	data_9.place(x=10, y=260, anchor="nw")
	Label(frame, text="<-left eyebrow", font=("Times", "12")).place(x=100,y=260,anchor="nw")
		
	var_10 = StringVar(frame)
	data_10 = OptionMenu(frame, var_10, *color)
	data_10.place(x=10, y=290, anchor="nw")
	Label(frame, text="<-right eyebrow", font=("Times", "12")).place(x=100,y=290,anchor="nw")
		
	var_11 = StringVar(frame)
	data_11 = OptionMenu(frame, var_11, *color)
	data_11.place(x=160, y=20, anchor="nw")
	Label(frame, text="<-hat", font=("Times", "12")).place(x=250,y=20,anchor="nw")
		
	var_12 = StringVar(frame)
	data_12 = OptionMenu(frame, var_12, *color)
	data_12.place(x=160, y=50, anchor="nw")
	Label(frame, text="<-circle on hat", font=("Times", "12")).place(x=250,y=50,anchor="nw")
	
	list = ['', '', '', '', '', '', '', '', '', '', '', '']
	var_1.trace("w", command)
	var_2.trace("w", command2)
	var_3.trace("w", command3)
	var_4.trace("w", command4)
	var_5.trace("w", command5)
	var_6.trace("w", command6)
	var_7.trace("w", command7)
	var_8.trace("w", command8)
	var_9.trace("w", command9)
	var_10.trace("w", command10)
	var_11.trace("w", command11)
	var_12.trace("w", command12)
	return list

#function the create the clown face in GUI
def clown_face(frame, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh):
	canvas = Canvas(frame)
	global c_hair, c_face, c_nose, c_left_circle, c_right_circle, c_mouth, c_left_eyeball, c_right_eyeball, c_left_eyebrow, c_right_eyebrow, c_hat, c_circle_on_hat
	#the clown face
	#1
	c_hair = canvas.create_polygon((60, 60, 80, 150, 220, 150, 240, 60, 180, 80, 120, 80), fill=h, outline="black")
	#2
	c_face = canvas.create_oval(80, 80, 220, 220, fill=f)
	#3
	c_nose = canvas.create_oval(140, 140, 160, 160, fill=n)
	#4
	c_left_circle = canvas.create_oval(90, 140, 120, 150, fill=lc)
	#5
	c_right_circle = canvas.create_oval(180, 140, 210, 150, fill=rc)
	#6
	c_mouth = canvas.create_oval(110, 170, 190, 200, fill=m)
	c_line = canvas.create_line(130, 185, 170, 185)
	c_left_eye = canvas.create_oval(120, 110, 140, 130, fill="white")
	c_right_eye = canvas.create_oval(160, 110, 180, 130, fill="white")
	#7
	c_left_eyeball = canvas.create_oval(125, 115, 135, 125, fill=le)
	#8
	c_right_eyeball = canvas.create_oval(165, 115, 175, 125, fill=re)
	#9 
	c_left_eyebrow = canvas.create_polygon((120, 105, 130, 90, 140, 105), fill=lew, outline="black")
	#10
	c_right_eyebrow = canvas.create_polygon((160, 105, 170, 90, 180, 105), fill=rew, outline="black")
	#11
	c_hat = canvas.create_polygon((120, 80, 150, 30, 180, 80), fill=ha, outline="black")
	#12
	c_circle_on_hat = canvas.create_oval(145, 60, 155, 70, fill=coh)
	return canvas

#function to change the colour of the clown face in the GUI
def change_color(canvas, h, f, n, lc, rc, m, le, re, lew, rew, ha, coh):
	new = canvas
	new.itemconfig(c_hair, fill=h)
	new.itemconfig(c_face, fill=f)
	new.itemconfig(c_nose, fill=n)
	new.itemconfig(c_left_circle, fill=lc)
	new.itemconfig(c_right_circle, fill=rc)
	new.itemconfig(c_mouth, fill=m)
	new.itemconfig(c_left_eyeball, fill=le)
	new.itemconfig(c_right_eyeball, fill=re)
	new.itemconfig(c_left_eyebrow, fill=lew)
	new.itemconfig(c_right_eyebrow, fill=rew)
	new.itemconfig(c_hat, fill=ha)
	new.itemconfig(c_circle_on_hat, fill=coh)