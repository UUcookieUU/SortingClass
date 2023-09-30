from itertools import count
import re
from typing import Any, Counter

a = [1, 45, 24 ,125,23 ,25,26,289,41252,0,2423]

class Sorting: 
    def __init__(self):
        self.data = []
    def __call__(self,newvalue):
        self.data.append(newvalue)
        for u in range(len(self.data)):
            for i in range(len(self.data)-1): # length
                if self.data[i+1] < self.data[i]:
                    var1 = self.data[i]
                    self.data[i] = self.data[i+1]
                    self.data[i+1] = var1
        return self.data
sort = Sorting()
for i1 in a:
    if i1 == a[len(a)-1]:
        print(sort(i1))
    else:
        sort(i1)

