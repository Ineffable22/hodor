#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
url = 'http://158.69.76.135/level2.php'
ID = 22
votes = 0
error = 0
times = 1024
# ua = UserAgent SO Windows
ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36"
print("Loading...\n")
for i in range(0, times):
    enter = requests.Session()
    txt = enter.get(url)
    soup = BeautifulSoup(txt.text, 'html.parser')
    code = soup.select('form > input[name="key"]')[0].get('value')
    check = {'id': ID, 'holdthedoor': 'submit', 'key': code}
    header = {'User-Agent': ua, 'Referer': url}
    resp = enter.post(url, data=check, headers=header)
    if resp.status_code == 200:
        votes += 1
    else:
        error += 1

percent = round(votes * 100/ times, 2)
print("--/\\/\\Scraping_Test/\\/\\--")
print("Success Cases: {}".format(votes))
print("Error Cases: {}".format(error))
print("{}% of the operation was successful\n".format(percent))
