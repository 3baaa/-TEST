'''
x=10
if x == 10:
  print('10입니다')
if x == 10:
  pass

x = 15
if x>=10:
  print('10 이상입니다.')

  if x==15:
    print('15입니다.')
  if x==20:
    print('20입니다.')

x=5
if x!=10:
  print('ok')

x=5
if x == 10:
  print('10입니다.')
else:
  print('10이 아닙니다.')

if True:
  print('참')
else:
  print('거짓')

if False:
  print('참')
else:
  print('거짓')

if None:
  print('참')
else:
  print('거짓')

x = 10
y = 20

if x == 10 and y == 20:
  print('참')
else:
  print('거짓')

x = 10
if x>0 and x<20:
  print('20보다 작은 양수입니다.')

written_test = 75
coding_test = True

if written_test>=80 and coding_test==True:
  print('합격')
else:
  print('불합격')

x=30
if x == 10:
  print('10입니다.')
elif x == 20:
  print('20입니다.')
else:
  print('10도 20도 아닙니다.')

x = int(input())
if 11<=x<=20:
  print('11~20')
elif 21<=x<=30:
  print('21~30')
else:
  print('아무것도 해당하지 않음')

for i in range(10,0,-1):
  print('Hello, world!',i)

for i in reversed(range(10)):
  print('Hello, world!',i)

a = [10,20,30,40,50]
for i in a:
  print(i)

x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
  print(i*10,end=' ')

i=3
while i > 0:
  print('Hello, world!',i)
  i -= 1

import random
#print(random.random())
#print(random.randint(1,6))

#i = 0
#while i != 3:
#  i = random.randint(1,6)
#  print(i)

dice = [1,2,3,4,5,6]
print(random.choice(dice))

i = 2
j = 5
while j>0:
  print(i,j)
  i*=2
  j-=1

i=0
while True:
  print(i)
  i+=1
  if i == 3:
    break

for i in range(3):
  print(i)
  if i == 3:
    break

for i in range(100):
  if i % 2 == 0 :
    continue
  print(i)

i = 0
while i < 100:
  i += 1
  if i%2==0:
    continue
  print(i)

i=0
while True:
  if i%10!=3:
    i+=1
    continue
  elif i>73 :
    break;
  print(i,end=' ')
  i+=1

for i in range(5):
  for j in range(5):
    print('*',end='')
  print()

for i in range(5):
  for j in range(5):
    if j<=i:
      print('*',end='')
  print()

for i in range(5):
  for j in range(5):
    if j == i:
      print('*',end='')
    else:
      print(' ',end='')
  print()

for i in range(5):
    for j in range(5):
      if i>j:
        print(' ',end='')
      else:
        print('*',end='')
    print()

for i in range(101):
  if i%3==0:
    print('Fizz')
  elif i%5==0:
    print('Buzz')
  elif i%3==0 and i%5==0:
    print('FizzBuzz')
  else:
    print(i)

for i in range(1,101):
  print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i)

for i in range(1, 101):
  if i%2==0 and i%11==0:
    print('FizzBuzz')
  elif i%2==0:
    print('Fizz')
  elif i%11==0:
    print('Buzz')
  else:
    print(i)

a = [10, 20, 30]
a.append(500)
print(a)
a.append([500,600])
print(a)
a.extend([500,600])
print(a)

a=[10,20,30]
a.insert(2,500)
print(a)
a.insert(0,500)
print(a)

a=[10,20,30]
a[1:1]=[500,600]
print(a)

a=[10,20,30]
print(a.pop(1))
print(a)

from collections import deque
a = deque([10,20,30])
print(a)
a.append(500)
print(a)
print(a.popleft())
print(a)

a=[10,20,30,15,20,40]
print(a.index(20))
print(a.count(20))
print(a.reverse())
print(a)
print(sorted(a))
print(a.sort())
print(a)
#del a[:]
#print(a)
a.clear()
print(a)

a=[10,20,30]
a[len(a):]=[500,600]
print(a)

a = [38,21,53,62,19]
for i in a:
  print(i)
i=0
while i < len(a):
  print(a[i])
  i+=1
'''