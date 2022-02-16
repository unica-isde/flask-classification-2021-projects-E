import redis
from flask import request, render_template, redirect
from rq import Connection, Queue
from rq.job import Job
from app import app
from app.forms.classification_form import ClassificationForm
from app.utils.image_processing import image_processing, valid_image
from ml.classification_utils import classify_image
from config import Configuration


@app.route('/classifications_uploaded_image', methods=['GET', 'POST'])
def upload_file():
    """API for upload an image and running a
    classification job. Returns the output scores from the
    model."""
    form = ClassificationForm()
    if request.method == "POST":

        if 'image' not in request.files:
            return redirect(request.url)
        image = request.files['image']
        if not valid_image(image):
            return redirect(request.url)

        filename, img_folder = image_processing(image)

        model_id = form.model.data
        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "model_id": model_id,
                "img_id": filename,
                "path": img_folder
            })
            task = q.enqueue_job(job)

            # returns the uploaded image classification output from the specified model
            return render_template("classification_uploaded_output_queue.html", image_id=filename,
                                   jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # page for uploading images
    return render_template('classifications_uploading_images.html', form=form)
