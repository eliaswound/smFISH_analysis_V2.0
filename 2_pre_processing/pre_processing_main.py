from tkinter import *
from tkinter import filedialog
import os
import glob
import numpy as np


# Load files from the selected directory
# Open up a tk window and ask for directory input
root = Tk()
pathname = filedialog.askdirectory()
# Close Tk window
root.destroy()
# Change directory
os.chdir(pathname)
# Grab all tif files in the folder
filename = glob.glob('*.npy')[0]
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)
# Data input
# Input image array
image_array = np.load(filename)
# Deal with background
