# Script
import re
import requests
import json
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
    
# TIME LIMIT SEPARATOR

pos = re.finditer('lessons',data)
indeces = []
for val in pos:
  indeces.append(val.start())
indeces=indeces[1:]

counts = [0]
pattern = re.compile(r'javascript:return DownloadFile')
for index, val in enumerate(indeces):
  if index == len(indeces)-1:
    count = len(pattern.findall(data,val))
  else:
    count = len(pattern.findall(data,val,indeces[index+1]))
  counts.append(count)

dictionary = {}
for n, t in enumerate(Titles):
  dictionary[t]=links[counts[n]:sum(counts[0:n+2])]

with open('config.json','w') as f:
  json.dump(dictionary,f,indent=4)

print('config.json created using dicitonary data')