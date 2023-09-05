def funcInp( ) : 
    Money = float (input('กรอกจำนวนเงิน : '))
    Person = int (input('จำนวนคน : '))
    return Money, Person

def funcMath(Money, Person ) : 
    print(f'จำนวนเงิน {Money:.2f} บาท มี {Person} คน หารออกมาได้คนละ {round(Money / Person)} บาท')
    print('จำนวนเงิน',Money,'บาท',Person,'คน','หารออกมาได้คนละ',round(Money / Person),'บาท')
    print('จำนวนเงิน'+str(Money)+'บาท มี'+str(Person)+'หารออกมาได้คนละ'+str(round(Money / Person))+'บาท')
    print('จำนวนเงิน {:.2f} บาท มี {} หารออกมาได้คนละ {} บาท'.format(Money,Person,round(Money / Person)))
    print('จำนวนเงิน %.2f บาท %d บาท หารออกมาได้คนละ %d บาท' % (Money,Person,round(Money/Person)))

Money, Person = funcInp( )
funcMath(Money, Person )