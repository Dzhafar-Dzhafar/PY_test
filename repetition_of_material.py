#Условия
'''data  = int(input("Введите число: "))
if data == 10:
    print("Значение равно 10")
    print("data= ",data)
elif data < 10:
    print("Значение меньше 10")
    print("data= ",data)
else:
    data = int(input("Введите что-то другое: "))
    print("data= ",data)
'''
#Циклы FOR
'''
for i in range(1, 11, 1):
    if i==8:
        break
    if i % 2==0:
        continue
    print(i)
'''
#Циклы FOR
'''
count=0
world = "Hi, proger!"
for i in world:
    if i=="r":
        count+=1
print(count)
'''
#Циклы while
'''
IHC=True 
while IHC:
    if input("Введи: ") == "Stop":
        IHC=False
'''
#Циклы FOR
'''
found=None
for i in "Hello!":
    if i =='H':
        found=True
        break
else:
    found=False
print(found)
'''
#Работа со списками
'''
nums =[1, 2, 3, 4, 5, True, "string", 5.2]
'''
'''
nums[0] =10
nums[-4]= 1
print(nums)
print(nums[3])
print(nums[-1][-1])
'''
'''
nums[-2]=0.1234
#nums.append(1000)#приставка значения
#nums.insert(1, True)#смещение элемента
#q=[1, 2, 0]
#nums.extend([q])
nums.sort()
#nums.reverse()
#nums.pop(-3)#Удаление последнего или назначенного элемента по индексу
#nums.remove(True)#удаление определенного значения по его содержимому
#nums.clear()#Чистка списка
print(nums.count(True))
print(nums)
'''
'''
nums=[55, 4, 11, 2, "23", False]
for el in nums:
    el *=-1
    print(el)
'''

#Даем клиенту задать длинну списка, элементы,  и выводим его
'''
n=int(input("Введи: "))
user=[]
i=0
while i<n:
    string="Элемент №" + str(i+1) +":"
    user.append(input(string))
    i+=1
print(user)
'''

#Функции строк
#word = "football"
#print("Длина строки =",(len(word)))
#print("Сколько у нас L в списке: ", (word.count('l')))
#print("Выводим список в верхнем регистре: ",(word.upper()))
#print("Выводим список : ",(word.isupper())) #True/False является ли вся эта строка в верхнем регистре
#print("Проверка на нижний регистр: ",(word.islower())) #Приводим к нижнему регистру
#print("Вывод строки с верхнего регистра: ", (word.capitalize()))
#print("Выводим индекс искомого символа 'О' из списка =", [word.find('o')])
'''
#Работа со списком
word='Змея, гусь, кукуруза'
hobby = word.split(', ')
for i in range(len(hobby)): #До длинны списка будет идти цикл
    hobby[i] = hobby[i].capitalize()
#Превращаем список в строку
result = " | ".join(hobby)
print(result)
'''
'''
#Индексы и срезы
word='footboll'
print(word[0:4:1])#С какого символа : По какой : Шаг
print(word[::-1])#Вывод строки целиком, в обратном порядке

#На примере списка
lis=[1, 5, "STR", True, 7.23]
#print(lis[2:-1:]) #Выводим с 3 эл до предпоследнего [4]=True
print(lis[:2:]) #Выводим по порядку первые от 0 до 2 из списка [1, 5] с шагом=1
'''
#Кортежи
'''
data=(1, 3, 4, 77, 12, True, 7.2, 'Buklia')
print(data[1:5])
print(len(data))
print(data)
'''
#data= 5, 3, 12, 2, True
#print(data)

#data= 5,
#print(data)
'''
data=(1, 3, 4, 77, 12, True, 7.2, 'Buklia')
for el in data:
    print(el)
nume=[1, 2, 3] #список переделаем в кортеж
new_data = tuple(nume)
print(new_data)
'''
#word=tuple('iProgger') #Строку в кортеж
#print(word)

#тип Словарь
#coco = {3: "GG", 2: "GO", 1: "GT"}
#print (coco[1])

#cocos=dict(code='us', name='America')
#print(cocos['name'])

