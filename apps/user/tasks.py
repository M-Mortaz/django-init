from celery import shared_task


@shared_task
def inform_celery_is_ready():
    print("celery is working!")


inform_celery_is_ready.delay()
