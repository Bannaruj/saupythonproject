def Xsequence() :
    x = int(input('กรอกค่าตัวเเปร :'))
    return x

def calX(x) :
    y = 2*x**2 + 2*x + 1 
    return y

def showcalculate(x, y) :
    print(f'ค่าตัวเเปรคุณเท่ากับ {x} เมื่อคิดในสมการจะได้ {y}')

x = Xsequence()
y = calX(x)
showcalculate(x, y)