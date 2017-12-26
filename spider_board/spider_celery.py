from celery import Celery

app = Celery('spider_task', broker='redis://localhost:6379/10', backend='redis://localhost:6379/11')