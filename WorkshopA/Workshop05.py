def EmployeeDetail() :
    EmployeeID = input('ใส่รหัสพนักงาน : ')
    EmployeeName = input('ใส่ชื่อ : ')
    return EmployeeID, EmployeeName

def EmployeeSalary() :
    Salary = float(input('ใส่เงินเดือน : '))
    return Salary

def calsalary(Salary, EmployeeID, EmployeeName) :
    AfterTax = Salary - (Salary * 7 /100) - 500
    print(f'คุณรหัส{EmployeeID} คุณชื่อ{EmployeeName} เงินเดือนสุทธิเท่ากับ {AfterTax}')

EmployeeID, EmployeeName = EmployeeDetail()
Salary = EmployeeSalary()
calsalary(Salary, EmployeeID, EmployeeName)