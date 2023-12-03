
import threading
import os
import killme
import killJohnLenon
import time
import lights
#import lights
import lidar_reader
import distanceReader
import motor

def run():
    while True:
        motor.runMotor()
        distanceReader.main()
        motor.turn()



#t1 = threading.Thread(target=lights.soundCue, name='t1')
#t2 = threading.Thread(target=lights.lightsCue, name='t2')
 
#t2.start()
#t1.start()
 
#t1.join()
#t2.join()

run()

#print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
#time.sleep(9)

#killme.togglePP()
#killJohnLenon.toggleJL()
