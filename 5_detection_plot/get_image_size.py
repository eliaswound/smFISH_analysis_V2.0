def get_image_size (pathname = "."):
    """
    :param pathname: the pathname contains the image
    :return: size of the image in zxy
    """
    import numpy as np
    import glob
    filename = glob.glob('*.npy')
    imarray = np.load(filename[0])
    image_shape = imarray.shape

    return image_shape