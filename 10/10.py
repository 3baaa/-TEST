'''
a = [1,2,3,4,5,6,3,3]
r_set = {3,5}

result = [i for i in a if i not in r_set]
print(result)

a = 'aaa'
print(a*2)

import math
print(math.sqrt(25))

import math as m
print(m.sqrt(25))

from math import sqrt
print(sqrt(25))

from math import *
print(pi)
print(sqrt(25))

from math import sqrt as s
print(s(25))

import urllib.request as r
resp=r.urlopen('http://www.google.co.kr')
print(resp.status)

import s2

print(s2.b)
print(s2.s(10))

from s2 import b,s
print(b)
print(s(10))

import person
m = person.Person('마','2','서')
m.greeting()

from person import Person as p
m = p('마',2,'서')
m.greeting()

import hello
print('main.py __name__:',__name__)

import calcp.operation
import calcp.geometry
print(calcp.operation.add(10,20))
print(calcp.operation.mul(10,20))
print(calcp.geometry.tri_area(30,40))
print(calcp.geometry.rect_area(30,40))

from calcp.operation import add, mul
print(add(10,20))
print(mul(10,20))

import sys
print(sys.path)

import sys
data=sys.stdin.readline().rstrip()
print(data)

r = min([1,2,3])
print(3)

r = eval('(3+5) * 7')
print(r)

from itertools import permutations

data = ['A','B','C']
r = list(permutations(data,3))
print(r)

from itertools import combinations

data = ['A','B','C']
r = list(combinations(data,2))

print(r)

from itertools import product

data = ['A','B','C']
r = list(product(data,repeat=2) )

print(r)

from itertools import combinations_with_replacement
data = ['A','B','C']
r = list(combinations_with_replacement(data,2))
print(r)

import heapq

def heapsort(i):
  h = []
  result = []
  for value in i:
    heapq.heappush(h,value)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

import heapq

heap = []
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
print(heapq.heappop(heap))
print(heap)

import heapq

def heapsort(i):
  h = []
  result = []
  for value in i:
    heapq.heappush(h,-value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

from bisect import bisect_left,bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

from bisect import bisect_left,bisect_right

def count_by_range(a,left_v,right_v):
  right_i = bisect_right(a,right_v)
  left_i = bisect_left(a,left_v)
  return right_i-left_i

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

from collections import Counter
counter = Counter(['r','b','r','g','b','b'])

print(counter['b'])
print(counter['g'])
print(counter)
print(dict(counter))

import math

print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(math.pi)
print(math.e)
'''