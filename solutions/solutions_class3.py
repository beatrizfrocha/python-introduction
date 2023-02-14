#1 fizemos este

def first_last(lst):
    return lst[0], lst[-1]

#2 fizemos este

def disconnection(s1, s2):
    return s1 - s2

#3 fizemos este

def max(lst):
    max_elem = 0
    for i in lst:
        if i>max_elem:
            max_elem = i
    return max_elem

#4 fizemos este

import math

def euclidean_distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

#5

def multiple_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0

def sum_multiples(limit):
    result = 0
    for i in range(1, limit+1):
        if multiple_3_or_5(i):
            result += i
            
    return result

#6 fizemos este

def filter_height_weight(d, h, w):
    result = {}
    for key, value in d.items():
        if value[0] >= h and value[1] >= w:
            result[key] = value
            
    return result

#7 fizemos este

def pairs(limit):
    return [(x, y) for x in range(limit+1) for y in range(limit+1)]

#8 fizemos este

def sum_list_tuple(it):
    result = 0
    for elem in it:
        result+=elem
    
    return result

def sum_tuples_in_list(l):
    result = []
    for elem in l:
        result.append(sum_list_tuple(elem))
        
    return result

#9 fizemos este

def least(l, n):
    l.sort()
    
    return l[:n]

#10 fizemos este

def max_sublist(l):
    sum = 0
    index = 0
    for idx, sl in enumerate(l):
        if sum_list_tuple(sl) > sum:
            sum = sum_list_tuple(sl)
            index = idx
            
    return l[index]