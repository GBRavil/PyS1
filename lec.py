a = 123
b = 1.23
s = 'hello world'
print(f'{a} - {b} - {s}')
f =True
list = [1,2,3]

print ('Введите а')
a = input() # присваивает строку
a = int(input()) # присваивает число

a = 12
b = 8
c = a // b # деление в целых числах
c = a % b # деление без остатка
c = a ** b # возведение в степень

a = 1.3
b = 3
c = round(a * b, 7) # округление с указанием количества знаков после запятой

a = 3
a += 3 # a = a + 3

a = 1 < 4 and 5 > 2
a = 1 < 4 or 5 > 2
a = 1 == 2
a = 1 != 2
a = 1 < 3 < 5 < 6
f = [1,2,3,4]
is_odd = f[0] % 2 == 0

a = int(input('a = '))
b = int(input('a = '))
if a > b:
    print(a)
else:
    print(b)    

a = int(input('a = '))
b = int(input('a = '))
if a > b:
    print(a)
elif a > b:
    print(b)  
else:
    print(a + b) 

a = 23
b = 0
while a != 0:
    b = b * 10 + (a % 10)
    a //= 10
print(b)    

a = 23
b = 0
while a != 0:
    b = b * 10 + (a % 10)
    a //= 10
else:
    print('Пожалуй')
    print('хватит )')    
print(b)   

list = [1,2,3,4,5] # r = range(10), r = range(1, 10) r = range(1, 10, 2)
for i in list:
    print(i**2)

numbers = list(range(1,6))
