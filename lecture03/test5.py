AllMoney = int(input('บอกจำนวนเงิน :'))
how_guy = float(input('บอกจำนวนคน :'))
print('----------------------------------')
result = float(AllMoney)/float(how_guy)
Divide = format(float(result)),".2f"
print(f'คุณมากัน {how_guy} รับเงินมา {AllMoney:.2f} ต้องจ่ายคนละ {result:.2f}')
print('คุณมากัน',(how_guy),'รับเงินมา',(AllMoney),'จ่ายคนละ',(result))
print(str('คุณมากัน')+str(how_guy)+str('รับเงินมา')+str(AllMoney)+str('จ่ายคนละ')+str(result))
print('คุณมากัน {} รับเงินมา {} จ่ายคนละ {} '.format(how_guy,AllMoney,result))