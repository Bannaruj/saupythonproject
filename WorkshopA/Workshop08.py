def PhLocation() :
    Where = (input('กรุณากรอกสถานที่ : '))
    Ph = int(input('กรุณากรอกค่าph : '))
    return Where, Ph

def PhResult(Ph) :
    if Ph == 7 or Ph == 8 :
        return 'Result is Normal'
    elif Ph > 8 :
        return 'Result is Acid'
    else :
        return 'Result is Alkali'
    
def Phshow(Where, Ph) :
    print(f'คุณอยู่ที่ {Where} มีค่า Ph {Ph}')

Where, Ph = PhLocation()
Phshow(Where, PhResult(Ph))

                