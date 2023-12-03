import time
from adafruit_motorkit import MotorKit
import random
kit = MotorKit()
def runMotor():
    kit.motor1.throttle = 1
    kit.motor2.throttle = -1
    time.sleep(15)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    exit()


def turn():
    flip = random.randint(0, 1)
    if flip == 0:
        kit.motor1.throttle = 0.5
        kit.motor2.throttle = -0.5
        time.sleep(1)
    else:
        kit.motor1.throttle = -0.5
        kit.motor2.throttle = 0.5
        time.sleep(1)