def StudentDetail():
    student_id = input("กรอกรหัสนักเรียน: ")
    student_name = input("กรอกชื่อนักเรียน: ")
    student_grade = float(input("กรอกเกรดเฉลี่ยนักเรียน: "))
    return student_id, student_name, student_grade

def CheckResult(grade):
    if grade < 2.00:
        return "สอบไม่ผ่าน"
    else:
        return "สอบผ่าน"

def main():
    num_students = int(input("กรอกจำนวนนักเรียนที่ต้องการตรวจสอบ: "))
    
    for i in range(num_students):
        print(f"กรุณาป้อนข้อมูลนักเรียนที่ {i+1}:")
        student_id, student_name, student_grade = StudentDetail()
        result = CheckResult(student_grade)
        
        print(f"รหัสนักเรียน: {student_id}")
        print(f"ชื่อนักเรียน: {student_name}")
        print(f"เกรดเฉลี่ย: {student_grade}")
        print(f"ผลการเรียน: {result}")
        print()

if __name__ == "__main__":
    main()