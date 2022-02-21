import numpy as np
import matplotlib.pyplot as plt

from app.utils.create_folder_if_not_found import create_folder_if_not_found
from ml.classification_utils import fetch_image


def make_histogram_plot(image_id):
    """
    This function returns the id of the histogram plot of an image, given its id.
    Average between channels is considered for every single pixel.
    """
    img_array = fetch_image(image_id)
    img_array = np.array(img_array.convert('RGB'))

    # calculate mean value from RGB channels and flatten to 1D array
    vals = img_array.mean(axis=2).flatten()

    # assign labels
    plt.xlabel('pixel values')
    plt.ylabel('occurrences')

    # clear figure
    plt.figure().clear()

    # assign title
    plt.title("Histogram of the image (average of the 3 channels of each pixel)")

    plt.plot()

    # plot histogram with 255 bins (columns)
    b, bins, patches = plt.hist(vals, 255, color='black')
    plt.xlim([0, 255])

    # get the id of the plot and save it
    plot_id = '{}_histogram.png'.format(image_id.replace('.JPEG', ''))
    plt.savefig('{}/{}'.format(get_histogram_folder(), plot_id))

    return plot_id


def make_histogram_plot_rgb(image_id):
    """
    This function returns the id of the histogram plot of an image, given its id.
    Channels are plotted separately in different sub-plots.
    """
    img_array = fetch_image(image_id)
    img_array = np.array(img_array.convert('RGB'))

    # channels
    ch_list = ['red', 'green', 'blue']


    # clear figure
    plt.figure().clear()

    # divide in 3 sub-plots
    fig, axs = plt.subplots(3, 1, tight_layout=True)

    for ch_id, ch in enumerate(ch_list):
        # get the channel pixels and convert in 1D array
        vals = img_array[:, :, ch_id].flatten()

        # plot histogram with 255 bins (columns)
        b, bins, patches = axs[ch_id].hist(vals, 255, color=ch)

        # set limit for x-axis
        axs[ch_id].set_xlim([0, 255])

    # assign title and labels
    plt.suptitle("Histograms of the image divided by color (Red, Green, and Blue)")
    plt.xlabel('pixel values')
    axs[1].set_ylabel('occurrences')

    # get the id of the plot and save it
    plot_rgb_id = '{}_histogram_rgb.png'.format(image_id.replace('.JPEG', ''))
    plt.savefig('{}/{}'.format(get_histogram_folder(), plot_rgb_id))

    return plot_rgb_id


def get_histogram_folder():
    """ This function returns the name of the folder of the histograms."""
    histogram_folder = 'app/static/histograms'
    create_folder_if_not_found(histogram_folder)
    return histogram_folder
