#1

def inverse(n):
    if n == 0:
        raise ZeroDivisionError("Cannot divide by zero")
        
    return 1/n

#2

def no_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except:
        print("No such file")

#3

import math

def quadratic_formula(a,b,c):
    discriminant_binomial = b ** 2 - 4 * a * c
    
    if discriminant_binomial < 0:
        raise Exception("Impossible equation")
        
    solution1 = (-b + math.sqrt(discriminant_binomial))/2*a
    solution2 = (-b - math.sqrt(discriminant_binomial))/2*a
    
    return solution1, solution2

#4

import math

class Esfera:
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return 4 * math.pi * self.raio ** 2
        
    def volume(self):
        return 4/3 * math.pi * self.raio ** 3

#5

class Animal:
    
    def __init__(self, cor, peso):
        self.cor = cor
        self.peso = peso

class Cao(Animal):
    def __init__(self, cor, peso, raca):
        super().__init__(cor, peso) 
        self.raca = raca
        
    def som(self):
        print("au au")
        
class Ave(Animal):
    def __init__(self, cor, peso, velocidade):
        super().__init__(cor, peso) 
        self.velocidade = velocidade
    
    def som(self):
        print("piu piu")

#6

class Compra:
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
        
    def total(self):
        return self.preco * self.quantidade
    
class CompraOnline(Compra):
    def __init__(self, preco, quantidade):
        super().__init__(preco, quantidade)
        
    def total(self):
        total = super().total()
        total += total * 0.05
        
        return total

#7

class MyEnumerate():
    
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

#8

class MyRange:
    def __init__(self, n):
        self.n = n
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > self.n - 1:
            raise StopIteration

        y = self.index
        self.index += 1
        return y

#9

def fibonacci():
    n1 = 1
    n2 = 1
    
    while True: #com o gerador não temos problemas de memória
        yield n1
        n1, n2 = n2, n1+n2

#10

def factorial():
    n1 = 0
    n2 = 1
    
    while True:
        yield n2
        n1 += 1
        n2 *= n1