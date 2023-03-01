def smFISHpreprocessing(kernel_size,minimal_distance,file_path = '.'):
    """
    This function will batch with pre-processing of the tiff image
    including: Read in Tiff image and return it as ndarray
               Create a max projection of tiff image and save it in results folder (If there is no such a folder create one)
               Create a Local maximum filter based on kernel size (Optional can return the filter but I dont think we need)
               Apply local maximum filter and save it in results folder
               Create a max projection image for local max filter
               Create a LoG filter based on the kernel size provided
               Apply LoG filter and save the image in results folder
               Create a max projection for LoG filtered Image
               Apply both LoG and local max filter and save max projection and original image
    :param file_path: The file path the image is in. Default use current file path
    :param kernel_size: The Kernel size used for LoG filter, 3d or 2d nd array
    :param minmal_dsitacne: The minimal distance between each spots for creating local maximum filter 3d or 2d nd array
    :return: The ndarray the Image look like.
    """
    import numpy as np
    import glob
    import tifffile
    import bigfish
    import os
    import bigfish.stack as stack
    import bigfish.detection as detection
    os.chdir(file_path)
    dir_list_temp = os.listdir()
    if 'results' not in dir_list_temp:
        os.mkdir("results")
    # Read in all files
    tiff_name = glob.glob("*.tif")
    imarray = tifffile.imread(tiff_name[0])
    # Maxmium intensity projection
    max_imarray = bigfish.stack.maximum_projection(imarray)
    tifffile.imwrite('results/max_imarray.tif', max_imarray, photometric='minisblack')
    # Create local max mask of original image
    imarray_localmax_mask = bigfish.detection.local_maximum_detection(imarray, minimal_distance)
    # apply the local max mask by simple multiplication
    imarray_localmax = imarray_localmax_mask * imarray
    tifffile.imwrite('results/imarray_localmax.tif', imarray_localmax, photometric='minisblack')
    # Max projection and save
    max_imarray_localmax = bigfish.stack.maximum_projection(imarray_localmax)
    tifffile.imwrite('results/max_imarray_localmax.tif', max_imarray_localmax, photometric='minisblack')
    # apply LoG filter
    imarray_LoG = bigfish.stack.log_filter(imarray, kernel_size)
    # Create local max mask for LoG filtered image
    imarray_LoG_localmax_mask = bigfish.detection.local_maximum_detection(imarray_LoG, kernel_size)
    # apply the local max mask to LoG filtered image
    imarray_LoG_localmax = imarray_LoG_localmax_mask * imarray_LoG
    # max projections
    max_imarray_LoG = bigfish.stack.maximum_projection(imarray_LoG)
    max_imarray_LoG_localmax = bigfish.stack.maximum_projection(imarray_LoG_localmax)
    # Save files
    tifffile.imwrite('results/filtered_imarray', imarray, photometric='minisblack')
    tifffile.imwrite('results/imarray_LoG.tif', imarray_LoG, photometric='minisblack')
    tifffile.imwrite('results/imarray_LoG_localmax.tif', imarray_LoG_localmax, photometric='minisblack')
    tifffile.imwrite('results/max_imarray_LoG_localmax.tif', max_imarray_LoG_localmax, photometric='minisblack')
    tifffile.imwrite('results/max_imarray_LoG.tif', max_imarray_LoG, photometric='minisblack')

    return imarray

def rotateImage(angle, imarray):
    """
    Input a ndarray of image and an angle
    Rotate the image by certain angle and save it as tiffile
    Returns the rotated image
    :param imarray: image array need to be rotated
           angle: Rotation angle
    :return:
    """
    from scipy import ndimage
    import tifffile
    import bigfish.stack
    angle = -((90-angle)%360)
    imarray_rotated = ndimage.interpolation.rotate(imarray,angle,axes = (1,2))
    max_imarray_rotated = bigfish.stack.maximum_projection(imarray_rotated)
    # Save image by tifffile
    tifffile.imwrite('results/imarray_rotated.tif',imarray_rotated,photometric='minisblack')
    tifffile.imwrite('results/max_imarray_rotated.tif',max_imarray_rotated,photometric = 'minisblack')
    return imarray_rotated
