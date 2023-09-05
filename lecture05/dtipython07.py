import math
def rad( ) :
    return float( input('ป้อนรัศมี : '))
def CalArea (radius) :
     area = math.pi * radius **2
     return area
def CalRound (radius) :
    round = 2 * math.pi * radius
    return round
def calCubeCircle (radius) :
    round = 4 / 3 * math.pi * radius ** 3 
    return round
def showResult () :
    a = rad()
    print(f'มีพื้นที่วงกลม {CalArea(a):.4f} เส้นรอบวงเป็น {CalRound(a):.4f} ปริมาตร {calCubeCircle(a):.4f} UwU')
showResult ()