import requests
import json
import sys
from utils import *





if __name__ == "__main__":
    print("running latencies_to_CSV.py...")
    
    # get mapping between regions codes and names
    regions_dict = get_regions_names('all_regions')
    

    # API call to get latencies
    URL = "https://api.cloudping.co/averages"
    r = requests.get(URL)
    regions = []


    for reg in r.json():
        regions.append(reg["region"])    
    

#
#    # Defualt: select all regions from cloudping.co
#    if len(sys.argv) == 1:
#        selected_regions = regions
#    elif len(sys.argv) == 2 and sys.argv[1] == "-s":
#        selected_regions = list(REGIONS_NAMES.keys())
#        print(">>", selected_regions)
#        b_selected = True
#    else:
#        print("Usage: python3 " + sys.argv[0] + "[-s]\n\t-s: selected regions")
#        sys.exit(1)

    # writing to the output file
    with open("latencies.csv", "w") as fd:
        # writing the header of the file
        for i, region in enumerate(regions):
            if i == 0:
                fd.write(regions_dict[region])
            else:    
                fd.write("," + regions_dict[region])
        fd.write("\n")
        
        # Writing the rows of data
        for index1, reg in enumerate(r.json()):
            assert(reg["region"] == regions[index1])
            # write the first column of the row
            #   which consists of the name of the region 
            fd.write(regions_dict[regions[index1]])
            for index2 , avg in enumerate(reg["averages"]):
                assert(avg["regionTo"] == regions[index2])
                fd.write("," + str(int(avg["average"])))
            fd.write("\n")
    


    print("end of latencies_to_csv.py...")
    
