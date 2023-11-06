
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(num):
    return num**2

def even(num):
    return num%2==0

lista= [num for num in filter(even, numeros)]
print(lista)

print (list(map(square, numeros)))