import tkinter as tk
import numpy 
from tkinter import ttk
from tkinter.messagebox import showinfo
import time
import math
import tkinter.filedialog
import os
import socket
import json
root = tk.Tk()
from Audiotemp import findIndex
from threading import Timer
from spatializer_demo import play

myPerson = -1

#this creates the circles when the grid is touched 
#the 155 is because the grid numbers are flipped in the y axis
def callback(event):
	#print ("clicked at", event.x, event.y)
	sound = (event.x, 155-event.y)
	x = event.x
	y = event.y
	#print ("clicked at", sound)
	listOfSound.append(sound)
	c.create_circle(x, y, 7, fill="blue", outline="#DDD", width=1)


#this creates the second,third, etc sounds
def callback2(event):
	w2.configure(text="Click the position on the grid\nwhere you would like the\nsound to be placed") 

	#print ("clicked at", event.x, event.y)
	sound = (event.x, 155-event.y)
	listOfSound.append(sound)
	c.create_circle(event.x, event.y, 7, fill="blue", outline="#DDD", width=1)

#this creates the person and creates the popups for the angle prompts
def callback1(event):
	global myPerson
	global xCoord
	global yCoord
	if(myPerson != -1):
		c.delete(myPerson)

	x = event.x
	y = event.y
	xCoord = x
	yCoord = y
	#print ("clicked at", x, 155-y)
	angle = 0
	myPerson = c.create_triange(x, y, angle, fill="red")

	b2 = tk.Scale(f4,orient='horizontal', from_=0, to=360, variable = var)
	b2.grid(row=8, column=3)
	b2 = tk.Button(f4, text = "Submit Angle", bg = "skyblue1", command=rotate_person)
	b2.grid(row=9, columns = 4)

#these following allow the arrow keys to move the person
def movePersonleft(event):
	global xCoord
	global yCoord
	global myPerson
	try:
		if(myPerson == -1):
			print("Please add person")
	except:
		#print("nope")
		return
	else:
		c.delete(myPerson)

	c.pack()
	angle = var.get()
	x = xCoord - 5
	y = yCoord
	xCoord = x

	myPerson =  c.create_triange(x, y, angle, fill="red")


def movePersonright(event):
	global xCoord
	global yCoord
	global myPerson
	try:
		if(myPerson == -1):
			print("Please add person")
	except:
		#print("nope")
		return
	else:
		c.delete(myPerson)

	c.pack()
	angle = var.get()
	x = xCoord + 5
	y = yCoord
	xCoord = x

	myPerson =  c.create_triange(x, y, angle, fill="red")

def movePersonup(event):
	global xCoord
	global yCoord
	global myPerson
	try:
		if(myPerson == -1):
			print("Please add person")
	except:
		#print("nope")
		return
	else:
		c.delete(myPerson)

	c.pack()
	angle = var.get()
	x = xCoord 
	y = yCoord - 5
	yCoord = y

	myPerson =  c.create_triange(x, y, angle, fill="red")

def movePersondown(event):
	global xCoord
	global yCoord
	global myPerson
	try:
		if(myPerson == -1):
			print("Please add person")
	except:
		#print("nope")
		return
	else:
		c.delete(myPerson)

	c.pack()
	angle = var.get()
	x = xCoord
	y = yCoord +5
	yCoord = y

	myPerson =  c.create_triange(x, y, angle, fill="red")

#moves around the perimeter by cycling through grid assuming 155 by 155 in size
#change these numbers to change the grid size in use
#it also updates the global coordinates to allow the person to move
def playSoundPerimeter():
	w2.configure(text="The person is moving \naround the perimeter") 
	if(myPerson != -1):
		c.delete(myPerson)
	list2 = list(range(5, 150, 20))
	c.pack()
	angle = 0
	global xCoord
	global yCoord
#1
	y=5
	for x in list2:
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#time.sleep(1)
		c.delete(currSpot)
#2
	x=150
	for y in (list2):
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#time.sleep(1)
		c.delete(currSpot)
#3
	y=150
	for x in reversed(list2):
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#time.sleep(1)
		c.delete(currSpot)
#4
	x=5
	for y in reversed(list2):
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#time.sleep(1)
		c.delete(currSpot)


