import math
def f(x,r):
    return (1 + r**2 - 2*r*math.cos((1-(r ** (-1.5))) * 2 * math.pi * x)) ** 0.5

distances = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]
sample_nums = [4,10,50]
us = distances[2]

#rectangles
for d in distances:
    if d != us:
        r = d/us
        for n in sample_nums:
            total = 0
            for k in range(n):
                total += f(k * (r**1.5) / n / abs(r**1.5 - 1), r)
            total = total / n
            print(total)
        print()

#trapeziums
for d in distances:
    if d != us:
        r = d/us
        for n in sample_nums:
            total = f(0,r) + f(r**1.5 / abs(r**1.5 - 1), r)
            for k in range(1,n):
                total += 2 * f(k * (r**1.5) / n / abs(r**1.5 - 1), r)
            total = total / 2 / n
            print(total)
        print()
        
#simpson's
for d in distances:
    if d != us:
        r = d/us
        for n in sample_nums:
            total = f(0,r) + f(r**1.5 / abs(r**1.5 - 1), r)
            for j in range(1,(n//2)+1):
                total += 4 * f((2*j - 1) * (r**1.5) / n / abs(r**1.5 - 1), r)
            for k in range(1,n//2):
                total += 2 * f(2 * k * (r**1.5) / n / abs(r**1.5 - 1), r)
            total = total / 3 / n
            print(total)
        print()
