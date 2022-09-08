#3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).

#*Пример:*

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

def get_float():
    while type:
        number_float = input()
        try:
            number_float = float(number_float)
            return number_float
        except ValueError:
            print('Неверный ввод числа!!!')
    return number_float

def GetPoint(x,y):
    if x==0 and y==0:
        print('Это точка пересечения координат!')
    elif x==0:
        print('Эта точка находится на оси Y')
    elif y==0:
        print('Эта точка находится на оси X')
    elif x>0 and y>0:
        print ('Эта точка находится в I четверти')
    elif x>0 and y<0:
        print ('Эта точка находится в II четверти')
    elif x<0 and y<0:
        print ('Эта точка находится в III четверти')
    else:
        print ('Эта точка находится в IV четверти')    



print('Введите координату Х:')
x = get_float()

print('Введите координату Y:')
y = get_float()

GetPoint(x,y)