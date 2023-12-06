import os
import pandas as pd


curDir = os.path.dirname(os.path.abspath(__file__))
dir=os.path.join(curDir,"../App")
dat1=dir + "/CSVTEST.txt"
data = pd.read_csv(dat1)

print(data[1][1])