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
    c = delegator.run('ping -c 2 -w 1' + hostname, block=False)
    return c

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('pairs', type=str, nargs='+')
    args = parser.parse_args()

    results = [ping.delay(pair) for pair in args.pairs]
    for result in results:
        pair, rate = result.get()
        print(pair, rate)