'''
coco = {3: "GG", 2: "GO", 1: "GT"}
for key, value in coco.items(): #Функуия 'items'
    print(key, '-', value)
#Получаем:
#3 - GG
#2 - GO
#1 - GT
'''
'''
coco = {3: "GG", 2: "GO", 1: "GT"}
#print(coco.get(2)) # GET заменет []

#coco.clear() #Чистим словарь
#print(coco)

#Удаление элемента словаря
#coco.pop(3)
#print(coco)

#Удаление последнего элемента словаря
#coco.popitem()
#print(coco)

#Получить ключи
#print(coco.keys())

#Значения
#print(coco.values())

#Вывести содержимое словаря
#print(coco.items())
'''
#Вложенные словари
'''
person={
    'user_1':{
        'first_name': 'Jon',
        'last_name': 'Mogo',
        'age': 25,
        'address': ['г.Моггао', 'ул.Курагуа', '13'],
        'grades': {'MAT':3, 'FAT':5}
    }
}
print(person['user_1']['address'][1])
'''
#Функции
'''
def test_func(word):
    #pass #аналог "ничего"
    print(word, end="")
    print("!")

test_func("Hi")
test_func(5)
test_func(True)
'''
'''
def summa(a, b):
    res=a+b
    return res
    #return a+b #или так
res=summa(5, 5)
print(res)
'''
'''
#Находим минимальное из списка
nums=[1, 5, 0.1, 7]
min=nums[0]
for el in nums:
    if el < min:
        min=el
print(min)
'''
#Сократим выше указанное
'''
def minimal(l):
    min_num = l[0]
    for el in l:
        if el < min_num:
            min_num=el
    return min_num
nums=[1, 5, 0.1, 7]

name1= minimal(nums)
if name1 < 1:
    print("<1")
else:
    print(">1")
'''
#Лямбда функции (запись в одну строчку кода (анонимная функция))
'''
func = lambda x, y: x*y
print (func(5, 2))
'''
#Работа с документами
'''
#Создаем и записываем в файл данные
file = open('C:/Users/18805444/Desktop/00000/data/text.txt', "w")

file.write('Hello')

file.close()
'''
'''
#Добавление значения в документ
file = open('C:/Users/18805444/Desktop/00000/data/text.txt', "a")

file.write('Hello\n')
file.write('!!!')

file.close()
'''
'''
data = input("Ввведите текст: ")
file = open('C:/Users/18805444/Desktop/00000/data/text.txt', "a")

file.write(data + '\n')

file.close()
'''
#Выводим первые 4 символа с документа
'''
file = open('C:/Users/18805444/Desktop/00000/data/text.txt', 'r')
print(file.read(4))

file.close()
'''
'''
#Считываем файл построчно
file = open('C:/Users/18805444/Desktop/00000/data/text.txt', 'r')
for line in file:
    print(line, end="")

file.close()
'''
#Исключения
#До тех пор пока Х=не число, будем просить ввести число
'''
x=0
while x==0:
    try:
        x=int(input("Введите число: "))
        x+=5
        print(x)
    except ValueError:
        print('Введите именно число!')
'''
#Вывод исключения деления на ноль
'''
try:
    x=5/0
    x=int(input())
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    Print("Вы ввкли что-то не так!")
'''
#Finally блок
'''
try:
    x=5/0
    x=int(input())
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    Print("Вы ввкли что-то не так!")
finally:
    print("Finally")
'''
#else в исключениях
'''
try:
    x=5/1
    x=int(input())
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Вы ввкли что-то не так!")
else:
    print('else')
'''
#Менеджер with ... as (самостоятельно открывает и закрывает файл)
'''
try:
    with open ('C:/Users/18805444/Desktop/00000/data/word.txt', 'r', encoding='utf-8' ) as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!")
'''
#Модули
'''
#time функция sleep (делаем отсрочку вывода ответа)
import time
time.sleep(3)
print('Hi')
'''
#datetime (псевдоним)
'''
import datetime as D #Устанавливаем псевдоним для модуля
print(D.datetime.now().time()) #Выводим текущее время
'''
'''
import datetime as D, sys, os, platform

print(sys.path)#Полный путь к текущему файлу
print(platform.system())#На какой ОС сейчас пользователь
'''

'''
import datetime as D, sys, os, platform
from math import sqrt as S, ceil #Импортируем из MATH функции sqrt(квадратный корень) и ceil (оеркгление значения)
print(S(5))
print(ceil(345345.43534543))
'''
#Создаем свой модуль (в доке Мой модуль.py)
#Вызываем весь модуль
'''
import MyMod as MM
print(MM.name)
MM.hello()
'''
#Используем частичное взаимодействие с модулем
'''
from MyMod import add_three_numbers as ADD

print(ADD(5, 3 , 12))
'''
#Установка сторонней библиотеки в терминале
'''
pip install NAME
'''

#Конструкторы