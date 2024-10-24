import random
MAX_LAYERS = 50
SAMPLES = 500
layers = 0
def approximate(polynomial,derivative,guess):
    #approximates a single root recursively using the Newton-Raphson method
    y = 0
    for exp in range(len(polynomial)):
        #evaluates the polynomial at 'guess'
        y += guess ** exp * polynomial[exp]
    m = 0
    for exp in range(len(derivative)):
        #evaluates the derivative (finds the slope) at 'guess'
        m += guess ** exp * derivative[exp]
    if m == 0:
        #in case a division by 0 error is incoming, this stops that
        m = random.choice([0.01,-0.01])
    #sets the new guess based on the slope and the y coordinate
    guess -= y / m
    #keeps track of the number of layers made so it doesn't loop forever
    global layers
    global MAX_LAYERS
    layers += 1
    #only continues if it hasn't reached the maximum amount of layers
    if layers < MAX_LAYERS:
        return approximate(polynomial,derivative,guess)
    else:
        return guess

print("Welcome to the polynomial roots approximator! You give me a polynomial, and I will (try to) find all its roots!")
print("Enter only integer coefficients of a polynomial from lowest order to highest order, with spaces separating each.")
polynomial = input("(e.g. 3x^3 + 2x^2 - 37x + 12 would be 12 -37 2 3 )").split()
for i in range(len(polynomial)):
    #turns everything into an integer
    polynomial[i] = int(polynomial[i])
derivative = []
for exp in range(1,len(polynomial)):
    #getting the derivative of the polynomial
    derivative.append(polynomial[exp]*exp)
lowest = polynomial[0]
highest = polynomial[0]
#finds the lowest and highest coefficients (to set the boundaries of where to search)
for coefficient in polynomial[1:]:
    if coefficient < lowest:
        lowest = coefficient
    elif coefficient > highest:
        highest = coefficient
#finds all roots by searching a range of values
roots = []
for i in range(SAMPLES):
    #random guess in the range set (the range here is a bit larger in case a solution is right on the edge)
    real = random.uniform(-5-abs(lowest),6+abs(highest))
    imaginary = random.uniform(-5-abs(lowest),6+abs(highest))
    guess = complex(real,imaginary)
    result = approximate(polynomial,derivative,guess+0.01)
    #rounds the result by rounding its real and imag components before combining
    result = round(result.real,2) + round(result.imag,2) * complex(0,1)
    layers = 0
    if not result in roots:
        #only adds it if the root is new
        if result.imag == 0.0:
            #adds only the real component if the imaginary component is nonexistent
            roots.append(result.real)
        else:
            roots.append(result)
if len(roots) == 1:
    print(roots[0],"was the root that I found!")
else:
    print(roots,"were the roots that I found!")
if len(roots) >= len(polynomial):
    print("Hm, that's too many roots! I think the polynomial you gave me actually has no roots! Or maybe I'm wrong, haha.")
