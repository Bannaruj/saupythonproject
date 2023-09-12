def InputBaseHigh() :
    Base = float( input('ป้อนฐานข้อมูล : '))
    High = float( input('ป้อนสูง : '))
    return Base, High

def calandshowtrianglearea(Base, High) :
    area = Base * High / 2
    print(f'สามเหลี่ยมฐาน {Base:.2f} สูง {High:.2f} มีพื้นที่ {area:.2f}')


print('-----------------------')
print('calculate triangle area')
print('-----------------------')
Base ,High = InputBaseHigh()
print('-----------------------')
calandshowtrianglearea(Base, High)
print('-----------------------')