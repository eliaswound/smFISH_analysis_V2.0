def cluster_decomposition(imarray,spots,voxel_size,spot_size,greeks,filepath = "."):
    """
    Decomposition of clusters
    :param imarray: Image array
    :param spots: spots detected
    :param resolution: resolution
    :param spot_size: spot size
    :param greeks: greeks alpaha beta gamma
    :return:
    """
    import os
    import bigfish.detection
    import numpy as np
    os.chdir(filepath)
    alpha = greeks[0]
    beta = greeks[1]
    gamma = greeks[2]
    spots_post_decomposition, dense_regions, reference_spot = bigfish.detection.decompose_dense(
    image=imarray,
    spots=spots,
    voxel_size= voxel_size,
    spot_radius= spot_size,
    alpha=alpha,  # alpha impacts the number of spots per candidate region
    beta=beta,  # beta impacts the number of candidate regions to decompose
    gamma=gamma)  # gamma the filtering step to denoise the image
    np.save(spots_post_decomposition,'spots_post_decomposition.npy')
    with open("spots_info_Decomposition.txt","w") as file :
        file.write("detected spots before decomposition")
        file.write("\r shape: {0}".format(spots.shape))
        file.write("\r dtype: {0}".format(spots.dtype))
        file.write("\n")
        file.write("detected spots after decomposition")
        file.write("\r shape: {0}".format(spots_post_decomposition.shape))
        file.write("\r dtype: {0}".format(spots_post_decomposition.dtype))
    return spots_post_decomposition, dense_regions, reference_spot
def declustering(spot, voxel_size, deculstering_parameters,filepath = "."):
    """
    Declustering code
    :param spots_post_decompositions: spots
    :param resolution: resolution
    :param deculstering_parameters:declustering parameters
    imarray: image array
    :return: spts and clusters
    """
    radius = deculstering_parameters[0]
    nb_min_spots = deculstering_parameters[1]
    import bigfish.detection
    import os
    import numpy as np
    os.chdir(filepath)
    spots_post_clustering, clusters = bigfish.detection.detect_clusters(
        spots=spot,
        voxel_size=voxel_size,
        radius=radius,
        nb_min_spots=nb_min_spots)
    np.save('spot_post_cluster.npy', spots_post_clustering)
    np.save('clusters.npy', clusters)
    with open("Cluster_info.txt", "w") as file:
        file.write("detected spots after clustering")
        file.write("\r shape: {0}".format(spots_post_clustering.shape))
        file.write("\r dtype: {0}".format(spots_post_clustering.dtype))
        file.write("\n")
        file.write("detected clusters")
        file.write("\r shape: {0}".format(clusters.shape))
        file.write("\r dtype: {0}".format(clusters.dtype))
    return spots_post_clustering, clusters