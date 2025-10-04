def factorial(n):
    result = 1
    if n>=0:
        if n==0:
            return 1
        else:
            for i in range(n):
                result = result * (i+1)
                i = i + 1
            
            return result
    else:
        print("Ingresa un número positivo")

def factorial_recursivo(n):
    if n>=0:
        if n==0:
            return 1
        else:
            result = n * factorial_recursivo(n-1)
            
            return result
    else:
        print("Ingresa un número positivo")


print(factorial_recursivo(4))
print ("hola")