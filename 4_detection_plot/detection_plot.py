def generate_coordinates_inner(x, y, time):
    # Initial collection with the starting coordinate (x, y)
    coordinates_collection = [(x, y)]

    for _ in range(time):
        # Copy the current collection to avoid modifying it while iterating
        current_coordinates = coordinates_collection.copy()

        # Loop through each coordinate in the current collection
        for coord in current_coordinates:
            # Extract x and y values from the coordinate
            cx, cy = coord

            # Add neighboring coordinates to the collection
            coordinates_collection.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

    # Remove duplicates by converting the list to a set and then back to a list
    coordinates_collection = list(set(coordinates_collection))

    return coordinates_collection

def generate_coordinates_outer(x, y, time):
    # Initial collection with the starting coordinate (x, y)
    coordinates_collection = [(x, y)]

    for _ in range(time):
        # Copy the current collection to avoid modifying it while iterating
        current_coordinates = coordinates_collection.copy()

        # Loop through each coordinate in the current collection
        for coord in current_coordinates:
            # Extract x and y values from the coordinate
            cx, cy = coord

            # Add neighboring coordinates to the collection
            coordinates_collection.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

    # Remove duplicates by converting the list to a set and then back to a list
    coordinates_collection = list(set(coordinates_collection))

    # Filter coordinates that were added up to the specified time
    coordinates_collection = [coord for coord in coordinates_collection if abs(coord[0]-x) + abs(coord[1]- y) == time]

    return coordinates_collection



def detection_plot(image_shape, filepath, plot_size):
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
            coordinates = generate_coordinates_inner(x,y,plot_size)
            for item in coordinates:
                empty_image[z,item[0],item[1]] = 255


    return spot, empty_image
def shadow_plot(image_shape, filepath, plot_size):
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
            coordinates = generate_coordinates_outer(x,y,plot_size+1)
            for item in coordinates:
                empty_image2[z+1,item[0],item[1]] = 255
                empty_image2[z-1,item[0],item[1]] = 255
    return empty_image2