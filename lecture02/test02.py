#ต่อข้อมูลหลายประเภทเข้าด้วยกัน
#(,)
score = 55
print('EIEI',20,True,777.22,10/2,"DDD",score)
#(+)
print('EIEI'+str(20)+str(True)+str(777.2)+"DDD"+str(score))
#Format
print('EIEI {} {} {} {} DDD'.format(20,True,777.2,score))
#F string
print(f'EIEI... {20} {True} {777.22} {10/2} DDD {score}')
#Modular operator (%)
print('EIEI %d %f DDD' % (20,777.22) )