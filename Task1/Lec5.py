#
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
#*Пример:*
#
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def weekend():
    num = input('Введите целое число от 1 до 7: ')
    flag = 0
    while flag == 0:
        try:
            num = int(num)
            if 1<=num<=5:
                print('Это рабочий день')
                flag = 1
            elif (6<=num<=7):
                print('Это выходной')
                flag = 1
            else:
                num = input('Введите целое число от 1 до 7: ')    
        except ValueError:
            num = input('Введите целое число от 1 до 7: ')
            
weekend()