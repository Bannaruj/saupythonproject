#Function 2 : have parameter( )/no return
#parameter = ตัวเเปร(varible)
def funcA(x, y) :
    print('AAA')
    z = x + y
    print(f'{x} + {y} = {z}')

def funcB(x, y, z):
    print('{:.2f} {:.4f} {:.5f}'.format(x, y, z))
funcA(10, 20) #ข้อมูลที่ส่งให้parameterคือ argument
funcA(5, 10)
funcB(2, 3, 4)
