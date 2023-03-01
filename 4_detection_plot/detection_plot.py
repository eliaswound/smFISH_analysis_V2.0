def detection_plot(image_shape, filepath):
    """
    :param np.shape of a image
    :param spot: spot need to be plotted
    :return: plotted image
    """
    import os
    import numpy as np
    os.chdir(filepath)
    spot = np.load("spot.npy")
    empty_image = np.zeros(image_shape, dtype=np.uint8)
    z_lim = empty_image.shape[0]-1
    x_lim = empty_image.shape[1]-1
    y_lim = empty_image.shape[2]-1
    for i in range(spot.shape[0]):
        spot_pos = np.ndarray.tolist(spot[i])
        z = spot_pos[0]
        x = spot_pos[1]
        y = spot_pos[2]
        if x + 3 > x_lim or y + 3 > y_lim:
            np.delete(spot, spot[i])
        elif x - 3 > x_lim or y - 3 > y_lim:
            np.delete(spot, spot[i])
        elif z == 0 or z == z_lim:
            np.delete(spot, spot[i])
        else:
            empty_image[z, x, y] = 255
            empty_image[z, x + 2, y] = 255
            empty_image[z, x + 1, y + 1] = 255
            empty_image[z, x + 1, y] = 255
            empty_image[z, x + 1, y - 1] = 255
            empty_image[z, x, y + 1] = 255
            empty_image[z, x, y + 2] = 255
            empty_image[z, x, y - 1] = 255
            empty_image[z, x, y - 2] = 255
            empty_image[z, x - 2, y] = 255
            empty_image[z, x - 1, y + 1] = 255
            empty_image[z, x - 1, y] = 255
            empty_image[z, x - 1, y - 1] = 255

    return spot, empty_image
def shadow_plot(image_shape, filepath):
    """
    :param image_shape: image shape 
    :param filepath: current file path 
    :return: shadow image 
    """
    import numpy as np
    import os
    os.chdir(filepath)
    spot = np.load("spot.npy")
    empty_image2 = np.zeros(image_shape, dtype=np.uint8)
    z_lim = empty_image2.shape[0] - 1
    x_lim = empty_image2.shape[1] - 1
    y_lim = empty_image2.shape[2] - 1
    for i in range(spot.shape[0]):
        spot_pos = np.ndarray.tolist(spot[i])
        z = spot_pos[0]
        x = spot_pos[1]
        y = spot_pos[2]
        if x + 3 > x_lim or y + 3 > y_lim:
            np.delete(spot, spot[i])
        elif x - 3 > x_lim or y - 3 > y_lim:
            np.delete(spot, spot[i])
        elif z == 1 or z == z_lim:
            np.delete(spot, spot[i])
        else:
            empty_image2[z + 1, x + 3, y] = 255
            empty_image2[z + 1, x - 3, y] = 255
            empty_image2[z + 1, x + 2, y + 1] = 255
            empty_image2[z + 1, x + 2, y - 1] = 255
            empty_image2[z + 1, x + 1, y + 2] = 255
            empty_image2[z + 1, x + 1, y - 2] = 255
            empty_image2[z + 1, x - 2, y - 1] = 255
            empty_image2[z + 1, x - 2, y + 1] = 255
            empty_image2[z + 1, x - 1, y - 2] = 255
            empty_image2[z + 1, x - 1, y + 2] = 255
            empty_image2[z + 1, x, y + 3] = 255
            empty_image2[z + 1, x, y - 3] = 255
            empty_image2[z - 1, x + 3, y] = 255
            empty_image2[z - 1, x - 3, y] = 255
            empty_image2[z - 1, x + 2, y + 1] = 255
            empty_image2[z - 1, x + 2, y - 1] = 255
            empty_image2[z - 1, x + 1, y + 2] = 255
            empty_image2[z - 1, x + 1, y - 2] = 255
            empty_image2[z - 1, x - 2, y - 1] = 255
            empty_image2[z - 1, x - 2, y + 1] = 255
            empty_image2[z - 1, x - 1, y - 2] = 255
            empty_image2[z - 1, x - 1, y + 2] = 255
            empty_image2[z - 1, x, y + 3] = 255
            empty_image2[z - 1, x, y - 3] = 255
    return empty_image2