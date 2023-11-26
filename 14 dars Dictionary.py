# 14 Dars Dicitionary

# Lugatni boshqa turlardan farqi yani integer, float h.klardan farqi endi biz bir lugatdagi malumotlarni saqlash uchun kalit soz va qiymatdan foydalanamiz.
# Huddi lugatday soz va uning izohi Pythonda ham lugat shu tarzda ishlaydi. 
# Yani har bir malumot ikki qismdan iborat. Kalit soz va qiymat(KEY-VALUE-PAIR) kalit soz va qiymat juftligi
# Masalan: Mashina uchun lugat yasaymiz va uning ichiga bir nechta mashina haqida malumotlarni saqlaymiz.

#car_0 = {'model':'ferrari' , 'rang':'qizil'  }

#Bu ikkisi kalit soz va qiymat juftligi deb ataladi
# MODEL (kalit soz) vs FERRARI (izoh)

#---------------------------------------------------------------------------------------

#Agar lugat ichidan biror bir qiymatni chiqarib olmoqchi bolsa unda :
#print(car_0['model'])
#print(car_0['rang'])

#Natija : 
    #ferrari
    #qizil
    
#------------------------------------------------------------------------------

en_uz={'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}
#print(en_uz)
#print(en_uz['apple'])
#print(en_uz['apricot'])
    
#Natija: 
    #olma
    #o'rik
    
#------------------------------------------------------------------------------

#mevalar={'olma':10000, 'tarvuz': 80000, 'qovun':10000}
#print(f"Olma narxi {mevalar['olma']} so'm ")

#Natija : Olma narxi 10000 so'm
#print(mevalar['qovun'])
#natija : 10000

#Bu yerda royxatdan farqli ravishda [] qavsni ichida royxatdagi elementlarni indexini korsatgan edik
# Lugatda esa index orniga kalit sozni korsatyapmiz
#------------------------------------------------------------------------------

#LUGATDA ISTALGAN MALUMOT TURLARINI SAQLASH MUMKIN

#talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000,}
#Bu yerda talaba haqida bir nechta malumot turlaridan foydalanib malumot yegyapmiz.

#Agar code juda ham uzun bolib ketsa \ operatoridan foydalanamiz.

#print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tugilgan,\
# {talaba_0['yosh']} yoshda")
    
#Natija: 
#Murod Olimov, 2000-yilda tugilgan, 20 yoshda
    
#------------------------------------------------------------------------------
#YANGI KALIT SOZ VA QIYMAT QOSHISH

#Consoleda print(talaba_0) qilsak 
#{'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000}

#Bu yerda 3ta element bor. ism, yosh, t_yil kalit soz deylik yangi kalit sozlar qoshmoqchimiz.
#Buning uchun 

#talaba_0 ['kurs'] = 4 
#talaba_0 ['fakultet'] = 'informatika'    

#consoleda natija : 
#print(talaba_0)
# {'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000, 'kurs': 4, 'fakultet': 'informatika'}
#------------------------------------------------------------------------------

#QIYMATNI OZGARTIRMOQCHI BOLSAKCHI 

#talaba_0['ism'] = 'abdulloh'

#Natija: print(talaba_0)
#{'ism': 'abdulloh', 'yosh': 20, 't_yil': 2000, 'kurs': 4, 'fakultet': 'informatika'}

#------------------------------------------------------------------------------
#Dasturlash davomida bazida bosh lugat yaratib uni toldirib borishmiz mumkin yoki foydalanuvchi toldirishi mumkin.

#talaba_1 = {} # bosh lugat yaratish uchun bizga {} ozi yetadi 
#talaba_1['ism'] = 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#Natija: 
    #{'ism': 'qobil rasulov', 'kurs': 3, 'yosh': 20}
    #Talaba Qobil Rasulov 3-kurs
    
#talaba_1['kurs'] = 4 
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")

#Mana endi talaba 4 kursga ozgarib qoldi    

#------------------------------------------------------------------------------
#LUGATDAN BIROR BIR ELEMENTNI OCHIRISHNI KORAMIZ 

#talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil': 2000}
#del talaba_0['yosh']             #del ochirish funksiyasi
#print(talaba_0)

#natija: {'ism': 'murod olimov', 't_yil': 2000}  yosh yoq etibor bersak
    
# consoleda print(en_uz)
# {'apple': 'olma', 'apricot': "o'rik", 'banana': 'banan'}

# del en_uz['banana']

# print(en_uz)
# {'apple': 'olma', 'apricot': "o'rik"}   
#Mana shunday qilib kalit soz yordamida ochirib tashlashimiz mumkin 
    
#------------------------------------------------------------------------------

#LUGATLARNI BIR NECHTA QATORGA BOLIB YOZISH
#Agar bizda malumotlar uzun bolsa biz ularni bir nechta qatorga bolib yozishimiz ham mumkin

telefonlar = {
    'ali':'iphone X',
    'vali':'galaxy s9',
    'olim':'mi 10 pro', 
    'orif': 'nokia 3310'
    }

#yuqorida  bitta odam haqida bir nechta malumotlarni jamlagan edik. Bu yerda esa bir nechta odamlardan bir turdagi malumotlarni yegish ni koryapmiz

#consoleda 
# telefonlar['ali] desak iphone X kelib chiqadi

#Bu yerda lugat ichidagi biror bir malumotni chiqarib olish uchun biz kalit sozlar bilan murojat qilayapmiz
#Deylik men telefonlar [hasan] deb murojat qilsam 

#natija: KeyError: 'hasan'  kalit sozda hato deyapti 
#Mana shunday xatolikni oldini olish uchun biz GET metodidan foydalansak boladi.

#GET METODI bu ham lugatni ichidan biror malulmotni olish usuli

#phone = telefonlar.get('ali', 'Bunday ism mavjud emas')
#print(phone)
#natija iphone X

#meva = en_uz.get('apple', 'Bunday meva mavjud emas')
#print(meva)

#natija : olma 

#meva = en_uz.get('pineapple', 'Bunday meva mavjud emas')
#print(meva)
#natija: Bunday meva mavjud emas

#GET + kalit soz (agar bolmasa) mavjud emas xabarini qaytarish

#yoki bosh qoldirshimiz ham mumkin masalan
phone = telefonlar.get('hasan',)
print(phone)

#natija: None (mavjud emas)

































   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
