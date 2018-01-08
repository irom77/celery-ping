from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

import subprocess
@app.task
def ping(hostname):
    (output, error) = subprocess.Popen('/bin/ping ' + hostname, 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    print(output, error)