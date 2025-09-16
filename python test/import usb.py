import usb.core
import usb.util
import time

# Function to check for new USB devices
def check_for_new_devices():
    devices = usb.core.find(find_all=True)
    for device in devices:
        print(f"Device: {device.idVendor}:{device.idProduct}")

# Continuously check for new devices
while True:
    check_for_new_devices()
    time.sleep(5)