import numpy as np
from datetime import datetime

f = open('data.csv', 'r')

output=[]
compliant_count = 0
non_compliant_count = 0
data=[]

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

    data.append(list((foia_num,request_date,execute_date)))

f.close()


A = [d[1].date() for d in data]
B = [d[2].date() for d in data]
delta_bdays = np.busday_count(A,B)

for i in xrange(0,len(data)):
    #Give CPD the benefit of the doubt
    compliant = True
    if(delta_bdays[i] > 5):
        compliant = False
        non_compliant_count += 1
    else:
        compliant_count += 1

    output.append(list([data[i][0],
                       data[i][1].strftime('%Y-%m-%d'),
                       data[i][2].strftime('%Y-%m-%d'),
                        delta_bdays[i],
                       compliant]))

#print "foia,request_date,due_dat,execute_dat,delta_days,compliant"
for out in output:
    print out

print "compliant: ",compliant_count,\
    " Non Compliant >5 days: ", non_compliant_count,\
    " Percent violated: ", non_compliant_count*100.0/(compliant_count+non_compliant_count)
