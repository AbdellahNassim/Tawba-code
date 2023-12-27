from multiprocessing import Pool
import math
def Be():
    while(True):
        print("Be")
        print("1")
        print("Amen")
def armagedon():
    while(True):
        print("armagedon")
        print("2")
        print("Amen")
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
if __name__ == '__main__':
    with Pool(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))) as p:
        p.map(Be, range(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))))
    with Pool(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))) as p:
        p.map(armagedon, range(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))))