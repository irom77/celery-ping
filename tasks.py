from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

import delegator
@app.task
def ping(hostname):
    """
    (output, error) = subprocess.Popen(['ping', '-c 2', hostname], 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() # , shell=True
    print(output, error)
    """
    c = delegator.run('ping -n 2 ' + hostname, block=False)
    return c
