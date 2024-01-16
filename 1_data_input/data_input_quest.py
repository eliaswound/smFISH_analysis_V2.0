pathname= "/scratch/qgs8612/smFISHanalysis"
import os
import glob
import tifffile
import numpy as np
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