# 22 Dars moslashuvchan funksiya (*args, **kwargs)

# Avvalgi darslarimizda biz min max funskiya yoki avto info funksiya yaratgan edik
# ularda 5ta yoki 6ta argument bor edi 7 chisini qoshsak ham 4 ta qilib qoysak ham error beradi

# Endi bu darsda biz shunday funksiya yarataylikki unga istalgancha argument qoshsa bolsin

#*args (arguments)

#def summa(*sonlar):           #ana endi foydalanuvchi istalgancha argument kiritisi mumkin
#    """Kiritilgan sonlarning yegindisini hisoblaydi"""
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi

#print(summa(1,2))    #2ta qiymat berdik
#print(summa(1,2,3,4,5))      #5ta
#print(summa(4,5,6,7))         #4 ta

#natija
#3
#15
#22    

# Endi consoleda istalgancha qiymat berishimiz mumkin

#summa(45,65,45,34,23,12,444)
#Out[69]: 668

#summa(100)
#Out[70]: 100

#summa()
#Out[71]: 0

# Ozi bu funksiya qanday ishlaydi mana foydalanuvchi istagancha qiymat kiritib yotipti
# yuqoridagi 1,2,3,4,5 har biri qiymarlar har biri funksiyani ichidagi alohida royxat ichiga joylanadi
# Tuple(ozgarmas roxyat) ichiga joylanadi


# Yoki pythonning ozini ichidagi tayyor sum funksiyasidan ham foydalanishimiz mumkin 
#def summa(*sonlar): 
#    """Kiritilgan sonlarning yegindisini hisoblaydi"""
#    return sum(sonlar)

#print(summa(2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))

#2
#15
#22 

#------------------------------------------------------------------------------

# Endi deylik bizda majbur argumentlar va ixtiyoriy argumentlar bolishi mumkin 

# =============================================================================
# def summa(x,y,*sonlar):   # bu holatda ozgaruvchan argumentni oxxirida yozishimiz kerak
# # va bu kamida 2ta argument qabul qiladi 1ta qilib qoysak xato beradi
#     """Kiritilgan sonlarning yegindisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))
# print(summa(2))    #Error summa() missing 1 required positional argument: 'y'
#     
# 
# =============================================================================


# IKKINCHI usul **kwards (Keyword Arguments) kalit sozli argumentlar
# Buni avvalgisidan farqi huddi lugat kabi kalit soz va qiymat korinishida qilishimiz kerak

def avto_info(kompaniya, model, **malumotlar):  #boshida ikkitasi majburiy
    """Avto haqidagi ma`lumotlarni lug`at ko`rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "Malibu", rang='qora', yil=2018)
#avto2 = avto_info("Kia", "K5", rangi='qizil', narh=35000, yil=2020)

# Funksiya qanday ishlaydi bu holatda
# Avvalo qoshimcha malumotlardan lugat yaratib oladi yuqorida u malumotlardir 
# pastdan esa biz kompaniya va model ni qoshganimiz uchun ular oxxiridan chiqdi   

# {'rang': 'qora', 'yil': 2018, 'kompaniya': 'GM', 'model': 'Malibu'}

#{'rangi': 'qizil', 'narh': 35000,'yil': 2020,'kompaniya': 'Kia','model': 'K5'}

# Biz istalgancha qoshishimiz mumkin masalan

avto2 = avto_info("Kia", "K5", rangi='qizil', narh=35000, yil=2020, korobka='avtomat')

{'rangi': 'qizil',
 'narh': 35000,
 'yil': 2020,
 'korobka': 'avtomat',  # qoshilib qoldi
 'kompaniya': 'Kia',
 'model': 'K5'}











