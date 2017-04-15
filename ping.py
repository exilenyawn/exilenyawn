import urllib.request
import time

def ping():
    data = urllib.request.urlopen("http://python15-delta213.rhcloud.com/").read()
    return data

while True:
    ping()
    print("ping")
    time.sleep(6000)
