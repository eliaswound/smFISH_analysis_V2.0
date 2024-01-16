import os
import glob
from pre_processing import *
from spot_detection import *
pathname= "/scratch/qgs8612/smFISHanalysis"
os.chdir(pathname)
# Grab all tif files in the folder
filename = glob.glob('*.npy')[0]
# Print working directory and filename to confirm we are at the correct path
print(os.getcwd())
print(filename)


# Setting parameters for spot detection
minimal_distance = (2, 2, 2)   # Minimal distance of spots z,x, y
kernel_size = (2.5, 1.3, 1.3)   # Kernel size of LoG filter, z usuall 2.5-4, x,y start with 1.5
voxel_size = (361, 64, 64)
spot_size = (600, 250, 250)
# Preprocess Image
imarray = smFISHpreprocessing(kernel_size, minimal_distance, pathname)
# Detection of Spots
get_elbow_curve(imarray, voxel_size, spot_size, pathname)
spots, threshold = spot_detection(imarray, voxel_size, spot_size, kernel_size, minimal_distance, pathname)
spots_plot_detection(spots, imarray, pathname)