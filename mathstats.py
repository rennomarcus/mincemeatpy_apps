import mincemeat
import numpy as np
import math
from sys import argv

file = open(argv[1], 'r')
data = list(file)
file.close()



datasource = {}
size = len(data)
slice_data = 200

size = int(math.ceil(float(size) / slice_data))

for i in range(size):
    datasource[i] = data[i*slice_data:(i+1)*slice_data]


def mapfn(k, v):
    import numpy as np
    count = len(v)
    numbers = np.empty(count)
    for i, x in enumerate(v):
        numbers[i] = int(x.strip())
    squared_n = numbers**2
    squared_n = numbers.mean()
    
    squared_m = numbers.mean()
    squared_m = squared_m**2
    total = sum(numbers)    
    yield 'count',  count
    yield 'total',  total
    yield 'means',  ( squared_n, squared_m )
    
#sqrt( mean( x**2 ) - mean(x) )            
def reducefn(k, vs):
    if k == 'count':
        return sum(vs)
    if k == 'total':
        return sum(vs)
    if k == 'means':
        vs = zip(*vs)
        size= len(vs[0])
        all_mean_2 = sum(vs[0])/size
        all_mean = sum(vs[1])/size
        if all_mean_2 > all_mean:
            return(all_mean_2 - all_mean)**0.5
        return(all_mean - all_mean_2)**0.5
    return  0
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

stats = []
stats.append(results['count'])
stats.append(results['total'])
stats.append(results['means'])
print 'Count: {0}\nSum {1}\nStd.dev {2} \n'.format(stats[0],  stats[1],  stats[2])
    
