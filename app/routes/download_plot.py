import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Response

from app import app
from app.utils.get_task_from_queue import get_task_from_queue
from config import Configuration

config = Configuration()


@app.route('/download_plot/<string:job_id>', methods=['GET'])
def download_plot(job_id=None):
    """Returns a JSON file with the results."""

    # data can be kept as bytes in an in-memory buffer
    output = io.BytesIO()

    if job_id is not None:
        task = get_task_from_queue(job_id)

        # get the result as json
        result = dict(task.result)

        # get data from the result of the task
        labels = list(result.keys())
        data = list(result.values())

        # make the plot canvas
        fig, ax = plt.subplots()

        # fill plot
        ax.barh(labels, data, align='center')
        ax.invert_yaxis()  # labels read top-to-bottom

        # save the plot in the memory buffer
        FigureCanvas(fig).print_png(output)

    return Response(
        output.getvalue(),
        mimetype="image/png",
        headers={"Content-disposition": "attachment; filename=result_plot.png"})
