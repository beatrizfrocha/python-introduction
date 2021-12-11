#1

def mean_second_column(matrix):
    return np.mean(matrix, axis = 0)[1]

#2

def even_elems(matrix):
    return matrix[matrix % 2==0]

#3

def sort_by_mean(*arrays):
    mean = []
    for idx, array in enumerate(arrays):
        mean.append((idx, np.mean(array)))
        
    mean.sort(key = lambda x: x[1])
    
    index = mean[-1][0]
        
    return arrays[index]

#4

def replace_inferior(array, n):
    return np.where(array < n, -100, array)

#5

def split_array(array, n):
    result = []
    new_array = np.array_split(array,n)
    for elem in new_array:
        result.append(len(elem))
    return result

#6

def join_arrays(array1, array2):
    if array1.base is None and array2.base is None:
        return np.stack((array1,array2))
    else:
        return np.stack((array1,array2), axis = 1)

#7

def sum_with_nditer(array1, array2):
    result = []
    for x in np.nditer(array1):
        for y in np.nditer(array2):
            result.append(x+y)
            
    return result

#8

def matrix_3_3():
    return np.arange(2,11).reshape(3,3)

#9

def sum_or_product(array):
    if array.dtype == "int":
        result = np.cumsum(array)
    else:
        result = np.prod(array)
        
    return result

#10

def fourth_column(matrix):
    return matrix[0:4, 2]

#11

def positions_of_nan(array):
    return np.where(np.isnan(array))

#12

def celsius_to_fahrenheit(celsius):
    return celsius*1.8+32

#13

def nth_repetition(array, item, n):
    return np.where(array==item)[0][n-1]

#14

def diagonal_1_to_5():
    return np.diag(1+np.arange(5))

#15

def higher(x,y):
    return np.where(x>y) 