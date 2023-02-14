#1 fizemos este

def calculator():
    operation = input("What operation would you like to perform? (add/subtract/divide/multiply) ")
    number1 = input("Insert the first number ")
    number2 = input("Insert the second number ")
    if operation == "add":
        return float(number1) + float(number2)
    elif operation == "subtract":
        return float(number1) - float(number2)
    elif operation == "divide":
        return float(number1) / float(number2)
    else:
        return float(number1) * float(number2)

#2 fizemos este

def rewrite(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            result = f.readlines()
            
        with open("new_file.txt", "a") as f:
            for idx, line in enumerate(result):
                if idx == 4:
                    continue
                f.write(line)
    else:
        print(f"{filename} does not exist.")

#3 fizemos este

def count_words():
    file = input("Insira o caminho do ficheiro pretendido ")
    result = 0
    
    if os.path.exists(file):
        with open(file, "r") as f:
            txt = f.read()
            result = len(txt.split())

    return result

#4 fizemos este

def bigger_than_n(l, n):
    return list(filter(lambda x: len(x)>n, l))

#5 fizemos este

def abs_value(l):
    return list(map(abs, l))

#6 fizemos este

def min(l):
    return reduce(lambda x, y: x if x < y else y,l)

#7 fizemos este

def harmonic_sum(n):
    return reduce(lambda x, y: x + 1/y, range(1,n))

#8 fizemos este

def sum_3_lists(l1,l2,l3):
    return list(map(lambda x, y, z: x+y+z,l1,l2,l3))

#9 fizemos este

def freq_word():
    word = input("Insert the word ")
    filename = input("Insert the file path ")
    result = 0
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            text = f.read()
            result = text.count(word)

    return result

#10 fizemos este

def filter_positives(l):
    return list(filter(lambda x: x>0, l))
