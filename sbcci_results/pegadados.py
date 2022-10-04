#!/bin/env python3


file = open('results.txt','r')
data = file.read()
data = data.split('\n')
file.close()

q = []
for i in range(1000):
    q.append('_%d'%i)

m = {}

for l in data:
    if len(l) > 0:
        d = l.split(' ')
        #print(d[0][-3:])
        if 'cpu' in d[0] and 'one_hop' in d[0]:
            #for h in q:
                #if d[0][-3:] == h or d[0][-2:] == h:
            n = d[0].split('_')[0]
            p = float(d[-1].replace('%',''))
            if n not in m:
                m[n] = p
            else:
                m[n] = max(m[n],p)


print(m)

