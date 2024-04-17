from __future__ import print_function, unicode_literals, absolute_import, division
from 2D_detection_functions import *
# Here import important system functions
import os
# import tk for getting the directory faster. dont need this in a command line/server version
from tkinter import *
from tkinter import filedialog
import glob
#this is for getting the directory, and helps saving time of typing what ever directory it is.
import numpy as np
import csv
# if you dont need to plot in jupyter you don need these. Some magic interperters need to be removed for command line version.
import matplotlib
import random
import math
matplotlib.rcParams["image.interpolation"] = 'none'
import matplotlib.pyplot as plt
# Glob and tifffile are needed
from glob import glob
from tifffile import imread,imwrite
# csb deep is to take normalization
from csbdeep.utils import Path, normalize
from csbdeep.io import save_tiff_imagej_compatible
# This is your stardist models and everything in stardist coming from.
from stardist import random_label_cmap, _draw_polygons, export_imagej_rois
from stardist.models import StarDist2D
lbl_cmap = random_label_cmap()
root = Tk()
pathname = filedialog.askdirectory()
# Close Tk window
root.destroy
root.quit()
# Change directory
os.chdir(pathname)
dataset = sorted(glob('*.tif'))
dataset = list(map(imread,X))
# Change Normalize parameters here
normalize_param = (0.1,99.8)
# Change detection parameters here, first one is probablilty and second one is overlap
detection_param = (0.1,0.1)
model = StarDist2D.from_pretrained('2D_versatile_fluo')