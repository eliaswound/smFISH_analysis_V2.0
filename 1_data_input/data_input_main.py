from tkinter import *
from tkinter import filedialog
import os
import glob
import tifffile
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
filename = glob.glob('*.tif')[0]
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)
# Data input
# Input 633 image
image_array = tifffile.imread(filename)
np.save("image_array.npy", image_array)

