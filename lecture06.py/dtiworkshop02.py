def inputCarDetail() :
    carNo = input('ป้อนทะเบียนรถ : ')
    carWeight = float( input('ป้อนน้ำหนักรถ : '))
    return carNo, carWeight

def checkcarandshowweight(carNo, carWeight) :
    if carWeight > 1000 :
        print(f'{carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'{carNo} น้ำหนักผ่านเกณฑ์')

print('-----------------------')
print('truckchecker')
print('-----------------------')
carNo, carWeight = inputCarDetail()
print('-----------------------')
checkcarandshowweight(carNo, carWeight)
print('-----------------------')