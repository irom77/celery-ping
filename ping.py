import delegator

def ping(hostname):
    c = delegator.run('ping -c 2 ' + hostname, block=False)
    c.block()
    return c.return_code

