def example1( ) : 
    print(1111)
    print(2222)
    return
    print(3333)
    print(4444)
    return
#Default Parameter 
def dtitest(x, y, z = 20, a =10):
    print(f'{x} + {y} + {z} + {a} = {x+y+z+a}')

dtitest(5,100)

dtitest(9, 8 , 10)