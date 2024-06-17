from tkinter import *
from tkinter import filedialog
import os
import glob
import numpy as np
import tifffile
from cluster_detection import *

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

imarray = np.load(filename)
os.chdir("results")
spot = np.load("spot_modified.npy")
voxel_size = (361, 64, 64)
declustering_parameters = (600, 6)
greeks = (0.7, 1, 5)
spot_size = (600, 250, 250)
# First number alpha: Impact number of spots in each regtion
# Second number beta, affect number of regions to decompose
# Third number gamma, filtering for image denoise
spots_post_decomposition, dense_regions, reference_spot = cluster_decomposition(imarray, spot, voxel_size, spot_size, greeks, filepath = ".")
spots_post_clustering, clusters = declustering(spots_post_decomposition, voxel_size, declustering_parameters, filepath=".")


