def get_elbow_curve(imarray, resolution,spot_size, filepath = "."):
    """
    Plots and saves elbow curve
    :param imarray: Image array
    :param resolution: Resolution on z,x,y as nanommeters
    :param spot_size: Spot size or spot radius
    :param filepath: Filepath, default current filepath
    :return: no return
    """
    import bigfish.plot as plot
    import os
    os.chdir(filepath)
    plot.plot_elbow(
        images=imarray,
        voxel_size=resolution,
        spot_radius=spot_size,
        path_output="results/Elbow",
        show=False)

    return

def spot_detection(imarray, resolution, spot_size, kernel_size,minimal_distance,filepath = "."):
    """
    This is the core spot detection program:
    input:
    :param imarray: Image array for spot detection
    :param resolution: Resolution z,x,y
    :param spot_size: Spot size
    :param kernel_size: Kernel size for LoG filter
    :param minimal_distance: Minimal distance between spots
    :return: Detected spots, threshold
    """
    import bigfish.detection
    import os
    import numpy as np
    os.chdir(filepath)
    spots, threshold = bigfish.detection.detect_spots(
        images=imarray,
        return_threshold=True,
        voxel_size= resolution,  # in nanometer (one value per dimension zyx)
        spot_radius= spot_size, # in nanometer (one value per dimension zyx)
        log_kernel_size= kernel_size,
        minimum_distance= minimal_distance)

    # Out put your spot detection results as txt file
    # Also added a estimation of signal-to-noise ratio
    np.save('results/spot.npy', spots)
    with open ("results/spot_info.txt","w") as file :
        file.write("\r shape: {0}".format(spots.shape))
        file.write("\r dtype: {0}".format(spots.dtype))
        file.write("\r threshold: {0}".format(threshold))

    return spots,threshold

def spots_plot_detection(spots,imarray,filepath = "."):
    import os
    import bigfish.stack as stack
    import bigfish.plot as plot
    os.chdir(filepath)
    max_imarray = stack.maximum_projection(imarray)
    # Plot detection
    plot.plot_detection(max_imarray,
                        spots,
                        contrast=True,
                        path_output="results/detectionmap2D_rotated",
                        ext = "tif",
                        show = False)
    return
