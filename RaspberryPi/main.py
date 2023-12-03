
import threading
import os
import killme
import killJohnLenon
import time
import lights
#import lights


t1 = threading.Thread(target=lights.soundCue, name='t1')
t2 = threading.Thread(target=lights.lightsCue, name='t2')
 
t1.start()
t2.start()
 
#t1.join()
#t2.join()

print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
time.sleep(9)

killme.togglePP()
killJohnLenon.toggleJL()
