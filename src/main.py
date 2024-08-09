import tkinter as tk
from tkinter import messagebox
from time import sleep as wait
import webbrowser
import pyautogui
import ctypes

def make_transparent_overlay():

    root = tk.Tk()
    root.attributes('-fullscreen', True)  
    root.config(bg='black')  
    root.lift()  
    root.attributes('-topmost', True)  
    root.attributes('-transparentcolor', 'black')  
    root.overrideredirect(True)  

    root.update()

    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())

    ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x20)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x02)

    label = tk.Label(root, text="Surprise! 😈", fg="white", bg="black", font=("Arial", 100))
    label.pack(expand=True)

    root.update()
    url = "https://copy.sh/v86/?profile=windows2000"
    webbrowser.open(url)
    wait(0.4)  

    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')

    wait(0.3)  

    fullscreen_button_location = (1164, 117)  
    pyautogui.click(fullscreen_button_location)

    wait(0.1)  

    another_button_location = (1002, 126)  
    pyautogui.click(another_button_location)

    wait(5)  

    root.destroy()

def troll_animation():
    root = tk.Tk()
    root.withdraw()

    messages = [
        ("Hello there!, Wanna Play?", "ok"),
        ("Ok, This game is very easy. If you lose, you will be a Windows 2000 user!", "ok"),
        ("Let's start!", "ok"),
        ("1 + 1 = you??", "yesno")
    ]

    for message, msg_type in messages:
        wait(1)
        if msg_type == "ok":
            messagebox.showinfo("", message)
        elif msg_type == "yesno":
            response = messagebox.askyesno("", message)
            if response:
                print("User chose Yes.")
                messagebox.showerror("", "Nah")
            else:
                print("User chose No.")
                messagebox.showerror("", "Nah")
                
    messagebox.showwarning("You lose!", "ok"),
    messagebox.showwarning("LOL!", "ok")

    wait(0.2)
    open_url()

def open_url():
    make_transparent_overlay()

if __name__ == "__main__":
    troll_animation()