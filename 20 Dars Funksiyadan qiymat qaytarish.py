#20 - dars Funksiyadan qiymat qaytarish

#def toliq_ism_yasa(ism, familiya):
#    """toliq ism qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    print(toliq_ism)
    
#toliq_ism_yasa('Olim', 'Dalimov')
# result Olim Dalimov

#Bu funksiyani kamchiligi shundaki biz  print(toliq_ism) foydalana olmaymiz     
# va dastur davomida nu bizga qayta qayta kerak bolishi mumkin
# qanday qilib biz buni biror ozgaruvchiga saqlab olishimiz mumkin


# =============================================================================
# def toliq_ism_yasa(ism, familiya):
#     """toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism     # print orniga 
#     
# toliq_ism_yasa('Olim', 'Dalimov')  
# 
# =============================================================================
#Buni bajarsak consolega hech narsa chiqmaydi sababi toliq_ism funksiyaning ichidabolgani uchun bu 
# Local variable (mahalliy ozgaruvchi) deyiladi
# siz funksiya ichidagi yaratgan variable ushani ichida qoladi
# Chiqarish uchun biz uni boshqa ozgaruvchiga yuklab olishimiz kerak

#talaba = toliq_ism_yasa('Olim', 'Dalimov') 

# Consoleda bajarsak endi chiqadi
#print(talaba)
#Olim Dalimov

#RETURN
#return bizga ozgaruvchinung qiymatini qaytaradi ozgaruvchining ozini emas

#---------------------------------------------------------------------------------

# Bu usuldan kelajakda foydalansak boladi masalan

# =============================================================================
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")
# # Darsga kelmagan talabalar olim hakimov va hakim olimov
# print(f"{talaba1} darsga kechikib keldi")  #olim hakimov darsga kechikib keldi
# 
# =============================================================================
# IXTIYORIY ARGUMENT

# =============================================================================
# def toliq_ism_yasa(ism, familiya, otasining_ismi= ''): #Ixtiyoriy qilib qoyishimiz mumkin
#     """toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#        toliq_ism =f"{ism} {familiya}"
#     return toliq_ism.title()
# 
# talaba1 = toliq_ism_yasa('olim', 'dalimov')
# talaba2 = toliq_ism_yasa('eshmat', 'toshmatov', 'boltaboyevich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# 
# #Darsga kelmagan talabalar: Olim Dalimov va Eshmat Boltaboyevich Toshmatov
# 
# #funksiyadan royxat lugat son text koplab narsalarni qaytarishimiz mumkin
# # yuqorida bitta narsa qaytargan edik holos
# 
# =============================================================================


# =============================================================================
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
#  
# # malum bir ozgaruvchiga hech qanday qiymat berishni istamasak none deb ketamiz 
# # yaxshi tarafi kelajakda if dan foydalansak none false ni beradi mavjud emas degani
# # va bundan biz kelajakda foydalanishimiz mumkin
# 
# =============================================================================
# =============================================================================
# avto1 = avto_info('GM' , 'Malibu' , 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM' , 'Gentra' , 'Oq' , 'Mexanika' , 2016,15000)    
# avtolar = [avto1, avto2]   #avto1,2 ni avtolar degan royxat ichiga yuklayapmiz
# print('Online bozordagi mavjud avtomashinalar:')
# for avto in avtolar: #avtolar ichidagi har bir avto haqida malumotni chiqarmoqchimiz
#     if avto['narh']:
#         narh =avto['narh']
#     else:
#        narh = "Noma`lum"
# print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
#        
#          
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma`lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}") 
# 
# # natija 
# #Onlayn bozordagi mavjud avtomashinalar:
# #ora Malibu. Narhi: Noma`lum
# #Oq Gentra. Narhi: 15000 
# 
# =============================================================================

# =============================================================================
# # Funkiyadan royxat qaytarish
# # esingizda bolsa biz range() haqida gaplashgan edik range(0,10) bu shu sonlar oraligini qaytaradi
# # lekin u ozi chiqmaydi biz uni listga yukalshimiz kerak
# # list(range(0,10)) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# # ozimiz uchun range funksiya yasab olamiz 
# def oraliq(min,max):     # bizni range endi 2ta qiymat qabul qilib olyapti min va max
#     sonlar = []     #bosh royxat qilib oldik yuqoridagi sonlarni shu royxat ichiga joylaymiz   
#     while min<max:      #toki  min maxdan kichik ekan biz unga +1 qoshamiz
#         sonlar.append(min)
#         min += 1
#     return sonlar
# 
# print(oraliq(0,10))
# print(oraliq(10,21))
# #natija
# 
# #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# 
# # Funksiyalarni yaxsi tarafi biz buni bir nechta tsikllar bilan chaqirib qayta  qayta foydalanishmiz mumkin
 
# =============================================================================

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
     avto = {'kompaniya':kompaniya,
             'model':model,
             'rang':rangi,
             'korobka':korobka,
             'yil':yili,
             'narh':narhi}
     return avto




print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = [] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma`lumotlarni kiriting",end= '')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli:")
    rangi=input("Rangi:")
    korobka=input('Korobka:')
    yili=input('Ishlab chiqarligan yili:')
    narhi=input("Narhi: ")

 #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
 #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:  
     
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

 # Yana avto qo'shish-qo'shmaslikni so'raymiz


    javob = input("Yana avto qo'shasizmi? yes/no:")
    if javob == 'no':
         break
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
     if avto['narh']:
         narh = avto['narh']
     else:
         narh = "No`malum"
     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")

#Naija         

Quyidagi ma`lumotlarni kiritingIshlab chiqaruvchi: gm
Modeli:damas
Rangi:oq
Korobka:mexanika
Ishlab chiqarligan yili:2019
Narhi: 90000
Yana avto qo'shasizmi? yes/no:yes

Quyidagi ma`lumotlarni kiritingIshlab chiqaruvchi: gm
Modeli:nexia
Rangi:qora
Korobka:avtomat
Ishlab chiqarligan yili:2019
Narhi: 10000
Yana avto qo'shasizmi? yes/no:no

Salonimizdagi avtolar:
Oq Damas, avtomat korobka. Narhi: 90000
Qora Nexia, avtomat korobka. Narhi: 10000


























































           
    
    

















