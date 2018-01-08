import subprocess

def ping(hostname):
    (output, error) = subprocess.Popen('ping ' + hostname, 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print output, error

