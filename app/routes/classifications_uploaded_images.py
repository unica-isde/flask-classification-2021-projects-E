from flask import request, render_template
from app import app
from app.forms.classification_form import ClassificationForm


@app.route('/classifications_uploaded_image', methods=['GET', 'POST'])
def upload_image():
    """API for uploading an image and running a
    classification job. Returns the output scores from the
    model."""
    form = ClassificationForm()
    if request.method == "POST":
        # TODO:
        # Implement Uploaded Image API
        # Implement functions that process the uploaded image and return filename and path
        # filename, img_folder = image_processing()
        # then create a job that classifies the image

        # then returns the image classification output queue
        # return render_template("classification_uploaded_output_queue.html", image_id=filename,
        # jobID=task.get_id())
        return

    # otherwise, it is a get request and should return the
    # page for uploading images
    return render_template('classifications_uploading_images.html', form=form)
