import requests
import json
URL="https://simplem.in:8443/meraki/all"
r=requests.get(url=URL)
dat=r.json()
te=dat[0]
print(type(te))
v=te['data']['apMac']
print(v,"apMac")
text=json.dumps(dat,sort_keys=True, indent=4)
with open(r'location1.txt','w') as f:
    f.write(text)
for i,j in enumerate(dat):
	print(i)
	print(type(i))
	print(j)
	print(type(j))
	if i==0:
		continue
	else:
		if j['data']['apMac']==v:
			print(j['data']['apMac'])
			print(i)
			dat=dat[:i]
			break

text=json.dumps(dat,sort_keys=True, indent=4)
with open(r'location.txt','w') as f:
    f.write(text)