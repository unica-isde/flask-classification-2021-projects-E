import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.histogram_form import HistogramForm
from ml.classification_utils import classify_image
from config import Configuration

config = Configuration()


@app.route('/image_histogram', methods=['GET', 'POST'])
def image_histogram():
    """API for picking one image from a list and returning the histogram of it.
    It calls the job queue to assign the task to worker."""
    form = HistogramForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data

        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        """
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "img_id": image_id
            })
            task = q.enqueue_job(job)
        """
        # returns the image classification output from the specified model
        # return render_template('classification_output.html', image_id=image_id, results=result_dict)
        #return render_template("classification_output_queue.html", image_id=image_id, jobID=task.get_id())
        return render_template("classification_output_queue.html", image_id=image_id)

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('histogram_select.html', form=form)
