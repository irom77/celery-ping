import subprocess

def ping(hostname):
    (output, error) = subprocess.Popen(['ping', '-c 2',hostname], 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() # , shell=True
    print(output, error)

