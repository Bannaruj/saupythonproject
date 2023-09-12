#คำสั่งbreakกับcontinue ที่มักใช้ร่วมกับ Control flow
for x in range(5) :
    if x == 3 :
        break; #break ทำให้จบloopทันที
    print(f'SAU...{x}')
print('----------------')
for y in range (5) :
    if y == 3 :
        continue; #continueทำงานเมื่อไหร่จบรอบนั้น ไปรอบต่อไปทันที
    print(f'DTI....{y}')