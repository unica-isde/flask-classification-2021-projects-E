from flask import Response, json

from app import app
from app.utils.get_task_from_queue import get_task_from_queue
from config import Configuration

config = Configuration()


@app.route('/download_result/<string:job_id>', methods=['GET'])
def download_results(job_id=None):
    """Returns a JSON file with the results."""

    # default output
    result = {'Error': 'Result has expired'}

    if job_id is not None:
        task = get_task_from_queue(job_id)

        # get the result as json
        result = dict(task.result)

    return Response(
        json.dumps(result),
        mimetype="text/json",
        headers={"Content-disposition": "attachment; filename=result.json"})
