from flask import render_template

from app import app
from app.forms.color_jitter_form import JitterImageForm
from config import Configuration

from ml import jitter_transformation

config = Configuration()


@app.route('/transformations/color_jitter_image', methods=['GET', 'POST'])
def color_jitter_image():
    """
    API for applying a color jitter transformation to a user selected
    image. Returns the image with the applied transformation.
    """
    form = JitterImageForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        brightness = form.brightness.data
        saturation = form.saturation.data
        contrast = form.contrast.data
        hue = form.hue.data

        image_name = jitter_transformation(image_id, brightness, contrast, saturation, hue)

        return render_template("color_jitter_output.html",
                               image_id=image_id, brightness=brightness, image_name=image_name)

    # otherwise, it is a get request and should return the
    # form for image selection
    return render_template('color_jitter_select.html', form=form)