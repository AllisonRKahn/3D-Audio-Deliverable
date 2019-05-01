from marvelmind import MarvelmindHedge
from time import sleep
import sys
import json
import socket

def main():
    hedge = MarvelmindHedge(tty = "/dev/tty.usbmodem1421", adr=None, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    s = socket.socket()
    s.connect(('127.0.0.1', 12347))
    i=0

    while True:
        try:
            #i = i+1
            sleep(2)
            # print (hedge.position()) # get last position and print
            # --------------------------
            # my additions to Marvelmind's code

            # list contains the X,Y,Z coordinates from the hedgehog
            list = hedge.send_position()
            print(str(list))

            temp = list[1:3]
            temp.append(list[4])
            final = []
            for x in temp:
                if x < 0:
                    x = x * -1
        #the multiplier is the proportion of the room
        #take highest value of x,y and divide 150 by it
        #so x*150 / highestValueOfRoom
                x = x*30
                final.append(x)
            print(final)
            toSend = json.dumps(final)
            s.send(toSend.encode())
            print("i is", i)
            #if i == 0:
            #    toSend = json.dumps("Bye")
            #    s.send(toSend.encode())
            #    s.close()
            #    hedge.stop()
            #    sys.exit()

            #print(str(list[1:5])[1:-1])
            # --------------------------
            if (hedge.distancesUpdated):
                hedge.print_distances()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()
