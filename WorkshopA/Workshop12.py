def GroupLeader():
    Name = input('กรอกชื่อหัวหน้ากรุ๊ปทัวร์ : ')
    Phone = input('กรอกเบอร์ : ')
    return Name, Phone

def PersonAmount():
    Amount = int(input('กรอกจำนวน : '))
    return Amount

def MoneyPerson(Amount):
    if Amount <= 2:
        CostPerson = 300
    elif Amount <= 5:
        CostPerson = 250
    elif Amount <= 10:
        CostPerson = 210
    else:
        CostPerson = 150
    return CostPerson

group_leader_info = GroupLeader()
amount = PersonAmount()
cost_per_person = MoneyPerson(amount)

print("ข้อมูลหัวหน้ากรุ๊ปทัวร์:", group_leader_info)
print("จำนวนคน:", amount)
print("ค่าใช้จ่ายต่อคน:", cost_per_person, "บาท")

expenses = [cost_per_person] * amount  
min_expense = min(expenses)
max_expense = max(expenses)
total_expense = sum(expenses)
average_expense = total_expense / amount

print("ค่าน้อยที่สุด:", min_expense)
print("ค่ามากที่สุด:", max_expense)
print("ผลรวม:", total_expense)
print("ค่าเฉลี่ย:", average_expense)
        
