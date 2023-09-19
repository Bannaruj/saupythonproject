def EmployeeDetail():
    ID = input('กรุณากรอกรหัส : ')
    Name = input('กรุณากรอกชื่อ : ')
    return ID, Name

def EmployeeSales():
    Sales = float(input('กรุณากรอกยอดขาย : '))
    return Sales

def EmployeeCommis(Sales, Name, ID):
    if Sales > 1001 and Sales <= 2000:
        commission = Sales * 1 / 100
    elif Sales > 2000 and Sales <= 3000:
        commission = Sales * 3 / 100
    elif Sales > 3000:
        commission = Sales * 5 / 100
    else:
        commission = 0
    
    print(f'คุณชื่อ {Name} คุณรหัส {ID} คุณได้เงินคอมมิชชั่น {commission}')

ID, Name = EmployeeDetail()
Sales = EmployeeSales()
EmployeeCommis(Sales, Name, ID)







   

    




    
