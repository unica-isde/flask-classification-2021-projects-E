import redis
from rq import Connection, Queue
from config import Configuration


def get_task_from_queue(job_id):
    """
    This function returns a task from the queue, given the relative job_id.
    """

    redis_url = Configuration.REDIS_URL
    redis_conn = redis.from_url(redis_url)
    with Connection(redis_conn):
        q = Queue(name=Configuration.QUEUE)
        task = q.fetch_job(job_id)
        return task
