import delegator

def ping(hostname):
    c = delegator.run('ping -c 1 -W 1 ' + hostname, block=False) # -W 1
    c.block()
    return c.return_code

