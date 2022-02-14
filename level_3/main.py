#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import pytesseract
url = 'http://158.69.76.135/level3.php'
url_captcha = 'http://158.69.76.135/captcha.php'
url_image = 'captcha.php'
ID = 22
votes = 0
error = 0
times = 1024
# ua = UserAgent SO Windows
ua = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36'
header = {'User-Agent': ua, 'Referer': url}
enter = requests.Session()
enter.headers.update(header)
print("Loading...\n")
for i in range(0, times):
    txt = enter.get(url, headers=header)
    soup = BeautifulSoup(txt.text, 'html.parser')
    code = soup.select('form > input[name="key"]')[0].get('value')

    fd = open("captcha.png", "wb")
    fd.write(enter.get(url_captcha, headers=header).content)
    fd.close()
    str_captcha = pytesseract.image_to_string("captcha.png")[:4]
    check = {'id': ID, 'holdthedoor': 'submit', 'key': code, 'captcha': str_captcha}
    resp = enter.post(url, data=check)
    if resp.status_code == 200:
        votes += 1
    else:
        error += 1
    print("URL->{}\n".format(url))
    print("Data inserted->\n{}\n".format(check))

percent = round(votes * 100/ times, 2)
print("--/\\/\\Scraping_Test/\\/\\--")
print("Success Cases: {}".format(votes))
print("Error Cases: {}".format(error))
print("{}% of the operation was successful\n".format(percent))
