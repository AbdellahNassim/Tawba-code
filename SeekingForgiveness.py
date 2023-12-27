from multiprocessing import Pool
import math
def SeekForgiveness():
    while(True):
       print("اللهم اشهد أني استغفرت لأخي و أحببته في الله و أحببت أن يغفر الله لي و له")
       print("O Allah, bear witness that I have saught forgiveness for my brother and I love him for the sake of Allah and I love that Allah forgives me and him")
       print("اللهم اشهد أني استغفرت لأختي و أحببتها في الله و أحببت أن يغفر الله لي و لها")
       print("O Allah, bear witness that I have saught forgiveness for my sister and I love her for the sake of Allah and I love that Allah forgives me and her")
       print("اللهم احشرني معهم يوم لا ظل إلا ظلك")
       print("O Allah, gather me with them on the Day when there is no shade but Your shade")
       print("اللهم اجعلني خليلك الأبدي")
       print("O Allah, make me Your eternal friend")
       print("اللهم اجعلني خليلك في الجنة")
       print("O Allah, make me Your friend in Paradise")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب و اجعلني خليلك في الصراط")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning and make me Your friend on the bridge")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب و اجعلني خليلك في الصراط و اجعلني خليلك في الجنة")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning and make me Your friend on the bridge and make me Your friend in Paradise")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب و اجعلني خليلك في الصراط و اجعلني خليلك في الجنة و اجعلني خليلك في النعيم")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning and make me Your friend on the bridge and make me Your friend in Paradise and make me Your friend in bliss")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب و اجعلني خليلك في الصراط و اجعلني خليلك في الجنة و اجعلني خليلك في النعيم و اجعلني خليلك في الفردوس الأعلى")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning and make me Your friend on the bridge and make me Your friend in Paradise and make me Your friend in bliss and make me Your friend in the highest Firdaws")
       print("اللهم اجعلني خليلك في الجنة و اجعلني خليلك في الدنيا و اجعلني خليلك في القبر و اجعلني خليلك في الصحراء و اجعلني خليلك في العرض و اجعلني خليلك في الحشر و اجعلني خليلك في الحساب و اجعلني خليلك في الصراط و اجعلني خليلك في الجنة و اجعلني خليلك في النعيم و اجعلني خليلك في الفردوس الأعلى و اجعلني خليلك في الفردوس الأعلى من الجنة")
       print("O Allah, make me Your friend in Paradise and make me Your friend in this world and make me Your friend in the grave and make me Your friend in the desert and make me Your friend in the open and make me Your friend in the gathering and make me Your friend in the reckoning and make me Your friend on the bridge and make me Your friend in Paradise and make me Your friend in bliss and make me Your friend in the highest Firdaws and make me Your friend in the highest Firdaws of Paradise")
       print("اللهم إني أسألك الوسيلة و الفضيلة و أسألك الجنة و أعوذ بك من النار")
       print("O Allah, I ask You for the means of approach and virtue, and I ask You for Paradise and I seek refuge in You from the Fire")
       print("اللهم إني أسألك أعلى مرتبة عندك و أسألك كل ما قرب إليها من قول أو عمل و أعوذ بك من أسفل مرتبة عندك و أعوذ بك من كل ما قرب إليها من قول أو عمل")
       print("اللهم اجعلني مثلك في كل خير")
       print("O Allah, make me like You in every good")
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
if __name__ == '__main__':
    with Pool(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))) as p:
        p.map(SeekForgiveness, range(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))))