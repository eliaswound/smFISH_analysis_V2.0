from tkinter import *
from tkinter import filedialog
import os
import glob
import numpy as np
import tifffile
#LOAD FILES
# Load detected spots
# Load files from the selected directory
# Open up a tk window and ask for directory input
root = Tk()
pathname = filedialog.askdirectory()
# Close Tk window
root.destroy()
# Change directory
os.chdir(pathname)
# Grab all tif files in the folder
filename = glob.glob('Nucleus_Expandlabels.tif')
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)
labels = tifffile.imread(filename)

# Same as above, read the labels npy file
root = Tk()
pathname = filedialog.askdirectory()
root.destroy()
os.chdir(pathname)
filename = glob.glob('spot_post_cluster.npy')[0]
print(os.getcwd())
print(filename)
spots = np.load(filename)

spotsarr = np.array(spots)
labelsarr = np.array(labels)

spot_count = {}

for i, spot in enumerate(spots):
    label = labels[int(spot[0]), int(spot[1]), int(spot[2])]

    if label not in spot_count:
        spot_count[label] = 1
    else:
        spot_count[label] += 1


for label, count in spot_count.items():
    print(f"Label {label}: {count} spots")

# print the total number of labels and spots
num_labels = len(spot_count)
total_spots = sum(spot_count.values())
print(f"\nTotal labels: {num_labels}")
print(f"Total spots: {total_spots}")

