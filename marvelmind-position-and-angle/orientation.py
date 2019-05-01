from marvelmind import MarvelmindHedge
from time import sleep
import sys
import numpy as np
import math

def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y

	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = math.degrees(math.atan2(t0, t1))
	print("roll x:",X);
	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = math.degrees(math.asin(t2))
	print("pitch y:",Y);
	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = math.degrees(math.atan2(t3, t4))
	print("yawn z:",Z)
	print("\n")


def main():
    hedge = MarvelmindHedge(tty = "/dev/tty.usbmodem1421", adr=10, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    while True:
        try:
            sleep(1)
            matrix= hedge.valuesImuData

            i=0
            w=0
            x=0
            y=0
            z=0
			#get quaternion data and average it
            while(i < 3):

                w=matrix[i][3]+w
                x=matrix[i][4]+x
                y=matrix[i][5]+y
                z=matrix[i][6]+z
                i=i+1
            quaternion_to_euler_angle(w/3,x/3,y/3,z/3)
            rawdata=hedge.valuesImuRawData
            xGaussData=rawdata[0][6]#compass data around x axis
            yGaussData=rawdata[0][7]#compass data around y axis
			#convert compass data into degrees
            d=(math.atan2(yGaussData,xGaussData))* (180/math.pi)
            print("degree is:",d)
            print(hedge._bufferSerialDeque)
            print('Position of hedge sensors:')
            print (hedge.position()) # get last position and print

        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()
