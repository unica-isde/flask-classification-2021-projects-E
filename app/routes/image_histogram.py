from flask import render_template

from app import app
from app.forms.histogram_form import HistogramForm
from app.utils.create_folder_if_not_found import create_folder_if_not_found
from app.utils.make_histogram_plot import make_histogram_plot, make_histogram_plot_rgb
from config import Configuration

config = Configuration()


@app.route('/image_histogram', methods=['GET', 'POST'])
def image_histogram():
    """API for picking one image from a list and returning the histogram of it.
    It calls the job queue to assign the task to worker."""
    form = HistogramForm()
    if form.validate_on_submit():  # POST
        # get image and convert it as np array
        image_id = form.image.data

        # make the histogram plots
        plot_id = make_histogram_plot(image_id)
        plot_rgb_id = make_histogram_plot_rgb(image_id)

        # if it is a post request, it shows the histogram plot
        return render_template("histogram_output.html", image_id=image_id, plot_id=plot_id, plot_rgb_id=plot_rgb_id)

    # otherwise, it is a get request and should return the image selector
    return render_template('histogram_select.html', form=form)
