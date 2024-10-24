steps = 0
def collatz(n):
    global steps
    if n == 1:
        #stops at 1
        print("It took",steps,"steps to get to 1!")
    elif n % 2 == 0:
        #even case
        steps += 1
        collatz(n//2)
    elif n % 2 == 1:
        #odd case
        steps += 1
        collatz(3*n+1)
number = int(input("""Input a number and I'll tell you how many steps it takes 
to get to 1 using the Collatz iterative process."""))
collatz(number)
