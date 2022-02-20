import numpy as np
import matplotlib.pyplot as plt

from ml.classification_utils import fetch_image


def make_histogram_plot(image_id):
    """
    This function returns the histogram plot of an image, given its id.
    """
    img_array = fetch_image(image_id)
    img_array = np.array(img_array.convert('RGB'))

    # calculate mean value from RGB channels and flatten to 1D array
    vals = img_array.mean(axis=2).flatten()

    # assign labels
    plt.xlabel('pixel value')
    plt.ylabel('occurrences')

    # assign title
    plt.title("Histogram of the image")

    plt.plot()

    # plot histogram with 255 bins (columns)
    b, bins, patches = plt.hist(vals, 255)
    plt.xlim([0, 255])

    return plt
