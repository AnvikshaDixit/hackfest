import json
import math
import requests
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox
import numpy as np
from matplotlib.patches import Circle
import matplotlib.cbook as cbook
import time

def plotter():
	while True:
		print ("exec", time.time())
		try:
			URL="https://simplem.in:8443/meraki/all"
			r = requests.get(url=URL)
			data = r.json()
		except:
			file = open("data.json")
			data = json.load(file)

		img=plt.imread('floorplan.png')
		fig,ax = plt.subplots(1)
		ax.set_aspect('equal')
		ax.imshow(img[::-1], origin='lower')

		ap1=data[0]['data']['apMac']
		for i,j in enumerate(data):
			if i==0:
				continue
			else:
				if j['data']['apMac']==ap1:
					data=data[:i]
					break

		red = 0
		yellow = 0
		green = 0
		for ap in data:
			for i in range(0,len(ap["data"]["observations"])):
				for j in range(i+1,len(ap["data"]["observations"])):
					# if "Router" not in data["observations"][i]["os"] and "Router" not in data["observations"][j]["os"] :
					try:
						i_x = 60*float(ap["data"]["observations"][i]["location"]["x"][0])
						i_y = 30*float(ap["data"]["observations"][i]["location"]["y"][0])
						j_x = 60*float(ap["data"]["observations"][j]["location"]["x"][0])
						j_y = 30*float(ap["data"]["observations"][j]["location"]["y"][0])

						dis = math.dist([i_x, i_y],[j_x, j_y])
						mpt_x = (i_x+j_x)/2
						mpt_y = (i_y+j_y)/2
						if(ap["data"]["observations"][i]["clientMac"]!=ap["data"]["observations"][j]["clientMac"]):
							if dis < 2:
								red+=1
								circ=Circle((mpt_x, mpt_y),0.5, color = 'red')
								ax.add_patch(circ)
							elif dis < 4:
								yellow+=1
								circ=Circle((mpt_x, mpt_y),0.5, color = 'yellow')
								ax.add_patch(circ)
							else:
								green+=1
								circ=Circle((mpt_x, mpt_y),0.5, color = 'green')
								ax.add_patch(circ)
					except:
						print("Error:Null values")

		plt.savefig('.\\static\\assets\\img\\Devices-Meraki.png')

		print("red", red)
		print("yellow", yellow)
		print("green", green)
		# plt.show()
		time.sleep(300)





	    