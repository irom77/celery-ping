import subprocess

def ping(hostname):
    (output, error) = subprocess.Popen('ping ' + hostname, 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    print(output, error)

