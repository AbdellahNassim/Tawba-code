from multiprocessing import Pool
import math

def Charity():
    print("O Allah you are the Answerer of prayers, I pray to you to give me what you will from money and sustanance and donate it in my stead to the needy of your kingdom. I trust that you have answered my prayers with excellence.")
    print("اللهم أنت مجيب الدعاء,اللهم إني أدعوك أن ترزقني ما شئت من المال و الرزق و أن تصدق به مكاني للمحتاجين من عبادك , إني أثق أنك قد أجبت دعائي بإفضل الإحسان") 


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
if __name__ == '__main__':
    with Pool(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))) as p:
        p.map(Charity, range(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))))