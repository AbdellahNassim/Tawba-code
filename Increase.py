from multiprocessing import Pool
import math
def Increase():
    while(True):
       print("اللهم إني أسألك الجنة و أعوذ بك من النار")
       print("O Allah, I ask You for Paradise and I seek refuge in You from the Fire")
       print("اللهم ضاعف لي الأجر و الثواب")
       print("O Allah, multiply for me the reward and the good")
       print("اللهم إني أسألك العفو و العافية في الدنيا و الآخرة")
       print("O Allah, I ask You for forgiveness and well-being in this world and in the Hereafter")
       print("اللهم إني أسألك العفو و العافية في ديني و دنياي و أهلي و مالي")
       print("O Allah, I ask You for forgiveness and well-being in my religion, my worldly affairs, my family, and my wealth")
       print("اللهم إني أسألك العفو و العافية في ديني و دنياي و أهلي و مالي و من أحب"
             " اليه من الأمر الذي يقربني إليه")
       print("O Allah, I ask You for forgiveness and well-being in my religion, my worldly affairs, my family, my wealth, and for what I love of the matters that bring me closer to You")
       print("اللهم اغفر لي و ارحمني و عافني و اهدني و ارزقني")
       print("O Allah, forgive me, have mercy upon me, grant me well-being, guide me, and provide for me")
       print("اللهم اغفر لي و ارحمني و عافني و اهدني و ارزقني و ارفعني")
       print("O Allah, forgive me, have mercy upon me, grant me well-being, guide me, provide for me, and elevate me")
       print("اللهم أتنا في الدنيا حسنة و في الآخرة حسنة و قنا عذاب النار")
       print("O Allah, grant us good in this world and good in the Hereafter, and protect us from the punishment of the Fire")
       print("اللهم أتنا في الدنيا حسنة و في الآخرة حسنة و قنا عذاب النار و أدخلنا الجنة مع الأبرار يا عزيز يا غفار")
       print("O Allah, grant us good in this world and good in the Hereafter, and protect us from the punishment of the Fire and admit us into Paradise with the righteous, O Mighty and Forgiving One")
       print("اللهم أتنا في الدنيا حسنة و في الآخرة حسنة و قنا عذاب النار و أدخلنا الجنة مع الأبرار يا عزيز يا غفار و صل اللهم على محمد و على آل محمد كما صليت على إبراهيم و على آل إبراهيم إنك حميد مجيد")
       print("O Allah, grant us good in this world and good in the Hereafter, and protect us from the punishment of the Fire and admit us into Paradise with the righteous, O Mighty and Forgiving One. O Allah, send prayers upon Muhammad and upon the family of Muhammad as You sent prayers upon Abraham and upon the family of Abraham. Verily, You are full of praise and majesty")
       print("اللهم أسعدني بما رزقتني و اجعل لي و لوالدي حسنة تبلغني بها يوم القيامة")
       print("O Allah, make me happy with what You have provided me, and give me a good replacement for what I have lost")
       print("اللهم أسعدني بما رزقتني و اجعل لي و لوالدي حسنة تبلغني بها يوم القيامة و أعذني من عذاب القبر و عذاب النار و أدخلني الجنة مع الأبرار يا عزيز يا غفار")
       print("O Allah, make me happy with what You have provided me, and give me a good replacement for what I have lost, and protect me from the punishment of the grave and the punishment of the Fire, and admit me into Paradise with the righteous, O Mighty and Forgiving One")
       print("اللهم ضاعف حسناتي و حسنات والدي و حسنات من قال آمين")
       print("O Allah, multiply my good deeds and the good deeds of my parents and the good deeds of whoever said Ameen")
       print("اللهم ضاعف حسناتي و حسنات والدي و حسنات من قال آمين و ارحم والدي كما ربياني صغيرا")
       print("O Allah, multiply my good deeds and the good deeds of my parents and the good deeds of whoever said Ameen, and have mercy upon my parents as they raised me when I was young")
       print("اللهم اغفر لجميع الخلائق و ارحمهم و اعف عنهم و اهدنا و اهد بنا و اصلحنا و اصلح بنا و اجعلنا سببا لهدايتهم")
       print("O Allah, forgive all of the creation, have mercy upon them, pardon them, guide us and guide them, rectify us and rectify them, and make us a reason for their guidance")
       print("اللهم اغفر لجميع المسلمين و المسلمات و المؤمنين و المؤمنات الأحياء منهم و الأموات")
       print("O Allah forgive all muslims and muslimahs, believers and believers, the living and the dead")
       print("اللهم اغفر لجميع المسلمين و المسلمات و المؤمنين و المؤمنات الأحياء منهم و الأموات و ارحمنا و ارحمهم")
       print("O Allah forgive all muslims and muslimahs, believers and believers, the living and the dead, and have mercy upon us and have mercy upon them")
       print("اللهم اغفر لجميع المسلمين و المسلمات و المؤمنين و المؤمنات الأحياء منهم و الأموات و ارحمنا و ارحمهم و اعف عنا و عنهم")
       print("O Allah forgive all muslims and muslimahs, believers and believers, the living and the dead, and have mercy upon us and have mercy upon them, and pardon us and pardon them")

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
if __name__ == '__main__':
    with Pool(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))) as p:
        p.map(Increase, range(ackermann(math.pow(math.inf,math.inf),math.pow(math.inf,math.inf))))