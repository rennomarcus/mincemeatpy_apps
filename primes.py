import mincemeat
import numpy as np

size = 10*1000*1000

def eliminate_numbers(num):
    if num%2 == 0:
        return True
    if num%3 == 0:
        return True
    if num%5 == 0:
        return True
    return False
    
def is_palindrome(data):
    if eliminate_numbers(data):
        return False
    str_num = str(data)
    digits = str_num.strip()
    size = len(digits)
    half = size/2
    part1 = digits[0:half]
    if size %2 != 0:
        part2 = digits[:half:-1]
    else:
        part2 = digits[:half-1:-1]
    if part1 == part2:
        return True
    return False
    
data = []
data1 = []
data2 = []
data3 = []
data4 = []
count = 0
for i in range(2,  size):
    count += 1
    if is_palindrome(i):
        if count == 1:
            data1.append(i)
        if count == 2:
            data1.append(i)
        if count == 3:
            data1.append(i)
        if count == 4:
            data1.append(i)
    if count == 4:
        count = 0

data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)

datasource = dict(enumerate(data))

def mapfn(k, v):
    total = len(v)
    for i in range(total):
        number = v[i]
        isprime = True
        redundancy = number**0.5 #after this number repetition occurs 
        j = 5
        while j*j < redundancy:
            if number % j == 0 or number % (j + 2) == 0:
                isprime = False
                break
            j += 6
        if isprime:
            yield number,  1
            
def reducefn(k, vs):
    return k
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print "result"

primes = [2, 3, 5]

for i in results.keys():
    primes.append(i)

print sorted(primes)
