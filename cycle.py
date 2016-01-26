from openpyxl import *
from datetime import *

wb = Workbook()
ws = wb.active

ws.title = "список"

a, b = [], []
column = ['ПІБ абонента: > ','Адреса: > ']

worker = input("Старший слюсар зміни:> ")   

while True:
    try:
        print("Введіть дату")    
        d = date(
             int(input("рік> ")), 
             int(input("місяць> ")), 
             int(input("день> "))
            )
        break
    except ValueError:
        print("Не вірна дата! Пробуй ще")

while True:
    try:
        q = int(input("скільки %s було заявок по витокам ? > " % d))      
        break
    except ValueError:
        print("Помилка с кількістю заявок, давай ще.")

while True:         
    if q > 0:               # цикл отвечающий за количество заявок
        for i in range(1, 3):            
            #создание списка с инф. о утечках и абонетах
            a.append(input("%s" % (column[i-1])))   
            
        a.append(worker) 
        #список дат нужно будет для прикрепления к инормации по заявкам, 
        # а так же для вычисления времени потраченого в пути 
        while True:
            try:
                print("час отримання заявки:")  
                t1 = time(
                           int(input("годин> ")),
                           int(input("хвилин> "))
                         )
                break
            except ValueError:
                print("Не вірний час отримання, вводь ще")            
        a.append(str(datetime.combine(d, t1)))
        
        while True:
            try:
                print("час прибуття на заявку:")  
                t2 = time(
                           int(input("годин> ")),
                           int(input("хвилин> "))
                         )
                break
            except ValueError:
                print("Не вірний час прибуття, вводь ще")
        a.append(str(datetime.combine(d, t2)))
        
        #разница между временем получения и выездом
        a.append(abs(datetime.combine(d, t2) - datetime.combine(d, t1)))
        #вставка пустої комірки
        a.append('')
        #причина аварии
        a.append(input("введіть причину витоку газу> "))

        ws.append(a)                    #append prev list to active list
        wb.save('fun.xlsx')
        a = []                          # очистка списка данными по абонентам
        q -= 1      #cчетчик заявок в один день
    
    elif q == 0:
        print ("змінити дату - ’д’, закінчити - ’к’")
        j = input("> ")
        if j == 'д':
            while True:
                try:
                    print("Введіть дату")    
                    d = date(
                         int(input("рік> ")), 
                         int(input("місяць> ")), 
                         int(input("день> "))
                        )
                    break
                except ValueError:
                    print("Не вірна дата! Пробуй ще")

            while True:
                try:
                    q = int(input("скільки %s було заявок по витокам ? > " % d))      
                    break
                except ValueError:
                    print("Помилка с кількістю заявок, давай ще.")         
            continue
        elif j == 'к':
            wb.save('fun.xlsx')
            break
        break

        















