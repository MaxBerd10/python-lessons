#15 Dars Lugat elementlari bilan ishlash 

#.items()

#talaba_0 = {
#    'ism':'alijon',
#    'familiya':'shamshiyev',
#    'yosh':'22',
#    'fakultet':'matematika',
#    'kurs':4
#    }

#talaba_0['ism']
#Out: 'alijon'

#talaba_0['yosh']
#Out: '22'

#Pythonda lugatlar katta bolishi mumkin kichkina bolishi mumkin 
#Yoki lugat ichidagi barcha malumotlarni yoki kalitlarni bilmasligimiz mukin bunday holatda nima qilamiz :
    
#  .items() metodi   (elementlar)  
#print(talaba_0.items())

#natija: dict_items([('ism', 'alijon'), ('familiya', 'shamshiyev'), ('yosh', '22'), ('fakultet', 'matematika'), ('kurs', 4)])

#manashu korinishda chiqdi lekin bu qulay yoki chiroyli bir korinishda chiqqani yoq 
#keling shuni chiroyli korinishda consoleda chiqaramiz 

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit:{kalit}")
#    print(f"Qiymat: {qiymat} \n")
    
#Kalit:ism
#Qiymat: alijon 

#Kalit:familiya
#Qiymat: shamshiyev 

#Kalit:yosh
#Qiymat: 22 

#Kalit:fakultet
#Qiymat: matematika 

#Kalit:kurs
#Qiymat: 4     

#------------------------------------------------------------------------------

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#    }

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")
    
#natija:
#    Alining telefoni iphone x
#    Valining telefoni galaxy s9
#    Olimning telefoni mi 10 pro
#    Orifning telefoni nokia 3310
    
#------------------------------------------------------------------------------

#Deylik bizdan faqat kalitlarni bilish talab qilinsa

#.keys() metodi lugat ichidagi har bir kalitni qaytaradi

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
#print(mahsulotlar.keys())
#natija: dict_keys(['olma', 'anor', 'uzum', 'anjir', 'shaftoli'])

#print('Do`kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#   print(mahsulot.title())
#natija : 
#Do`kondagi mahsulotlar:
#Olma
#Anor
#Uzum
#Anjir
#Shaftoli  

#------------------------------------------------------------------------------

#Bu yerda biz keys metodidan foydaladik aslida bundan foydalanmasak ham yani :
#print('Do`kondagi mahsulotlar:')
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())    
# code natjasi bir xil boladi
#Do`kondagi mahsulotlar:
#Olma
#Anor
#Uzum
#Anjir
#Shaftoli

#------------------------------------------------------------------------------

#bozorlik = ['anor', 'uzum', 'non', 'baliq']   #royxat yaratdik
#for mahsulot in mahsulotlar:         #dokondagi mahusulot bizni royxatda bormi yoqmi tekshiryapmiz
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so`m")
        
#natija         
#Anor 20000 so`m
#Uzum 40000 so`m
# Bizni royxatimizdagi narsadan dokonda faqat ikkitasi bor ekan
# non bilan baliq yoq ekan

#------------------------------------------------------------------------------
# Buning aksini ham qilishimiz mumkin 
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, dokoningizga {buyum} ham olib keling")
        
#Anor 20000 so`m
#Uzum 40000 so`m
#Iltimos, dokoningizga non ham olib keling
#Iltimos, dokoningizga baliq ham olib keling

#------------------------------------------------------------------------------

#Avvalgi darslarimizda aytgan edik biz kugatni ichiga malumotlarni qaysi tartibda kiritsek shu tartibda qoladi

#dict_keys(['olma', 'anor', 'uzum', 'anjir', 'shaftoli'])

#Lekin bizdan A-Z alfabit boyicha chiqarish talab qilinishi mumkin bunda biz .sorted() foydalanishimiz mumkin

#print("Do`kondagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())

#Do`kondagi mahsulotlar:
#Anjir
#Anor
#Olma
#Shaftoli
#Uzum 
# Endi bu yerda alfabit boyicha chiqib keldi 
#Lekin usha asosiy ildizi ozgargani yoq consoleda yozsak usha avval kiritganimizday chiqadi

#-------------------------------------------------------------------------------

# Endi bazida bizdan kalitlar emas balki qiymatlarni chiqarish talab qilinishi mumkin
# .values()


#telefonlar = {
#    'ali':'iphone X',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro', 
#    'orif': 'nokia 3310'
#    }
#print(telefonlar.values())
# natija

#dict_values(['iphone X', 'galaxy s9', 'mi 10 pro', 'nokia 3310'])

#----------------------------------------------------------------------------

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)
    
#Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
#iphone X
#galaxy s9
#mi 10 pro
#nokia 3310

#Endi buyerda faqatgina qiymatlar chiqib keldi

#-----------------------------------------------------------------------------

# Biroz royxatni kengaytiramiz 
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro', 
    'orif': 'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)

#Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
#iphone X
#galaxy s9
#mi 10 pro
#nokia 3310
#galaxy s9
#huawei p30
#iphone x
#iphone x
#---------------------------------------------------------------------------------
# Korib turibmizki iphone x bir nechta bor deylik elementlarni takrorlanmagan holda chiqarmoqchimiz
# Bunday holatda biz set() funksiyasidan foydalansak boladi
# Bu funksiya takrorlangan elementlarni olib tashlab har biridan bitta bittadan element qoldiradi

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#    print(tel)
    
#Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
#galaxy s9
#nokia 3310
#mi 10 pro
#huawei p30
#iphone x

# Ana endi hammasidan bittadan korsatdi
#------------------------------------------------------------------------------

#SET ham aslida Pythonda malumot turi hisoblanadi 
#royxat, lugat, toople(ozgarmas lugat) kabi SET ham ichida bir nechta malumotlarni saqlashga moljallangan

#SET yaratish uchun {} lardan foydalanamiz

toys = {"ball", "car", "lamp", "ball"}

#Etibor bering set ichidagi elementlar takrorlanmaydi
# print(type(toys))
#<class 'set'>             turini tekshirsak set deyapti

#print(toys)
#{'ball', 'lamp', 'car'} desak 3ta element turibdi bittasini tashlab yubordi













        





























  













































































