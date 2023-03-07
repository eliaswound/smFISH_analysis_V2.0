from __future__ import print_function, unicode_literals, absolute_import, division
import sys
import numpy as np
import tifffile
import matplotlib
import matplotlib.pyplot as plt
from glob import glob
from tifffile import imread
from csbdeep.utils import Path, normalize
from csbdeep.io import save_tiff_imagej_compatible
import os
from stardist import random_label_cmap
from stardist.models import StarDist3D
np.random.seed(42)
lbl_cmap = random_label_cmap()


# Step1: Nucleus identification

filepath = "D:/Northwestern/Research/Chris_Petersen_lab/022523_smFISH_analysis_v2.0_development/405"
os.chdir(filepath)
X = sorted(glob('*.tif'))
X = list(map(imread,X))

n_channel = 1 if X[0].ndim == 3 else X[0].shape[-1]
axis_norm = (0,1,2)   # normalize channels independently
# axis_norm = (0,1,2,3) # normalize channels jointly
if n_channel > 1:
    print("Normalizing image channels %s." % ('jointly' if axis_norm is None or 2 in axis_norm else 'independently'))
demo_model = True

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
img = normalize(X[0], 0.2,99.8, axis=axis_norm)
labels, details = model.predict_instances(img,nms_thresh = 0.3,prob_thresh =0.6)
tifffile.imwrite("Nucleus_Labels.tif",labels)
np.shape(labels)
plt.figure(figsize=(13,10))
z = max(0, img.shape[0] // 2 - 5)
plt.subplot(121)
plt.imshow((img if img.ndim==3 else img[...,:3])[z], clim=(0,1), cmap='gray')
plt.title('Raw image (XY slice)')
plt.axis('off')
plt.subplot(122)
plt.imshow((img if img.ndim==3 else img[...,:3])[z], clim=(0,1), cmap='gray')
plt.imshow(labels[z], cmap=lbl_cmap,alpha=0.5)
plt.title('Image and predicted labels (XY slice)')
plt.axis('off');


#Step2: Expand segmentation labels

import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.color import label2rgb
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import expand_labels, watershed

labels = "D:/Northwestern/Research/Chris_Petersen_lab/022523_smFISH_analysis_v2.0_development/405/Labeled_nucleus.tif"

nlabels = data.labels()

# Make segmentation using edge-detection and watershed.
edges = sobel(labels)

# Identify some background and foreground pixels from the intensity values.
# These pixels are used as seeds for watershed.
markers = np.zeros_like(labels)
foreground, background = 1, 2
markers[labels.0] = background
markers[coins > 150.0] = foreground

ws = watershed(edges, markers)
seg1 = label(ws == foreground)

expanded = expand_labels(seg1, distance=10)

# Show the segmentations.
fig, axes = plt.subplots(
    nrows=1,
    ncols=3,
    figsize=(9, 5),
    sharex=True,
    sharey=True,
)

axes[0].imshow(coins, cmap="Greys_r")
axes[0].set_title("Original")

color1 = label2rgb(seg1, image=coins, bg_label=0)
axes[1].imshow(color1)
axes[1].set_title("Sobel+Watershed")

color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[2].imshow(color2)
axes[2].set_title("Expanded labels")

for a in axes:
    a.axis("off")
fig.tight_layout()
plt.show()


