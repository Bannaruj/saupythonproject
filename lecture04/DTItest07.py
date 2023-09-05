employ_money = float(input('เงินเดือน :'))
employ_name = input('ชื่อพนักงาน :')
employ_ID = input('ป้อนรหัสพนักงาน: ')
Tax = employ_money + (employ_money * 7 / 100) - 500
print(f'คุณชื่อ {employ_name} รหัส {employ_ID} เงินเดือนสุทธิ {Tax}')