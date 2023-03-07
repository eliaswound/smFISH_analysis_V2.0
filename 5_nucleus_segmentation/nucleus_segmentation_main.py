from __future__ import print_function, unicode_literals, absolute_import, division
import sys
import numpy as np
import tifffile
from glob import glob
from tifffile import imread
from csbdeep.utils import normalize
import os
from stardist import random_label_cmap
from stardist.models import StarDist3D
np.random.seed(42)
lbl_cmap = random_label_cmap()


# Step1: Nucleus identification

filepath = "D:/Northwestern/Research/Chris_Petersen_lab/022523_smFISH_analysis_v2.0_development/405"
# Change directory
os.chdir(filepath)
# Read in file as a list
X = sorted(glob('*.tif'))
X = list(map(imread,X))
# Channel sorting if it is multi channel image the last dimension will be numbers of channels
# If it is a 3D image, it will only have 3 dimensions channel number will be 1
n_channel = 1 if X[0].ndim == 3 else X[0].shape[-1]
# Define which axis need to be normalized
axis_norm = (0,1,2)   # normalize channels independently
# axis_norm = (0,1,2,3) # normalize channels jointly
# if multi channel, decide if you need to normalize across all channel or separately
if n_channel > 1:
    print("Normalizing image channels %s." % ('jointly' if axis_norm is None or 2 in axis_norm else 'independently'))
# Load demo
demo_model = True
# If we have a demo, run demo. If not, run trained model.
if demo_model:
    print (
        "NOTE: This is loading a previously trained demo model!\n"
        "      Please set the variable 'demo_model = False' to load your own trained model.",
        file=sys.stderr, flush=True
    )
    model = StarDist3D.from_pretrained('3D_demo')
else:
    model = StarDist3D(None, name='stardist', basedir='models')
None;
# normalization
img = normalize(X[0], 0.2,99.8, axis=axis_norm)
# Prediction
labels, details = model.predict_instances(img,nms_thresh = 0.3,prob_thresh =0.6)
# Write file and labels
tifffile.imwrite("results/Nucleus_Labels.tif", labels)