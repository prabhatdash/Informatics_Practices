#to find the value of                                     a**b(2**c/b/a)**2/7-d+cos(a)
import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=float(input("d:"))
x=a**b
u=b/a
y=(2**c)/u
i=2/7
o=y**i
m=x*o-d+math.cos(a)
print(m)
