def create_results_directory():
    current_directory = os.getcwd()  # Get the current working directory
    results_directory = os.path.join(current_directory, 'results')  # Path to the results directory

    if not os.path.exists(results_directory):  # Check if the results directory exists
        os.mkdir("results")  # Create the results directory if it doesn't exist
        print("Results directory created successfully.")
    else:
        print("Results directory already exists.")

# Call the function to create the directory

def make_stardist_Predictions (dataset, normalize_low = 0, normalize_high = 0, nms_thresh = 0, prob_thresh = 0):
    for i in range(len(dataset)):
        if normalize_low ==0 or normalize_high == 0:
            img = normalize(dataset[i], 1,99.8, axis=(0,1))
        else:
            img = normalize(dataset[i], normalize_low, normalize_high, axis=(0,1))
        if nms_thresh == 0 or prob_thresh == 0 :
            labels, polygons = model.predict_instances(img)
            labels, details = model.predict_instances(img)
        else:
            labels, polygons = model.predict_instances(img,nms_thresh = nms_thresh, prob_thresh = prob_thresh)
            labels, details = model.predict_instances(img,nms_thresh = nms_thresh, prob_thresh = prob_thresh)
        # write labels
        imwrite("labels/Nucleus_Labels_"+str(i).zfill(3)+".tif", labels)
        # Create figure for images + labels
        labelfigure = plt.figure(figsize=(8,8))
        plt.imshow(img if img.ndim==2 else img[...,0], clim=(0,1), cmap='gray')
        plt.imshow(labels, cmap=lbl_cmap, alpha=0.5)
        plt.axis('off');
        plt.savefig('images/segmented_image_'+str(i).zfill(3)+'.png')
        plt.close(labelfigure)
        # Export polygons
        export_imagej_rois('polygons/polygon_rois_'+str(i).zfill(3)+'.zip', polygons['coord'])


def random_select_images(image_list, percentage):
    """
    Randomly selects X% of images from the given list.

    Parameters:
        image_list (list): List of images.
        percentage (float): Percentage of images to select.

    Returns:
        list: List of randomly selected images.
    """
    # Calculate the number of images to select
    num_images_to_select = math.ceil(len(image_list) * percentage / 100)

    # Randomly select images
    selected_images = random.sample(image_list, num_images_to_select)

    return selected_images


def random_crop_images(dataset, X, Y):
    """
    Randomly crops images from the dataset to the specified size (X, Y).

    Parameters:
        dataset (list of 2D arrays): List of images.
        X (int): Width of the cropped area.
        Y (int): Height of the cropped area.

    Returns:
        list: List of cropped images.
    """
    cropped_dataset = []

    for image in dataset:
        height, width = image.shape

        # Check if X or Y exceeds the dimensions of the image
        if X > width or Y > height:
            raise ValueError("X or Y exceeds the dimensions of the image")

        # Generate random coordinates for the top-left corner of the cropped area
        top_left_x = random.randint(0, width - X)
        top_left_y = random.randint(0, height - Y)

        # Crop the image
        cropped_image = image[top_left_y:top_left_y + Y, top_left_x:top_left_x + X]

        cropped_dataset.append(cropped_image)

    return cropped_dataset

def example(model, image, show_dist=True):
    # Normalized image
    img = normalize(image, 1,99.8, axis = (0,1))
    # Get labels and details
    labels, details = model.predict_instances(img)
    # Plt figure
    figure = plt.figure(figsize=(13,10))
    # Make image to show
    img_show = img if img.ndim==2 else img[...,0]
    # Get coordinates
    coord, points, prob = details['coord'], details['points'], details['prob']
    # Plot image on the first one
    ax1 = figure.add_subplot(131); ax1.imshow(img_show, cmap='gray'); ax1.axis('off')
    # Plot image on the second one
    ax2 = figure.add_subplot(132); ax2.imshow(img_show, cmap='gray'); ax2.axis('off')
    # plot the ploygons using the function from stardist
    a = ax2.axis()
    _draw_polygons(coord, points, prob, show_dist=show_dist)
    ax2.axis(a)
    # Plot the image on the third one
    ax3 = figure.add_subplot(133); ax3.imshow(img_show, cmap='gray'); ax3.axis('off')
    # Plot labels on the third one.
    ax3.imshow(labels, cmap=lbl_cmap, alpha=0.5)
    figure.tight_layout()
    return figure