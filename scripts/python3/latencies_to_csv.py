import requests
import json
import sys



if __name__ == "__main__":

	try:
		REGIONS_NAMES = json.load(open("regions.json", "r"))

	except Exception as e:
		print(e)

	URL = "https://api.cloudping.co/averages"
	r = requests.get(URL)
	regions = []
	b_selected = False


	for reg in r.json():
		regions.append(reg["region"])	

	if len(sys.argv) == 1:
		selected_regions = regions
	elif len(sys.argv) == 2 and sys.argv[1] == "-s":
		selected_regions = list(REGIONS_NAMES.keys())
		print(">>", selected_regions)
		b_selected = True
	else:
		print("Usage: python3 " + sys.argv[0] + "[-s]\n\t-s: selected regions")
		sys.exit(1)

	with open("latencies.csv", "w") as fd:
		for region in regions:
			if region not in selected_regions:
				continue
			if b_selected:
				fd.write("," + REGIONS_NAMES[region])
			else:
				fd.write("," + region)
		fd.write("\n")

		for index1, reg in enumerate(r.json()):
			if reg["region"] not in selected_regions:
				continue
			assert(reg["region"] == regions[index1])
			if b_selected:
				fd.write(REGIONS_NAMES[regions[index1]])
			else:
				fd.write(regions[index1])
			for index2 , avg in enumerate(reg["averages"]):
				if avg["regionTo"] not in selected_regions:
					continue
				assert(avg["regionTo"] == regions[index2])
				fd.write("," + str(int(avg["average"])))
			fd.write("\n")
					


		 

	 
