#solution to APPS 1114 (from https://youtu.be/0pgEMWy70Qk?&t=338)


import random

def prank(a, n):
    #a is an array which only contains ints from 1 to n (inclusive)
    
    #least restrictive condition to ensure a reconstruction is possible:
    #all items in f with indices found in a must be the first occurence of their value in f
    #(this ensures they're all 'identifiable' by the reconstruction algorithm)

    #the values of f are arbitrary as long as they satisfy the above condition
    #here i'm making f so that all values in f are minimised (positive ints)
    f = [-1 for i in range(n)]
    count = 1 #used for items that must be unique
    
    for v in a:
        if f[v-1] == -1:
            f[v-1] = count
            count += 1

    for i in range(n):
        if f[i] == -1:
            count_2 = 1 #used for items that don't matter (can repeat)
            while count_2 in f[i+1:]:
                #finds the lowest number not found after f[i]
                count_2 += 1
            f[i] = count_2

    b = [f[a[i]-1] for i in range(len(a))]
    
    yield f
    yield b
    
def reconstruct(f, b):
    n = len(f)
    m = len(b)
    a = [-1 for i in range(m)]
    
    for i in range(m):
        found = False
        j = 0
        while j < n and not found:
            if f[j] == b[i]:
                found = True
            j += 1
        #since every item in b was defined to be a value output by f,
        #there should always be an item in f equal to a specific item in b
        assert found == True

        a[i] = j #a[i] should be from 1 to n, so j shouldn't be decremented

    return a
        

n = int(input("n: "))
m = int(input("m: "))
a = [random.randint(1, n) for i in range(m)]

x = prank(a, n)
f = next(x)
b = next(x)

a_result = reconstruct(f, b)

print("a:",a)
print("f:",f)
print("b:",b)
print("reconstructed a:",a_result)

for i in range(m):
    assert a[i] == a_result[i]
