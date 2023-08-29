#รับข้อมูลทางเเป้นพิมพ์(input)
emp_name = input('ป้อนชื่อพนักงาน : ')
SalePrice = float(input('ป้อนยอดขาย : '))
print('---------------------------')
#int( )จำนวนเต็ม float( )จำนวนจริง
commision = float(SalePrice) * 10 / 100

print(f'คุณ {emp_name} ยอดขาย {SalePrice:.2f} บาท ได้ค่าคอมมิชชั่น {commision:.2f} บาท')
print('คุณ',emp_name,'ยอดขาย',SalePrice,'บาท ได้ค่าคอมมิชชั่น',commision,'บาท')
print(str('คุณ')+str(emp_name)+str('ยอดขาย')+str(SalePrice)+str('บาท ได้ค่าคอมมิชชั่น')+str(commision)+str('บาท'))
print('คุณ {} ยอดขาย {} บาทได้ค่าคอมมิชชั่น {} บาท'.format(emp_name,SalePrice,commision))
