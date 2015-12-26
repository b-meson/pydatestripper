import pandas as pd
import csv
#import time
#import pytz
import datetime

from datetime import datetime
from pandas.tseries.offsets import *

f = open('data.csv', 'r')

requested = []
completed = []
# initialize the array before we use it with zeros 
duedate= [0]*15755
for line in f:
    Request= line.split(",")
    requested.append(Request[0])
    completed.append(Request[2])

for i in range(len(requested)):
    duedate[i]=datetime.strptime(requested[i], '%d-%b-%y') + BDay(5)
    print duedate[i]
