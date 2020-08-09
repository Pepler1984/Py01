import math
def printSQ(a,b):#печать квадрата
    A = [["*"] * a] * b
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()
def square(a,b,k):#рекурсия разбивка квадрата
    k += 1 # Счетчик кол-ва квадратов
    if a>b:
        a=b
    elif b>a:
        b=a
    elif a==b>1:
        a=math.ceil(a/2)
        b=a
    elif a<=1:
        return
    print("Квадрат № ",k,"\n")
    print("длина сторон квадрата:",a)
    printSQ(a,b)
    square(a,b,k)

a=int(input("Введите длину прямоугольника:\n"))
b=int(input("Введите высоту прямоугольника:\n"))
printSQ(a,b)
k = 0
square(a,b,k)