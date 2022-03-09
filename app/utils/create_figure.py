import matplotlib.pyplot as plt


def create_figure(labels, data):
    """
    This function returns a fig of a plot. The plot is built with the given data and labels.
    The plot is a chart with horizontal bars.
    """

    # make the plot canvas
    fig, ax = plt.subplots()

    # manage colors
    bar_colors = ['#1A4A04CC', '#750014CC', '#795703CC', '#06216CCC', '#3F0355CC']
    edge_colors = ['#1A4A04FF', '#750014FF', '#795703FF', '#06216CFF', '#3F0355FF']

    # fill plot
    ax.barh(labels, data, align='center', color=bar_colors, edgecolor=edge_colors)
    ax.invert_yaxis()  # labels read top-to-bottom

    # make legend
    plt.legend(['Output scores'], loc='upper center', bbox_to_anchor=(0., 1.02, 1., .102))

    # avoid image cropping
    fig.tight_layout()

    return fig
