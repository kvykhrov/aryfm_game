import time
import random
import string


def aryfm():
    a = random.randint(2,11)
    b = random.randint(0,8)

    result = a*b

    line1 =  '%i  %i ' % (a,b)

    print line1

    time.sleep(random.randint(2,5))

    line2 = '#### =%i ####' % result
    centerarg = random.randint(14,25)
    print string.center(line2,centerarg)

for i in [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]:
    aryfm()
