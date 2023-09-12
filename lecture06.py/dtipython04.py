#if-else-if
score = int( input('ป้อนคะเเนน : ') )
if score >= 80 :
    print('ได้เกรดA')
elif score >= 70 and score < 80 :
    print('ได้เกรดB')
elif score >= 60 and score < 70 :
    print('ได้เกรดC')
elif score >= 50 and score < 60 :
    print('ได้เกรดD')
#elif score < 50 : หรือ
else :
    print('ได้เกรดF')
    print('-------------')
    print('Created by ELLE')