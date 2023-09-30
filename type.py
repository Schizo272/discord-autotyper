import time
import pyautogui

def main():
    try:
        while True:
            # Pause for x seconds
            time.sleep(1.5)
            pyautogui.typewrite("BigBalls420")
            pyautogui.press("enter")
    
    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    main()
