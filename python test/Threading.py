import threading
import time
import random

# Simulate picking up objects
def pick_objects():
    for i in range(5):
        print(f"[Pick Thread] Picking object {i + 1}")
        time.sleep(random.uniform(0.5, 1.5))

# Simulate sorting objects
def sort_objects():
    for i in range(5):
        print(f"[Sort Thread] Sorting object {i + 1}")
        time.sleep(random.uniform(0.5, 1.5))

# Simulate logging operations
def log_operations():
    for i in range(5):
        print(f"[Log Thread] Logging operation {i + 1}")
        time.sleep(random.uniform(0.3, 1.0))

# Create threads for each robotic task
pick_thread = threading.Thread(target=pick_objects)
sort_thread = threading.Thread(target=sort_objects)
log_thread = threading.Thread(target=log_operations)

# Start all threads
pick_thread.start()
sort_thread.start()
log_thread.start()

# Wait for all threads to complete
pick_thread.join()
sort_thread.join()
log_thread.join()

print("\n✅ Robotic tasks completed.")
