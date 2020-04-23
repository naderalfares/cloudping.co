import json
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    
    regions = []
    latencies = []
    with open("latencies.csv", "r") as fd:
        for i, line in enumerate(fd):
            if i == 0:
                regions = line.strip("\n").split(",")
            else:
                latencies.append([ int(ele) for ele in line.strip("\n").split(",")[1:]])

    #print(regions)
    #for ele in latencies:
    #    print(ele)

    df = pd.read_csv("latencies.csv")
    print(df.head)
     
