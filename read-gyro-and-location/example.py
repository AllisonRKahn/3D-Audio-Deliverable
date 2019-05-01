from marvelmind import MarvelmindHedge
from time import sleep
import sys
import numpy as np
import math
# first of all import the socket library
import socket

def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y

	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = math.degrees(math.atan2(t0, t1))
	#print("roll x:",X);
	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = math.degrees(math.asin(t2))
	#print("pitch y:",Y);
	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = math.degrees(math.atan2(t3, t4))
	print("yawn z:",Z)
	print("\n")


def main():

    hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=10, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    # next create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
	# reserve a port on your computer in our
	# case it is 12345 but it can be anything
    port = 12345
	# Next bind to the port
	# we have not typed any ip in the ip field
	# instead we have inputted an empty string
	# this makes the server listen to requests
	# coming from other computers on the network
    s.bind(('', port))
	# put the socket into listening mode
    s.listen(5)

    print ("socket is listening")
    c, addr = s.accept()
    while True:
        try:
            sleep(1)

            matrix= hedge.valuesImuData
            rawdata=hedge.valuesImuRawData
            position=hedge.position()
#            quaternion_to_euler_angle(matrix[0][3],matrix[0][4],matrix[0][5],matrix[0][6])
            i=0
            w=0
            x=0
            y=0
            z=0
            xGaussData=0
            yGaussData=0
            while(i < 3):
                w=matrix[i][3]+w
                x=matrix[i][4]+x
                y=matrix[i][5]+y
                z=matrix[i][6]+z
                xGaussData=rawdata[i][6]+xGaussData
                yGaussData=rawdata[0][7]+yGaussData
                i=i+1
            yGaussData=yGaussData/3
            xGaussData=xGaussData/3
            d=(math.atan2(yGaussData,xGaussData))* (180/math.pi)
            data=str(position[1])+","+str(position[2])+","+str(d)
            print("d is:",d)
            quaternion_to_euler_angle(w/3,x/3,y/3,z/3)

            print ('Got connection from', addr)
            c.send(data.encode('utf-16'))
            while(c.recv(2048).decode('utf-16')!="ack"):
               print("waiting for ack")
            print ("ack received!")
            #c.close()
#            print('Position Raw:')
#            print (hedge.position()) # get last position and print
#            print('Position:')
#            hedge.print_position()

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
            c.close()
    c.close()
main()
