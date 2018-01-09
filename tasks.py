from celery import Celery
# import config
import delegator

app = Celery('tasks')
app.config_from_object('config')

@app.task
def add(x, y):
    return x + y


@app.task
def ping(hostname):
    """
    (output, error) = subprocess.Popen(['ping', '-c 2', hostname], 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() # , shell=True
    print(output, error)
    """
    c = delegator.run('ping -c 1 -W 1 ' + hostname, block=False) # -W 1
    c.block()
    return c.return_code

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('hosts', type=str, nargs='+')
    args = parser.parse_args()

    results = [ping.delay(host) for host in args.hosts]
    for result in results:
        return_code = result.get()
        print(return_code)