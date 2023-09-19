def loanName() :
    Name = input('กรุณาใส่ชื่อ :')
    return Name

def loanMoney() :
    Money = float(input("ป้อนจำนวนเงินกู้ (บาท): "))
    return Money
def InterestCal(Name, loanMoney):
    if loanMoney >= 1000:
        interest_rate = 2.5  
    else:
        interest_rate = 5.5
    interest_payment = (interest_rate / 100) * loanMoney
    print(f"คุณชื่อ {Name} อัตราดอกเบี้ยที่คุณจะต้องจ่ายคือ {interest_payment:.2f} บาท")

name = loanName()
money = loanMoney()

InterestCal(name, money)