from tkinter import *
from tkinter import filedialog
import os
import glob
import numpy as np
import tifffile
from get_image_size import *
from detection_plot import *
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
plot_size = 6
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)
# Get image shape
image_shape = get_image_size(pathname)
# change directory to results folder
os.chdir("results")
# Run detection plot
spot_modified, spot_plot = detection_plot(image_shape, os.getcwd(),plot_size)
shadow = shadow_plot(image_shape, os.getcwd(),plot_size)
# Save image and modified spot
np.save("spot_modified.npy", spot_modified)
# Writed detected image
tifffile.imwrite('detection_plot.tif', spot_plot, photometric='minisblack')
tifffile.imwrite('detection_shadow_plot.tif', shadow, photometric='minisblack')