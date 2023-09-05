#Function 1 : no parameter( )/no return
def funcA( ) :
    print('AAA')
    #funcB( )ไม่ควรเรียกfunctionสลับกันไปมา
    print('BBB')
#ไม่มีคำสั่งreturn
def funcB( ) :
    print(111)
    funcA( )

funcA( ) 
funcB( )    