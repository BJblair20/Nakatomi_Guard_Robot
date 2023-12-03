import time
from adafruit_motorkit import MotorKit

def runMotor():
    kit = MotorKit()
    kit.motor1.throttle = 1
    kit.motor2.throttle = -1
    time.sleep(15)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    exit()
