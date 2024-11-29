import random
import math

def add_parity_bits(string):
    #adding parity bits
    num_parities = int(math.log(len(string), 2)) + 1
    if int(math.log(len(string) + num_parities, 2)) >= num_parities:
        num_parities += 1
    for parity in range(num_parities):
        string = string[0:(2**parity)-1] + "p" + string[(2**parity)-1:]
    string = "0" + string

    #assigning parity checks
    for parity in range(num_parities):
        even_1s = True
        for i in range(len(string)):
            if (i // 2**parity) % 2 == 1 and string[i] == "1":
                even_1s = not even_1s
        if even_1s:
            string = string[:2**parity] + "0" + string[(2**parity)+1:]
        else:
            string = string[:2**parity] + "1" + string[(2**parity)+1:]
                
    return string

def reconstruct(code):
    #use parity checks
    num_parities = int(math.log(len(code), 2)) + 1
    wrong_index = 0
    for parity in range(num_parities):
        even_1s = True
        for i in range(len(code)):
            if (i // 2**parity) % 2 == 1 and code[i] == "1":
                even_1s = not even_1s
        if not even_1s:
            wrong_index += 2**parity

    #correct wrong bit
    if wrong_index < len(code):
        if code[wrong_index] == "0":
            code = code[:wrong_index] + "1" + code[wrong_index+1:]
        else:
            code = code[:wrong_index] + "0" + code[wrong_index+1:]
    else:
        print("Unable to correct!")
        
    #remove parity bits
    for parity in range(num_parities-1, -1, -1):
        code = code[:2**parity] + code[(2**parity)+1:]
    code = code[1:]
    
    return code

string = input("Enter a string of bits: ")

code = add_parity_bits(string)
print("Encoding:", code)

changed_index = random.randint(0,len(code)-1)
if code[changed_index] == "0":
    code = code[:changed_index] + "1" + code[changed_index+1:]
else:
    code = code[:changed_index] + "0" + code[changed_index+1:]
print("Encoding after bit flip:", code)

""" #uncomment to test if two bits flip
changed_index = random.randint(0,len(code)-1)
if code[changed_index] == "0":
    code = code[:changed_index] + "1" + code[changed_index+1:]
else:
    code = code[:changed_index] + "0" + code[changed_index+1:]
print("Encoding after bit flip:", code)
"""

print("Corrected string:", reconstruct(code))
