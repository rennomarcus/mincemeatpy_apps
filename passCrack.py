#!/usr/bin/env python
import mincemeat
import hashlib
import sys

data = sys.argv[1]

datasource = {1: data }

def mapfn(k, v):
    def convert(n):
        if n > 25:
            return unichr(48 + n -26).encode("utf-8")
        else:
           return unichr(97 + n).encode("utf-8")

    def check_pass(d):
        if d == v:
            return True
        else:
            return False

    for i in range(36):
        m = hashlib.md5(convert(i))
        data = m.hexdigest()[0:5]
        if check_pass(data):
            yield convert(i), 1
        for j in range(36):
            m2 = hashlib.md5(convert(i) + convert(j))
            data2 = m2.hexdigest()[0:5]
            if check_pass(data2):
                yield  convert(i) + convert(j), 1
            for z in range(36):
                m3 = hashlib.md5(convert(i) + convert(j) + convert(z))
                data3 = m3.hexdigest()[0:5]
                if check_pass(data3):
                    yield  convert(i) + convert(j) + convert(z), 1
                for w in range(36):
                    m4 = hashlib.md5(convert(i) + convert(j) + convert(z) + convert(w))
                    data4 = m4.hexdigest()[0:5]
                    if check_pass(data4):
                        yield  convert(i) + convert(j) + convert(z) + convert(w), 1


def reducefn(k, vs):
    return k

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

found = []
for i in results.keys():
    found.append(i)
found = sorted(found)
print("Found:" + str(found))
