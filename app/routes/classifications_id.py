from app import app
from app.utils.get_task_from_queue import get_task_from_queue
from config import Configuration

config = Configuration()


@app.route('/classifications/<string:job_id>', methods=['GET'])
def classifications_id(job_id):
    """Returns the status and the result of the job identified
    by the id specified in the path."""
    task = get_task_from_queue(job_id)

    response = {
        'task_status': task.get_status(),
        'data': task.result,
    }
    return response
