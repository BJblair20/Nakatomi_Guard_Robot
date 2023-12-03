import smbus
import time

# I2C address of the Lidar-Lite sensor
LIDAR_LITE_ADDRESS = 0x62

# Register addresses
LIDAR_LITE_DIST_WRITE = 0x00
LIDAR_LITE_DIST_READ = 0x8f

def read_lidar_lite_distance(bus):
    # Write to register to initiate distance measurement
    bus.write_byte_data(LIDAR_LITE_ADDRESS, LIDAR_LITE_DIST_WRITE, 0x04)

    # Wait for measurement to complete (adjust this based on your sensor's documentation)
    time.sleep(0.04)

    # Read distance value
    distance = bus.read_word_data(LIDAR_LITE_ADDRESS, LIDAR_LITE_DIST_READ)

    # Convert distance from centimeters to meters
    distance /= 100.0

    return distance

def main():
    # Open I2C bus
    bus = smbus.SMBus(1)  # You may need to change the bus number based on your hardware

    try:
        while True:
            distance = read_lidar_lite_distance(bus)
            print(f"Distance: {distance:.2f} meters")
            time.sleep(1)

    except KeyboardInterrupt:
        # Close the I2C bus when the program is interrupted
        bus.close()

if __name__ == "__main__":
    main()