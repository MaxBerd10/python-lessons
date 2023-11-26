# 24 dars Funksiyalar nomsiz funksiyalar

# oddiy funksiyada biz def nom(argument)  qilib pastdan return ifoda qilib qaytarayotgan edik
# Bu standart funksiya va u istalgancha uzunlikda bolishi mumkin

# Endi biz lambda funksiyasidan foydalanamiz (nomsiz) degani

# lambda argument: ifoda boladi argument esa chegaralanmagan arg1 arg2 h.k
# ifoda ham = arg1 arg2 arg3 bolishi mumkin
# Bunda faqatgina bitta boladi lambdada return shart emas

#import math

#uzunlik = lambda pi, r : 2*pi*r  #aylananing radiusi (uzunligi)
#print(uzunlik(math.pi,10))  #mathni ichidan pi oldik va radiusini 10ga teng dedik

# 62.83185307179586

#------------------------------------------------------------------------------

# x ning y chi darajasini hisoblaymiz

#kvadrat = lambda x, y : x ** y 
#print(kvadrat(3, 2))   #3ni 2 darajasi 9

#lambda nomsiz dedik lekin nega uzunlik yoki kvadrat deb nom berdik
# buning uchun biz uni qayerda ishlashini korishimiz kerak

#def daraja(n):
#    return lambda x : x**n    #(Bu yerda x nomalum uni lambda qayerdandir oladi)

# daraja(3)
# Out: <function __main__.daraja.<locals>.<lambda>(x)>

# Desak bizga lambda degan qandaydir funksiya qaytaryapti qaytaryapti 
# yuqoridagi darajamiz bu funksiya yasaydigan funksiya boldi

#kvadrat = daraja(2)     #kvadrat yasaydigan funksiya
# consoleda 

# kvadrat(3) desak 
# Out[17]: 9

#kub = daraja(3)      #daraja degan funksiyani chaqiramiz n ning orniga esa 3 ni beramiz
    
# kub(2)
# Out[19]: 8

#print(f"3-ning kvadrati {kvadrat(3)} ga ", 
#      f"kubi  {kub(3)} ga teng")

# natija   
# 3-ning kvadrati 9 ga  kubi  27 ga teng
# Demak lambda funksiyasidan boshqa funksiyalar ichida foydalanish juda qulay ekan

#------------------------------------------------------------------------------

#lambda funksiyasining 2 chi qulayligi 
# pythonda shunday funksiyalar bor ular argument sifatida boshqa funksiyalarni qabul qilib oladi va qandaydir funksiya qaytaradi
from math import sqrt            #sonning kvadrat ildizini hisoblaydi

sonlar = list(range(11))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ildizlar = list(map(sqrt, sonlar))
#print(ildizlar)
#map funksiyasi sonlarni oladida ularga sqrt ni qollaydi

#  [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]


def daraja2(x):   # istalgan sonni kvadratini qaytaradigan funksiya boldi
    """Berdilgan sonning kvadratini qaytaruvchi funksiya """
    return x*x

#Endi avval yaratgan sonlarimizni kvadratini hisoblab chiqaylik

#print(list(map(daraja2,sonlar)))  #map yordamida har bir sonning kvaadratini hisoblaymiz
# natija:     [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Bundan ham osson yoli bu lambda usuli
kvadratlar = list(map(lambda x:x*x, sonlar))
# Buyerda lambda funksiyamiz x yani bitta argument qabul qiladi va x*x qilib kopaytiradi
# map funksiya sonlarni oladi va ularni lambda funksiyaga uzatadi

#print(kvadratlar)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [4, 5, 6]     #bu yerda biz 4+7 5+8 6+9 qilmoqchimiz
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y, a,b))  # lambdaga 2ta argument beryapmiz
# x ni orniga a y orniga esa b ni qoyyapmiz
#print(a_plus_b)

#------------------------------------------------------------------------------

# Yana bir yangi funksiya
import random as r

sonlar = r.sample(range(100),10) #10ta tasodifiy sonlar royxatini olnoqchiman
#print(sonlar)
 
#def juftmi(x):
#    """ x juft bolsa true, aks xolda false qaytaradi"""
 #   return x%2==0   # 0 ga tengmi ?  deyapmiz va == mantiqiy qiymatlarni true yoki false qaytaradi

#juftmi(4)
# True

#juftmi(12345)
# False

# % bolish emas module deyiladi va sonning qoldigini chiqaradi topishga yodam beradi
# 4%2 6%2 = 0
# 5%2 = 1,   10%7 = 3

#------------------------------------------------------------------------------

#juft_sonlar = list(filter(juftmi,sonlar))
# sonlar royxatini ichidan juftmi funksiya yordamida malum bir sonlarni saralab oladi.
# va ularni ichidan juft sonlarni ajratib olmoqchimiz 

# FILTER funsiyasi ham mapga oxshab bitta funksiya va royxat qaytaradi

#[67, 61, 23, 15, 64, 82, 71, 56, 38, 97]

#juft_sonlar
#[64, 82, 56, 38]

#------------------------------------------------------------------------------


#Biz buni filter qilish uchun avval juftmi degan funksiya yaratib olgan edik
# Deylik bu funksiya bizga har doim ham kerak emas faqatgina bir marttalik edi holos
# Bu holarda biz lambda funksiyasidan foydalansak boladi

#juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
#(juft_sonlar)

#sonlarni olyapmizda agar qiymat 0 ga teng bolsa lambda true qaytaradi
#[93, 17, 46, 60, 78, 90, 9, 15, 73, 66]
#[46, 60, 78, 90, 66]

#------------------------------------------------------------------------------



# lambda dan nafaqat sonlar balki matnlar bilan ham ishlashimiz mumkin 
mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o`rik", 'tarvuz', 'qovun', 'banan']
harf = 'b'
mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
#print(mevalar_b)      #natija ['banan']

#"husan".startswith("h")
# True

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)
# uzunligi 5ta yo undan kam bolgan mevalarni ajratib olmoqchimiz

# natija: ['olma', 'anor', 'anjir', 'o`rik', 'qovun', 'banan']
















































