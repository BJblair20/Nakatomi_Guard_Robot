
import threading
import os
import killme
import killJohnLenon
import time
#import lights


t1 = threading.Thread(target=killme.pp, name='t1')
t2 = threading.Thread(target=killJohnLenon.kk, name='t2')
 
t1.start()
t2.start()
 
#t1.join()
#t2.join()

print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
time.sleep(3)

killme.togglePP()
killJohnLenon.toggleJL()
