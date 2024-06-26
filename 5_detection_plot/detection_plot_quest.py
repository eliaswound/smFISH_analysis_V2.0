import os
import glob
import numpy as np
import tifffile
from get_image_size import *
from detection_plot import *
pathname= "/scratch/qgs8612/smFISHanalysis"

os.chdir(pathname)
# Grab all tif files in the folder
filename = glob.glob('*.npy')[0]
plot_size = 3
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)
# Get image shape
image_shape = get_image_size(pathname)
# change directory to results folder
os.chdir("results")
# Run detection plot
spot_modified, spot_plot = detection_plot(image_shape, os.getcwd(), plot_size)
shadow = shadow_plot(image_shape, os.getcwd(),plot_size)
# Save image and modified spot
np.save("spot_modified.npy", spot_modified)
# Writed detected image
tifffile.imwrite('detection_plot.tif', spot_plot, photometric='minisblack')
tifffile.imwrite('detection_shadow_plot.tif', shadow, photometric='minisblack')