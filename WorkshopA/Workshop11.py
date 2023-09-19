def PhoneDetail():
    Name = input('กรอกชื่อ : ')
    PhoneNumber = input('กรอกเบอร์ : ')
    return Name, PhoneNumber

def PhoneperMinute(Minute):
    total_cost = 0

    for minute in range(1, int(Minute) + 1):
        if minute <= 15:
            CostPerMinute = 5
        elif minute <= 30:
            CostPerMinute = 3
        else:
            CostPerMinute = 1.5
        total_cost += CostPerMinute
    
    return total_cost

def PhoneMinute():
    Minute = input('กรอกนาที : ')
    total_cost = PhoneperMinute(Minute)
    print("ค่าใช้จ่ายทั้งหมด:", total_cost, "บาท")

Name, PhoneNumber = PhoneDetail()
PhoneMinute()








        