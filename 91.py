"""#№1
print("x y z")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x or y) <= (z == x)):
                print(x, y, z)
#№2
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x and not(y)) or (y == z)  or not(w)):
                    print(x, y, z, w)
#№3
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((z and y) or ((x <= z) == (y <= w))):
                    print(x, y, z, w)

#№4
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(not(x <= w) or (y == z) or y):
                    print(x, y, z, w)
#№5
print("a b c d")
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if not((not(a) and not(b)) or (b == c) or d):
                    print(a, b, c, d)

#№6
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x or not y) and not(w == z) and w:
                    print(x, y, z, w)
#№7
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((not x and not y) or (y == z) or not w):
                    print(x, y, z, w)
#№8
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x or y) <= (z and w)) and (x <= w):
                    print(x, y, z, w)
#№9
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x <= y) or (y == w)) and ((x or z) == w):
                    print(x, y, z, w)
#№10
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(y <= (x == w)) and (z <= x):
                    print(x, y, z, w)

#№11
for A in range(32):
    B = True
    for x in range(32):
        if ((x&25==0) or (x&9!=0) or (x&A!=0))==0:
            B=False
    if B:
        print(A)
        break
#№12
for A in range(32):
    B = True
    for x in range(32):
        if ((x&25==0) or (x&19!=0) or (x&A!=0))==0:
            B=False
    if B:
        print(A)
        break
#№13
for A in range(128):
    B = True 
    for x in range(128):
        if (x & 49 != 0 or (x & 28 == 0 or x & A != 0)) == 0:
            B=False
    if B:
        print(A)
        break
#№14
for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (3*x + 4*y != 70) or (a > x) or (a > y):
                k += 1
    if k == 90_000:
        print(a)
        break
#№15
for A in range(300, -1, -1):
    k = 0
    for x in range(300):
        for y in range(300):
            if (x * y < 100) or (y >= A) or (x > A):
                k += 1
    if k == 90_000:
        print(A)
        break
#№16
for A in range(300, -1, -1):
    k = 0
    for x in range(300):
        for y in range(300):
            if (x * y < 121) or (y > A) or (x >= A):
                k += 1
    if k == 90_000:
        print(A)
        break
#№17
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0))):
            k += 1
    if k == 999:
        print(a)
        break
#№18
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 18 != 0))):
            k += 1
    if k == 999:
        print(a)
        break
#№19
for a in range(100, 0, -1): 
    k = 0
    for x in range(1, 1000):
        if (90 % a == 0) and ((x % a != 0) <= ((x % 15 == 0) <= (x % 20 != 0))):
            k += 1
    if k == 999:
        print(a)
        break"""
"""27"""
#№1А
"""Ответ не правильный :(
file = open("27A1.txt")
n = int(file.readline())
a = []
for i in range(n):
    km,c = map(int, file.readline().split())
    p = c//100 if c%100==0 else c//100 + 1
    a.append([km, p])
min_cost = 10**20
numb = 0
for i in range(n):
    cost = 0
    for punkt in range(n):
        r = abs(a[i][0] - a[punkt][0])
        cost = cost + r * a[punkt][1]
    if cost < min_cost:  
        numb = a[i][1]
        min_cost	
print(numb)"""
#№1A
"""file = open("27A1.txt")
n = int(file.readline())

a = [0]*11_000_000
for i in range(n):
    km, c = map(int, file.readline().split())
    p = c // 100 if c%100==0 else c//100 + 1
    a[km] = p
sm = sum(a)
c=0
for i in range(11_000_000):
    c+= i*a[i]
m = 11**20
numb = 0

before = a[0]
for i in range(1,11_000_000):
    c = c + before - (sm-before)
    if a[i]>0 and c < m:
        m, numb = c, i
    before = before + a[i]
print(numb)"""
#№2A
"""f = open("27A2.txt")
n, m = map(int, f.readline().split())
a = []
s = 0
for i in range(n):
    km, p = map(int, f.readline().split())
    c = p//m if p%m==0 else p//m+1
    s += c
    a.append([km, c, s])
sm = s
#symma perevozki dlya 0 pynkta
s = 0
for i in range(n):
    s += (a[i][0]-a[0][0])*a[i][1]
mn = s
for i in range(1,n):
    r = a[i][0] - a[i-1][0]
    s = s + r*a[i-1][2] - r*(sm-a[i-1][2])
    mn = min(mn, s)
    
print(mn)"""
#№3A
"""f = open("27A3.txt")
n, v, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, p = map(int, f.readline().split())
    c = p//v if p%v==0 else p//v+1
    a.append([km, c])
a.sort()

st = end = 0
s = a[0][1]
curr = 0
while a[end+1][0] - a[curr][0] <= m:
    end+=1
    s+=a[end][1]
    
mx = s
for i in range(1,n):
    curr = i
    while end+1!=n-1 and a[end+1][0] - a[curr][0] <= m:
        end+=1
        s+= a[end][1]
    while a[curr][0] - a[st][0]>m:
        s-= a[st][1]
        st+=1
    mx = max(mx, s)
print(mx)"""
#№4
f = open("27A4.txt")
n = int(f.readline())
s, d = 0, float('inf')
for i in range(n):
    a, b = map(int, f.readline().split())
    if abs(a-b)%13:
        d = min(d, abs(a-b))
print(s) if s%13 else print(s-d)