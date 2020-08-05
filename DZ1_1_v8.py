"""Дано натуральное четырехзначное число n.
Верно ли, что все его цифры различны?"""

celoe = int(input("введите целое число:\n"))
print("верно ли, что все числа различны?", celoe)
A=[]
while celoe > 1: #Создаем список
    raz=celoe%10
    celoe=celoe//10
    A.append(raz)
A.append(celoe)
print(A)
A.reverse() #Разворачиваем список
print(A)

# Вариант 1
k=0
for i in range (len(A)-1):
    for j in range(i+1,len(A)):
        print(A[i],A[j])
        if A[i]==A[j]:
            k+=1
if k>0: print("есть совпадения", k,"раз")
else: print("все числа различны")

# Вариант 2 (множества)
print(A)
setA = set(A)
print(type(A))
print(type(setA))
if len(A) == len(setA):
    print("все числа различны")
else:
    print("есть совпадения")
    
            
            
   
      
 
    
    
