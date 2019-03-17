#!/usr/bin/env python3

import requests

from celery import Celery

app = Celery(__name__, broker="amqp://celery:celery123@localhost:5672", backend="redis://localhost")


@app.task
def request_163():
	req = requests.get("https://www.163.com")
	print(req.text)
	
	