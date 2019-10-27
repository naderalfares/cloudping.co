import requests
import json
import sys

if __name__ == "__main__":
	URL = "https://api.cloudping.co/averages"
	r = requests.get(URL)
	regions = []
	for reg in r.json():
		regions.append(reg["region"])	

	if len(sys.argv) == 1:
		selected_regions = regions
	elif sys.argv[1] == -1:
		# add the selcted regions here
		selected_regions = []
	else:
		print("Usage: python3 " + sys.argv[0] + "[-s]\n\t-s: selected regions hardcoded in the script")
		sys.exit(1)

	with open("latencies.csv", "w") as fd:
		for region in regions:
			if reg["region"] not in selected_regions:
				continue
			fd.write("," + region)
		fd.write("\n")

		for index1, reg in enumerate(r.json()):
			if reg["region"] not in selected_regions:
				continue
			assert(reg["region"] == regions[index1])
			fd.write(regions[index1])
			for index2 , avg in enumerate(reg["averages"]):
				if reg["region"] not in selected_regions:
					continue
				assert(avg["regionTo"] == regions[index2])
				fd.write("," + str(int(avg["average"])))
			fd.write("\n")
					


		 

	 
