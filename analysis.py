import pandas as pd
import csv
import datetime

from datetime import datetime
from pandas.tseries.offsets import *

f = open('data.csv', 'r')
#tuple of foianum, requestdate, duedate, executeddate, deltadays, compliant
output=[]
compliant_count = 0
non_compliant_count = 0
for line in f:
    l = line.split(',')
    foia_num = l[1]

    # null entries
    if not l[0]:
        l[0] = '01-Jan-00'
    request_date = datetime.strptime(l[0], '%d-%b-%y')

    # Some never get filled
    if not l[2]:
        l[2] = '31-Dec-99'
    execute_date = datetime.strptime(l[2], '%d-%b-%y')

    # 5 business days to complete request
    due_date = request_date + BDay(5)

    delta_days = execute_date - request_date
    #Give CPD the benefit of the doubt
    compliant = True
    if(delta_days.days > 5):
        compliant = False
        non_compliant_count+=1
    else:
        compliant_count+=1

    output.append(tuple( (foia_num,
                        request_date.strftime("%Y-%m-%d"),
                        due_date.strftime("%Y-%m-%d"),
                        execute_date.strftime("%Y-%m-%d"),
                        delta_days.days,
                        compliant) ))

f.close()

for a,b,c,d,e,f in output:
    #print a,b,c,d,e,f
    print a,e,f

print "compliant: ",compliant_count,\
    " Non Compliant >5 days: ", non_compliant_count
