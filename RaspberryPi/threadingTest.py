import threading
import time

def loop1():
    global stop_flag
    while True:
        print("Loop 1 is running")
        time.sleep(3)
        # Set the stop flag after some condition
        
        print("Setting stop flag from Loop 1")
        stop_flag.set()

def loop2():
    global stop_flag
    while not stop_flag.is_set():
        print("Loop 2 is running")
        time.sleep(2)

stop_flag = threading.Event()
# Create two threads
thread1 = threading.Thread(target=loop1)
thread2 = threading.Thread(target=loop2)

# Start the threads
thread1.start()
thread2.start()