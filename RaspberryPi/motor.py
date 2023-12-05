import time
from adafruit_motorkit import MotorKit
import random
kit = MotorKit()
def runMotor():
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.5

def stopMotor():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    exit()


def turn():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    time.sleep(1)
    flip = random.randint(0, 1)

    if flip == 0:
        kit.motor1.throttle = 0.8
        kit.motor2.throttle = 0.8
        time.sleep(0.025)
    else:
        kit.motor1.throttle = -0.8
        kit.motor2.throttle = -0.8
        time.sleep(0.025)

if __name__ == "__main__":
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0