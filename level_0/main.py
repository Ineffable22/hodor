#!/usr/bin/python3
import requests
ID = 22
vote = 0
url = 'http://158.69.76.135/level0.php'
check = {'id' : ID, 'holdthedoor': 'submit'}
for i in range(0, 1024):
    resp = requests.post(url, data=check)
    if resp.status_code == 200:
        vote += 1
        print(vote)
