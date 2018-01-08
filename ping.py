import subprocess

def ping(hostname):
    (output, error) = subprocess.Popen('ping ' + hostname, 
    stdout=subprocess.STDOUT, stderr=subprocess.STDOUT, shell=True).communicate()
    print(output, error)