def playSoundSnake():
	w2.configure(text="The person is moving in a snake") 

	angle = 0
	if(myPerson != -1):
		c.delete(myPerson)
	c.pack()
	list2 = list(range(1, 155, 20))
	list3 = list(reversed(list2))
	listFinal = list2 + list3 + list2 + list3 + list2 + list3 + list2
	x=0
	global xCoord
	global yCoord
	last = 0
	for y in listFinal:
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#time.sleep(1)
		c.delete(currSpot)

		if y==141 and last != 141:
			x = x+ 20
		if y==1 and last != 1:
			x = x+20
		last = y

def playSoundDiagonal():
	w2.configure(text="The person is moving diagonally") 
	if(myPerson != -1):
		c.delete(myPerson)
	c.pack()
	list2 = list(range(5, 150, 20))
	angle = 0
	global xCoord
	global yCoord
#1
	y=5
	for x in list2:
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		
		xCoord = x
		
		yCoord= y
		temp = playSound()
		#print(temp)
		#time.sleep(1)
		c.delete(currSpot)
		y= y+20
#2
	y=150
	for x in reversed(list2):
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#print(temp)
		#time.sleep(1)
		c.delete(currSpot)
		y= y-20
#3
	x=150
	for y in list2:
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#print(temp)
		#time.sleep(1)
		c.delete(currSpot)
		x= x-20
#4
	x = 5
	for y in reversed(list2):
		currSpot = c.create_triange(x, y, angle, fill="red")
		c.update()
		xCoord = x
		yCoord= y
		temp = playSound()
		#print(temp)
		#time.sleep(1)
		c.delete(currSpot)
		x= x+20

#logistics to call the function to create circle
def popup_bonusSound():
	w2.configure(text="Click the position on the grid\nwhere you would like the\nsound to be placed.\nYou can place as many sounds\nas you wish.") 
	c.bind("<Button-1>", callback)
	c.pack()

#logistics to call the function to create circle
def popup_bonusSound1():
	c.bind("<Button-1>", callback2)
	w2.configure(text="Click the position on the grid\nwhere you would like the\nsound to be placed.\nYou can place as many sounds\nas you wish.") 

	c.pack()

#logistics to call the function to create person
def popup_bonusPerson():
	c.bind("<Button-1>", callback1)
	w2.configure(text="Click the position on the grid\nwhere you would like the\nperson to be placed.\nYou can then change the scale\nand click 'Submit Angle' to change the angle\nthe person is facing.\n\nYou can only place one person\n\nYou can use the arrow keys to\nmove the person.") 

	c.pack()

#creates the grid in the beginning 
def create_grid(event=None):
	 w = c.winfo_width() # Get current width of canvas
	 h = c.winfo_height() # Get current height of canvas
	 c.delete('grid_line') # Will only remove the grid_line

	 # Creates all vertical lines at intevals of 100
	 for i in range(0, w, 10):
		  c.create_line([(i, 0), (i, h)], tag='grid_line')

	 # Creates all horizontal lines at intevals of 100
	 for i in range(0, h, 10):
		  c.create_line([(0, i), (w, i)], tag='grid_line')


#what actually creates the circle (actually a round oval)
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

#what actually creates the triange. The angles are calculated for a fixed size triangle
def _create_triange(self, x, y, angle, **kwargs):
	if angle <= 180:
		angle = angle + 180
	else:
		angle = angle - 180

	r = - angle * math.pi
	r = r/180

	sin = math.sin(r) 
	cos = math.cos(r)
	x2 = ((+4) * cos) + ((-12) * sin) + x
	y2 = (-(+4) * sin) + ((-12) * cos) + y
	x3 = ((-4) * cos) + ((-12) * sin) + x
	y3 = (-(-4) * sin) + ((-12) * cos) + y


	return self.create_polygon(x, y, x2, y2, x3, y3, **kwargs)

tk.Canvas.create_triange = _create_triange


#rotates the person by rotating the points calculated in previous function
def rotate_person():
	global xCoord
	global yCoord
	global myPerson
	try:
		if(myPerson == -1):
			print("Please add person")
	except:
		#print("nope")
		return
	else:
		c.delete(myPerson)

	c.pack()
	angle = var.get()
	x = xCoord
	y = yCoord
	myPerson =  c.create_triange(x, y, angle, fill="red")

