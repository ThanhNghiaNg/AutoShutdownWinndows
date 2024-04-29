import pyautogui
import time
import os
import ctypes
import sys
import time

# Function to check if the mouse has moved
def has_mouse_moved(last_pos):
    current_pos = pyautogui.position()
    if current_pos != last_pos:
        return True
    return False

# Function to sleep the computer
def sleep_computer():
    # On Windows
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # Lock windows
    # user32 = ctypes.WinDLL('user32')
    # user32.LockWorkStation()

    # On macOS
    # os.system("pmset sleepnow")

def main():
    # Set the initial position of the mouse
    last_mouse_pos = pyautogui.position()

    # Define the time in seconds after which the computer should sleep
    # Get defaultSleepTime from command-line arguments or use default value
    if len(sys.argv) > 1:
        defaultSleepTime = int(sys.argv[1])
    else:
        defaultSleepTime = 30 * 60  # Default sleep time: 30 minutes

    sleep_time = defaultSleepTime  

    while True:
        print(sleep_time)
        if has_mouse_moved(last_mouse_pos):
            last_mouse_pos = pyautogui.position()
            sleep_time = defaultSleepTime
        else:
            time.sleep(1)  # Introducing a delay of 0.5 seconds
            sleep_time -= 1  # Subtracting 0.5 seconds from sleep_time
            if sleep_time <= 0:
                sleep_computer()
                break

if __name__ == "__main__":
    main()
