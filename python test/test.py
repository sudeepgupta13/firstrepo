import pyudev
import requests
import json
import socket
from datetime import datetime

# Replace with the central server's IP and port
SERVER_URL = "http://192.168.1.100:5000/monitor"  # <-- UPDATE THIS

hostname = socket.gethostname()

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    print("Monitoring USB events...")

    for device in monitor:
        if device.action == 'add':
            event = "USB Connected"
        elif device.action == 'remove':
            event = "USB Disconnected"
        else:
            continue

        data = {
            "hostname": hostname,
            "event": event,
            "device": device.sys_name,
            "time": datetime.now().isoformat()
        }

        try:
            response = requests.post(SERVER_URL, json=data)
            print(f"Sent event to server: {data}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data: {e}")

if __name__ == "__main__":
    monitor_usb()
