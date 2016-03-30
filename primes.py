import mincemeat
import numpy as np

size = 10*1000*1000



def eliminate_number(num):
    if num%3 == 0:
        return True
    if num%5 == 0:
        return True
    return False
   
data = [[] for x in range(10)]

count = 0
for i in range(7,  size, 2): #step 2 so i can eliminate all evens
    if  not eliminate_number(i):
        data[count].append(i)
        count += 1
        count = count %10
    

datasource = dict(enumerate(data))

def mapfn(k, v):    
    def is_palindrome(data):
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
        
    total = len(v)
    for i in range(total):
        if is_palindrome(v[i]):
            number = v[i]
            isprime = True
            redundancy = number**0.5 #after this number repetition occurs 
            j = 5
            while j*j <= number and j <= redundancy:
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
print "Length" + str(len(primes))
print "Sum" + str(sum(primes))
