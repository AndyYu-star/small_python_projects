import random
import math

def bubble_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    swapped = True
    passes = 0
    while passes < len(l)-1 and swapped:
        swapped = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                swapped = True
                swaps += 1
            comparisons += 1
        passes += 1
    print("Bubble sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def selection_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    for i in range(len(l)-1):
        min_pos = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_pos]:
                min_pos = j
            comparisons += 1
        if min_pos != i:
            l[i],l[min_pos] = l[min_pos],l[i]
            swaps += 1
    print("Selection sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def insertion_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    for i in range(1,len(l)):
        j = i
        item_sorted = False
        while j > 0 and not item_sorted:
            if l[j] < l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
                j -= 1
                swaps += 1
            else:
                item_sorted = True
            comparisons += 1
    print("Insertion sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def merge_sort_algorithm(array):
    l = array[:]
    writes = 0
    comparisons = 0
    s = 0
    space = 0
    if len(l) <= 1:
        return [l,writes,comparisons,space]
    else:
        result1 = merge_sort_algorithm(l[:len(l)//2])
        l1 = result1[0]
        writes += result1[1]
        comparisons += result1[2]
        result2 = merge_sort_algorithm(l[len(l)//2:])
        l2 = result2[0]
        writes += result2[1]
        comparisons += result2[2]
        aux = []
        l1_pos = 0
        l2_pos = 0
        while l1_pos < len(l1) and l2_pos < len(l2):
            if l1[l1_pos] < l2[l2_pos]:
                aux.append(l1[l1_pos])
                l1_pos += 1
            else:
                aux.append(l2[l2_pos])
                l2_pos += 1
            comparisons += 1
            s += 1
        if l1_pos < len(l1):
            for n in l1[l1_pos:]:
                aux.append(n)
                s += 1
        else:
            for n in l2[l2_pos:]:
                aux.append(n)
                s += 1
        if s > space:
            space = s
        s = 0
        for i in range(len(aux)):
            l[i] = aux[i]
            writes += 1
    return [l,writes,comparisons,space]

def merge_sort(array):
    result = merge_sort_algorithm(array)
    writes = result[1]
    comparisons = result[2]
    space = result[3]
    print("Merge sort -", writes, "writes,", comparisons, "comparisons and", space,"bytes of auxilliary memory")
    return result[0]

def quick_sort_algorithm(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    s = 1
    space = 0
    if len(l) <= 1:
        return [l,swaps,comparisons,space]
    pivot = l[0]
    left_point = 1
    right_point = len(l)-1
    while left_point <= right_point:
        while l[left_point] <= pivot and left_point < right_point:
            left_point += 1
            comparisons += 1
        if left_point == len(l)-1:
            if l[left_point] <= pivot:
                left_point += 1
            comparisons += 1
        while l[right_point] > pivot and left_point < right_point:
            right_point -= 1
            comparisons += 1
        if left_point < right_point:
            l[left_point], l[right_point] = l[right_point], l[left_point]
        else:
            l[0], l[left_point-1] = l[left_point-1], pivot
            right_point -= 1
        swaps += 1
    result1 = quick_sort_algorithm(l[:left_point-1])
    s += result1[3]
    if s > space:
        space = s
    s = 1
    result2 = quick_sort_algorithm(l[left_point:])
    s += result2[3]
    if s > space:
        space = s
    s = 1
    swaps += result1[1] + result2[1]
    comparisons += result1[2] + result2[2]
    l = result1[0] + [pivot] + result2[0]
    return [l,swaps,comparisons,space]
        
def quick_sort(array):
    result = quick_sort_algorithm(array)
    swaps = result[1]
    comparisons = result[2]
    space = result[3]
    print("Quick sort -", swaps, "swaps,", comparisons, "comparisons and", space,"bytes of auxilliary memory")
    return result[0]

def heap_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    for i in range(len(l) // 2, -1, -1):
        pos = i
        swapped = True
        while 2*pos+1 < len(l) and swapped:
            swapped = False
            if l[pos] > l[2*pos+1]:
                if 2*pos+2 < len(l):
                    if l[pos] <= l[2*pos+2]:
                        l[pos], l[2*pos+2] = l[2*pos+2], l[pos]
                        pos = 2*pos+2
                        swapped = True
                        swaps += 1
                    comparisons += 1
            else:
                if 2*pos+2 < len(l):
                    if l[2*pos+1] > l[2*pos+2]:
                        l[pos], l[2*pos+1] = l[2*pos+1], l[pos]
                        pos = 2*pos+1
                    else:
                        l[pos], l[2*pos+2] = l[2*pos+2], l[pos]
                        pos = 2*pos+2
                    swapped = True
                    swaps += 1
                    comparisons += 1
                else:
                    l[pos], l[2*pos+1] = l[2*pos+1], l[pos]
                    pos = 2*pos+1
                    swapped = True
                    swaps += 1
            comparisons += 1
    for i in range(len(l)-1, 0, -1):
        l[0], l[i] = l[i], l[0]
        swaps += 1
        pos = 0
        swapped = True
        while 2*pos+1 < i and swapped:
            swapped = False
            if l[pos] > l[2*pos+1]:
                if 2*pos+2 < i:
                    if l[pos] <= l[2*pos+2]:
                        l[pos], l[2*pos+2] = l[2*pos+2], l[pos]
                        pos = 2*pos+2
                        swapped = True
                        swaps += 1
                    comparisons += 1
            else:
                if 2*pos+2 < i:
                    if l[2*pos+1] > l[2*pos+2]:
                        l[pos], l[2*pos+1] = l[2*pos+1], l[pos]
                        pos = 2*pos+1
                    else:
                        l[pos], l[2*pos+2] = l[2*pos+2], l[pos]
                        pos = 2*pos+2
                    swapped = True
                    swaps += 1
                    comparisons += 1
                else:
                    l[pos], l[2*pos+1] = l[2*pos+1], l[pos]
                    pos = 2*pos+1
                    swapped = True
                    swaps += 1
            comparisons += 1
    print("Heap sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def comb_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    SHRINK_FACTOR = 1.3
    swapped = True
    gap = len(l)
    while swapped or gap > 1:
        swapped = False
        gap = int(gap / SHRINK_FACTOR)
        if gap < 1:
            gap = 1
        for i in range(0,len(l)-gap):
            if l[i] > l[i+gap]:
                l[i], l[i+gap] = l[i+gap], l[i]
                swapped = True
                swaps += 1
            comparisons += 1
    print("Comb sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def shell_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    SHRINK_FACTOR = 2.25
    gap = int(len(l) / SHRINK_FACTOR)
    last_pass = False
    while gap >= 1 and not last_pass:
        if gap == 1:
            last_pass = True
        for i in range(0,len(l),gap):
            j = i
            item_sorted = False
            while j >= gap and not item_sorted:
                if l[j] < l[j-gap]:
                    l[j],l[j-gap] = l[j-gap],l[j]
                    j -= gap
                    swaps += 1
                else:
                    item_sorted = True
                comparisons += 1
        gap = int(gap / SHRINK_FACTOR)
        if gap < 1:
            gap = 1
    print("Shell sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

def radix_sort(array):
    l = array[:]
    writes = 0
    reads = 0
    space = 0
    BASE = 4
    pointers = [0]*BASE
    space += len(pointers)
    aux = []
    largest = 0
    for item in l:
        aux.append(item)
        if item > largest:
            largest = item
        reads += 1
        writes += 1
        space += 1
    max_passes = int(math.log(largest,BASE)) + 1
    i = 0
    while i < max_passes:
        for item in l:
            for j in range((item % BASE**(i+1)) // BASE**i + 1,len(pointers)):
                pointers[j] += 1
            reads += 1
        for j in range(len(l)):
            aux[j] = l[j]
            writes += 1
        for item in aux:
            digit = (item % BASE**(i+1)) // BASE**i
            l[pointers[digit]] = item
            pointers[digit] += 1
            reads += 1
            writes += 1
        pointers = [0]*BASE
        i += 1
    print("Radix sort -", writes, "writes,", reads, "reads and",space,"bytes of auxilliary memory")
    return l

def counting_sort(array):
    l = array[:]
    writes = 0
    reads = 0
    space = 0
    pointers = [0]*len(l)
    space += len(pointers)
    aux = []
    largest = 0
    for item in l:
        aux.append(item)
        if item > largest:
            largest = item
        reads += 1
        writes += 1
        space += 1
    for item in l:
        for i in range(item + 1,len(pointers)):
            pointers[i] += 1
        reads += 1
    for i in range(len(l)):
        aux[i] = l[i]
        writes += 1
    for item in aux:
        l[pointers[item]] = item
        pointers[item] += 1
        reads += 1
        writes += 1
    print("Counting sort -", writes, "writes,", reads, "reads and",space,"bytes of auxilliary memory")
    return l

def optimised_bogo_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    for i in range(len(l)-1):
        sorted = True
        j = i+1
        while j < len(l) and sorted:
            if l[i] > l[j]:
                sorted = False
            comparisons += 1
            j += 1
        while not sorted:
            sorted = True
            for j in range(len(l)-1,i,-1):
                rand_index = random.randint(i,len(l)-1)
                l[rand_index],l[j] = l[j],l[rand_index]
                swaps += 1
            j = i+1
            while j < len(l) and sorted:
                if l[i] > l[j]:
                    sorted = False
                comparisons += 1
                j += 1
    print("Optimised bogo sort -", swaps, "swaps and", comparisons, "comparisons")
    return l

"""
def bogo_sort(array):
    l = array[:]
    swaps = 0
    comparisons = 0
    sorted = True
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            sorted = False
        comparisons += 1
    while not sorted:
        sorted = True
        for i in range(len(l)-1,0,-1):
            rand_index = random.randint(0,len(l)-1)
            l[rand_index],l[i] = l[i],l[rand_index]
            swaps += 1
        for i in range(len(l)-1):
            if l[i+1] < l[i]:
                sorted = False
            comparisons += 1
    print("Bogo sort -", swaps, "swaps and", comparisons, "comparisons")
    return l
"""
                    
array = list(range(20))
random.shuffle(array)
#array = [8,10,4,10,4,4,10,15,15,15,4,4,8,8,15,10,10,15,15,8]
#array = [0,1,3,4,2,5,6,8,7,10,9,11,12,17,14,16,13,15,19,18]
#array = list(range(19,-1,-1))

print(array)
bubble_sort(array)
selection_sort(array)
insertion_sort(array)
merge_sort(array)
quick_sort(array)
heap_sort(array)
comb_sort(array)
shell_sort(array)
radix_sort(array)
counting_sort(array)
optimised_bogo_sort(array)
#bogo_sort(array)
