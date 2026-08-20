import keyboard
import pydirectinput
import time
import pygetwindow as gw
import sys
import ctypes

# Force Admin Rights (Required for game key injections)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# --- CONFIGURATION ---
activated = False
game_window = None
pydirectinput.PAUSE = 0.0
# ---------------------

print("=======================================================")
print("     ACTIVE FOCUS WINDOW BINDING (Admin Mode)")
print("=======================================================")
print("1. Click INSIDE your Idle Slayer game window.")
print("2. With the game focused, press: Ctrl + Shift + D")
print("   (This will automatically bind the target window)")
print(" -> Exit script: ESC")
print(" If you like this script, consider supporting the developer: https://buymeacoffee.com/drowfear or https://ko-fi.com/drowfear")
print("=======================================================")

while True:
    # Toggle shortcut
    if keyboard.is_pressed('ctrl+shift+d'):
        activated = not activated
        
        # Save window handle on first activation
        if activated and game_window is None:
            game_window = gw.getActiveWindow()
            if game_window:
                print(f"\n[+] GAME DETECTED AND BOUND: '{game_window.title}'")
            else:
                print("\n[!] Could not detect active window. Please try again.")
                activated = False
        
        print(f"-> Macro {'ACTIVATED' if activated else 'DEACTIVATED'}")
        time.sleep(0.5) # Prevent key bounce
        
    if activated and game_window:
        active_window = gw.getActiveWindow()
        
        # Verify current window matches saved window
        if active_window == game_window:
            # Press D (Dash)
            pydirectinput.keyDown('d')
            time.sleep(0.02)
            pydirectinput.keyUp('d')
            
            # Press Space (Jump - 140ms duration)
            pydirectinput.keyDown('space')
            time.sleep(0.14)
            pydirectinput.keyUp('space')
            
            time.sleep(0.06)
        else:
            # Idle wait when unfocused
            time.sleep(0.01)
            
    if keyboard.is_pressed('esc'):
        print("\nScript terminated.")
        break
