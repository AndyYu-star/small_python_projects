def sieve(maximum, num_factors, exclusive):
    
    #creates the numbers and the # of factors counted for each number
    #all numbers get 2 factors from the start (1&itself), except for 1, which gets just 1
    nums = list(range(1, maximum+1))
    factors = [2] * maximum
    factors[0] = 1
    
    #cycles through each divisor and number, increasing their # of factors
    #this ignores divisors that are more than the square root of the maximum
    for divisor in range(2, int(maximum**0.5)+1):
        #increments it by 2 because it starts from 1 + the square of the divisor
        #this means pairs of factors are counted together, which is more efficient
        for i in range(divisor**2 - 1, maximum, divisor):
            factors[i] += 2
        #decreases the # of factors of the square of divisor manually, to account for the duplicated factor
        factors[divisor**2 - 1] -= 1
            
    if exclusive:
        #deletes all numbers that don't have exactly 'num_factors' factors
        for i in range(maximum-1, -1, -1):
            if factors[i] != num_factors:
                del nums[i]
    else:
        #deletes all numbers that have more factors than num_factors
        for i in range(maximum-1, -1, -1):
            if factors[i] > num_factors:
                del nums[i]
    return nums

print("Welcome to the sieve of Eratosthenes! (but better!)")
maximum = int(input("What is the highest number you want it to go to? "))
num_factors = int(input("How many factors should the numbers have at maximum? (Enter '2' for prime numbers) "))
exclusive = input("Do the numbers have to have EXACTLY the number of factors you specified (exclusive), or can they have less than that (inclusive)? (Enter 'E' for exclusive, or 'I' for inclusive) ")
if exclusive.upper() == "E":
    exclusive = True
else:
    exclusive = False
print("Here are the numbers from 1 to", maximum, "that satisfy those conditions:")
print(sieve(maximum, num_factors, exclusive))
