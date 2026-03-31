#!/usr/bin/env python3
print("Bhopping Script! 🦘 [FOR ROBLOX EVADE]")

# Packages
from evdev import InputDevice, ecodes
import uinput, time, threading, select


# Read and send devices
mouse = InputDevice("/dev/input/event5") # Change this to your mouse event
keyboard = InputDevice("/dev/input/event13") # Change this to your keyboard event
all_keys = [getattr(uinput, k) for k in dir(uinput) if k.startswith("KEY_")] # Sorry, but ChatGPT made this
device = uinput.Device(all_keys)

# Flag
auto_jump_flag = False


# Functions
# Press key
def press_key(key: str, seconds: float = 0.02):
    device.emit(getattr(uinput, key), 1)
    # print(f"Held {key}")
    time.sleep(seconds)
    device.emit(getattr(uinput, key), 0)
    # print(f"Release {key}")
    # print(f"Pressed {key}")

# Worker threads
def auto_jump():
    while auto_jump_flag:
        press_key("KEY_SPACE")
        print("Jumped!")
        time.sleep(0.01)


# Input loop
devices = [mouse, keyboard]

while True:
    r, _, _ = select.select(devices, [], [])

    for d in r:
        for e in d.read():
             # Scroll down: Jump
            if e.type == ecodes.EV_REL and e.code == ecodes.REL_WHEEL:
                if e.value == -1:
                    print("Jumped!")
                    press_key("KEY_SPACE")

            # Side mouse button: Auto-jump
            if e.type == ecodes.EV_KEY and e.code == ecodes.BTN_EXTRA:
                if e.value == 1:  # press
                    print("Auto-jump ENABLED! 🔥")
                    if not auto_jump_flag:
                        auto_jump_flag = True
                        threading.Thread(target=auto_jump, daemon=True).start()
                elif e.value == 0:  # release
                     print("Auto-jump DISABLED! 💨")
                     auto_jump_flag = False

            # ` key: Change POV
            if e.type == ecodes.EV_REL and e.code == ecodes.KEY_GRAVE:
                if e.value == 1:
                    print("Changed POV")
                    press_key("KEY_O")