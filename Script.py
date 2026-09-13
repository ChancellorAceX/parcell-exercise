# Script
import re
import requests
url = 'https://ftis.org/'
response = requests.get(url+'Posts.aspx')
if response.status_code == 200:
    print('response received')
    data = response.text
else:
    print(f'Failed to get: {response.status_code}')


Titles = re.findall(r'(?<=\d_lb_name">).+(?=</span>)', data)
# print(Titles)

IDs = re.findall(r'(?<=javascript:return DownloadFile\(&quot;).+(?=&quot;\))', data)
# print(IDs)
GoodIDs = []
for id in IDs:
    GoodIDs.append(id.replace('#','A'))
# print(GoodIDs)

links = []
for id in GoodIDs:
    links.append(url+'PostFileDownload.aspx?id='+id)
print(links)
    
    
  