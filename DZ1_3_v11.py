"""Удалить пять первых нечетных по значению
элементов списка
Работает только при условии длинны списка от 9 элементов"""
import random
n=int(input("Введите длину списка N>=9, N = :\n"))
A=[0]*n
for i in range (len(A)):
    A[i]=random.randint(0,100)
print(A)
for i in range (0,10,2):#меняю первые 5 нечет на 's'
    A[i]='s'
print(A)
i=0
while i<len(A): # двигаемся по списку удаляем 's'
    if A[i] == 's':
        A.remove(A[i])
    else:
        i+=1
print(A)
    