#opens the connection with the marvel mind code that is executed at the same time
#change the port number as necessary
def fromLocation():
	s = socket.socket()
	port = 12347
	s.bind(('', port))
	s.listen(5)
	conn, addr = s.accept()
	print ("Socket Up and running with a connection from",addr)
	while True:
		rcvdData = conn.recv(1024).decode()
		rcvdData = json.loads(rcvdData)

		if(rcvdData == "Bye" or rcvdData == "bye"):
			break
		elif rcvdData != "":
			#print (rcvdData)
			#rcvdData.strip('\n')
			#print(rcvdData)
			global xCoord
			global yCoord
			global angle
			xCoord = rcvdData[0]
			yCoord = rcvdData[1]
			angle = rcvdData[2]

			global myPerson
			try:
				if(myPerson != -1):
					c.delete(myPerson)
			except:
				#print("nope")
				return

			myPerson =  c.create_triange(int(xCoord), int(yCoord), int(angle), fill="red")
			c.update()
			playSound()

	print("Socket is closed")
	conn.close()


#formats the list of sounds and person
#sends it to the findIndex function in Audiotemp.py which gives index
#the play function from spatializer_demo is then called for 3 seconds before exiting

def playSound():
	global xCoord
	global yCoord
	#print(listOfSound)
	posOfPerson = (xCoord, 155-yCoord, var.get())
	#print(posOfPerson)
	#print("__________")
	index = findIndex(listOfSound, posOfPerson)
	#print("index is", index)
	#play(index)

	Timer(3, play, [index]).start()
	time.sleep(3)
	return "good"


btn_dict = {}
permcol = 0 
col = 0
row = 0
words = [[(k, j) for k in range(1, 16)] for j in range(1, 16)] 
listOfSound = []

#creates the GUI visually with buttons, etc

f = tk.Frame(root, bg = "skyblue1", width = 500, height = 500)
f.pack(side='left')

f2 = tk.Frame(root, bg = "skyblue1", height=100, width = 100)
f2.pack(side='left', fill = 'y')

f5 = tk.Frame(root, bg = "skyblue1", height=100, width = 200)
f5.pack(side='left', fill = 'y')
w = tk.Label(f5, text="Instructions: ", bg="skyblue1")
w.grid(row=1, column=3)
w2 = tk.Label(f5, text="Welcome! \n\nPlease begin by placing a sound!\n\nYou can then place a person or \nselect one of the preset paths.", bg="skyblue1")
w2.grid(row=2, column=3)

f3 = tk.Frame(f, bg = "skyblue1", width = 500)
f3.pack(side='left', pady = 50, padx = 50)

f4 = tk.Frame(f2, bg = "skyblue1", width = 100)
f4.pack(side='left', pady = 20, padx = 20)

c = tk.Canvas(f3, height=150, width=150, bg='white')
c.pack(fill=tk.BOTH, expand=True, pady = 20)
b2 = tk.Button(f3, text = "Play", bg = "skyblue1", command=playSound)
b2.pack(fill=tk.BOTH, expand=True)
b2 = tk.Button(f3, text = "Exit", bg = "skyblue1", command=root.destroy)
b2.pack(fill=tk.BOTH, expand=True)


c.bind('<Configure>', create_grid)
var = tk.IntVar()

frame = tk.Frame(root, width=155, height=155)
root.bind('<Left>', movePersonleft)
root.bind('<Right>', movePersonright)
root.bind('<Up>', movePersonup)
root.bind('<Down>', movePersondown)



b = tk.Button(f4, text = "Place Default Sound", bg = "skyblue1", command=popup_bonusSound)
b.grid(row=1, column=3)
b2 = tk.Button(f4, text = "Move Around Perimeter", command = playSoundPerimeter, bg = "skyblue1")
b2.grid(row=3, column=3)
b2 = tk.Button(f4, text = "Move in Snake Pattern", command = playSoundSnake, bg = "skyblue1")
b2.grid(row=4, column=3)
b2 = tk.Button(f4, text = "Move Across Diagonals", command = playSoundDiagonal, bg = "skyblue1")
b2.grid(row=5, column=3)

b2 = tk.Button(f4, text = "Use MarvelMind", bg = "skyblue1", command=fromLocation)
b2.grid(row=6, column=3)

b2 = tk.Button(f4, text = "Place Person", bg = "skyblue1", command=popup_bonusPerson)
b2.grid(row=7, column=3)



root.mainloop()


