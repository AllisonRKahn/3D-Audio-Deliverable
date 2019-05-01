import numpy as np
import matplotlib.pyplot as plt

#calculates the angle between two points (x,y)
def angle_between(p1, p2):
	diffX = p1[0] - p2[0]
	diffY = p1[1] - p2[1]
	if diffX == 0 and diffY < 0:
		return 0
	elif diffX == 0 and diffY > 0:
		return 180
	elif diffY == 0 and diffX > 0:
		return 90
	elif diffY == 0 and diffX < 0:
		return 270
	
	
	if diffX>0 and diffY>0:
		fract = (diffX/diffY)
		arctan = (np.arctan(fract))
		return np.rad2deg(arctan)
	elif diffX >0 and diffY<0:
		fract = (diffX/(diffY*-1))
		arctan = (np.arctan(fract))
		temp = np.rad2deg(arctan)
		return ((90-temp)+90)
	elif diffX < 0 and diffY < 0:
		fract = ((diffX*-1)/(diffY*-1))
		arctan = (np.arctan(fract))
		temp = np.rad2deg(arctan)
		return (temp+180)
	elif diffX < 0 and diffY > 0:
		fract = ((diffX*-1)/(diffY))
		arctan = (np.arctan(fract))
		temp = np.rad2deg(arctan)
		return ((90-temp)+270)
	
def distance_between(p1, p2):  
	diffX = p1[0] - p2[0]
	diffY = p1[1] - p2[1]
	dist = np.sqrt((diffX**2) + (diffY**2))
	return dist

#adds the angle of the user to find the new angle

def findUserPoint(angleOfUser):
	xAdd = 0
	yAdd = 0

	if 0 <= angleOfUser <=90:
		xAdd = -np.sin(np.deg2rad(angleOfUser))
		yAdd = np.cos(np.deg2rad(angleOfUser))
	elif (90 < angleOfUser <= 180):
		xAdd = -np.sin(np.deg2rad(angleOfUser))
		yAdd = np.cos(np.deg2rad(angleOfUser))
	elif 180 < angleOfUser <= 270:
		xAdd = -np.sin(np.deg2rad(angleOfUser))
		yAdd = np.cos(np.deg2rad(angleOfUser))
	elif 270 < angleOfUser <= 360:
		xAdd = -np.sin(np.deg2rad(angleOfUser))
		yAdd = np.cos(np.deg2rad(angleOfUser))

	yAdd = yAdd*.5
	xAdd = xAdd*.5

	#print("yAdd is", str(yAdd))
	#print("xAdd is", str(xAdd))
	return (xAdd, yAdd)

#converts the angle to the index to give to audio file
def angleToIndex(angleBtwn):
	index = 0
	if 0<= angleBtwn < 15:
		index = 13
	elif 15<= angleBtwn < 30:
		index = 14
	elif 30<= angleBtwn < 45:
		index = 15
	elif 45<= angleBtwn < 60:
		index = 16
	elif 60<= angleBtwn < 75:
		index = 17
	elif 75<= angleBtwn < 90:
		index = 18
	elif 90<= angleBtwn < 105:
		index = 19
	elif 105<= angleBtwn < 120:
		index = 20
	elif 120<= angleBtwn < 135:
		index = 21
	elif 135<= angleBtwn < 150:
		index = 22
	elif 150<= angleBtwn < 165:
		index = 23
	elif 165<= angleBtwn < 180:
		index = 24

	elif 180<= angleBtwn < 195:
		index = 1
	elif 195<= angleBtwn < 210:
		index = 2
	elif 210<= angleBtwn < 225:
		index = 3
	elif 225<= angleBtwn < 240:
		index = 4
	elif 240<= angleBtwn < 255:
		index = 5
	elif 255<= angleBtwn < 270:
		index = 6
	elif 270<= angleBtwn < 285:
		index = 7
	elif 285<= angleBtwn < 300:
		index = 8
	elif 300<= angleBtwn < 315:
		index = 9
	elif 315<= angleBtwn < 330:
		index = 10
	elif 330<= angleBtwn < 345:
		index = 11
	elif 345<= angleBtwn < 360:
		index = 12
	

	return index

#formats and executes the above functions
def findIndex(listOfSounds, posOfPerson):

	xcoordUser = posOfPerson[0]
	ycoordUser = posOfPerson[1]
	coordUser = (int(xcoordUser), int(ycoordUser))

	#print(listOfSounds)

	soundsWithDistances = {}

	for x in listOfSounds:
		dist = distance_between(x, coordUser)
		soundsWithDistances.update({x:dist})

	closestCoord = min(soundsWithDistances, key=soundsWithDistances.get)
	#print(closestCoord)


	angleBtwn = angle_between(closestCoord, coordUser )
	#distBtwn = distance_between(coordSound, coordUser)
	#print("angle between: ", angleBtwn)
	#print("distance between: ", distBtwn)
	angleOfUser = posOfPerson[2]
	if angleOfUser <=180:
	    angleOfUser = angleOfUser + 180
	else:
	    angleOfUser = angleOfUser - 180

	#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

	#user is green facing blue

	#print(angleBtwn)
	#print(angleOfUser)
	#print("User is: ", str(coordUser))
	#print("Sound is: ", str(closestCoord))

	if coordUser[0] < closestCoord[0] and coordUser[1] < closestCoord[1]:
		#print("!")
		#print("angleOfUser", angleOfUser)
		#print("angleBtwn", angleBtwn)
		if 0< angleOfUser < (360-angleBtwn):
			trueAngle = 360 - angleOfUser - angleBtwn
		else:
			trueAngle = (360-angleBtwn) + (360-angleOfUser)
	elif coordUser[0] < closestCoord[0] and coordUser[1] > closestCoord[1]:
		#print("!!")
		if 0< angleOfUser < (360-angleBtwn):
			trueAngle = 360 - angleBtwn - angleOfUser
		else:
			trueAngle = (360-angleBtwn) + (360-angleOfUser)
	elif coordUser[0] > closestCoord[0] and coordUser[1] < closestCoord[1]:
		#print("!!!")
		if 0 < angleOfUser < (360-angleBtwn):
			trueAngle = 360 - angleOfUser - angleBtwn
		else:
			trueAngle = (360-angleBtwn) + (360-angleOfUser)
	else:
		#print("!!!!")
		if 0 < angleOfUser < (360-angleBtwn):
			trueAngle = 360 - angleOfUser - angleBtwn
		else:
			trueAngle = (360-angleOfUser) + (360- angleBtwn)
		

	index = angleToIndex(trueAngle)
	#print("INDEX IS", index)
	return index
	
	



# listOfSounds = [[12, 32], [101, 28]]
# posOfPerson = (62, 89, 0)
# findIndex(listOfSounds, posOfPerson)







