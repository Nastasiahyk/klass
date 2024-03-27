
#Задание23
e = 10**-6
a = int(input())
n = 1 
x =[]
if a <=10:
    x.append(min(2*a,0.95))
elif 1<a<25:
    x.append(a/5)
else:
    x.append(a/25)
x.append(4/5*x[n-1]+a/(5*x[n-1]**4))
while 5/4*a*(abs(x[n]-x[n-1]))<e:
    n+=1
    x.append(4/5*x[n-1]+a/(5*x[n-1]**4))
print(x[n])
#Задание24
from math import sqrt
e = int(input())
n = 1
a = [0]
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
n+=1
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
while abs(a[n]-a[n-1])<e:
    a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
print(a[n])
