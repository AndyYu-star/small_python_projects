#solution to APPS 293 (from https://youtu.be/0pgEMWy70Qk?&t=403)

#maths stuff:
"""
The number of squares with side length 1 is mn. The number of squares with
side length 2 is (m-1)(n-1), then (m-2)(n-2) for side length 3 and so on.

Let m >= n. Then x = mn + (m-1)(n-1) + (m-2)(n-2) + ... + (m-n+1)(n-n+1).

There are n terms being added here. Expanding and collecting like terms gives:
x = mn^2 - (m+n)(1+2+...+n-1) + 1+4+9+...+(n-1)^2

The sum of the first (n-1) integers is n(n-1)/2, and the sum of the first (n-1)
square numbers is n(n-1)(2n-1)/6.

So now we have:
x = mn^2 - n(n-1)(m+n)/2 + n(n-1)(2n-1)/6.

Expanding and simplifying this gets:
x = (mn^2)/2 + mn/2 - (n^3)/6 + n/6

Rearranging this to make m the subject, we have:
m = (6x/(n(n+1)) + n-1)/3

We can simply check if a valid m exists for values of n. m is at minimum equal
to n, and in this case x = n(n+1)(2n+1)/6 (the sum of squares from 1 to n^2),
so we only need to check n from 1 until n(n+1)(2n+1)/6 exceeds x.
"""

def find_m(x, n):
    if (6*x) % (n*(n+1)) == 0 and (6*x//n//(n+1) + n-1) % 3 == 0:
        return (6*x//n//(n+1) + n-1)//3
    else:
        return -1 #m can't exist in this case since it must be an integer

def num_squares(m, n): #only used for checking
    total = 0
    while m > 0 and n > 0:
        total += m*n
        m -= 1
        n -= 1
    return total

x = int(input("x: "))
n = 1
solutions = []
while n*(n+1)*(2*n+1) <= 6*x:
    m = find_m(x, n)
    if m >= n: #the formula is only valid when m >= n
        solutions.append([m, n])
        if m != n:
            solutions.append([n, m])
    n += 1

print(solutions)

for s in solutions:
    assert x == num_squares(s[0], s[1])
