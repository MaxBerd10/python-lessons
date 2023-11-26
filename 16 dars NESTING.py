# 16 dars NESTING 
# Lugat ichida royxat, toyxat ichida lugat lugat ichida lugat

# =============================================================================
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'karobka':'avtomat'
#         }
# 
# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'karobka':'mexanika'
#         }
# 
# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'karobka':'mexanika'
#         }
# =============================================================================

#Endi tasavvur qiling biz bu malumotlarni foydalanuvchiga korsatmoqchimiz.
#Ha deb car0 deyavermasdan ozgatuvchi yaratib olamiz

#car = car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} -yil, {car['narh']}$")
#Qztorimiz uzun bolib ketsa qator tashlab yangi qatordan yozishimiz mumkin f string bilan
# natija
#Lacetti, oq rang, 2018 -yil, 13000$
# teppada car0 ni car1 car2 qilib ozgartirsak malumot ozgarib boraveradi
#Nexia 3, qora rang, 2015 -yil, 9000$
#Gentra, qizil rang, 2019 -yil, 15000$

#Va bu noqulay sababi hamamsini birma bir bajarishim va ozgaruvchi nomini yodlab qolishim kerak
#AGar hamma moshina haqida malumotni birdaniga chiqaramaan desam codim uzun bolib ketadi

#car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} -yil, {car['narh']}$")

#car = car1
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} -yil, {car['narh']}$")

#car = car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} -yil, {car['narh']}$")

#Natija
#Lacetti, oq rang, 2018 -yil, 13000$
#Nexia 3, qora rang, 2015 -yil, 9000$
#Gentra, qizil rang, 2019 -yil, 15000$

#Lekin bu juda ham uzun


# cars = [car0, car1, car2] # Deb royxat yaratib oldik. Demak biz 3ta lugatni bitta royxat ichiga soldik
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']} - yil, {car['narh']}$")


#Natija 
#Lacetti, oq rang, 2018 - yil, 13000$
#Nexia 3, qora rang, 2015 - yil, 9000$
#Gentra, qizil rang, 2019 - yil, 15000$

#Ana endi man hammasini eslab qolishim shart emas cars ichiga kirib ketti hammasi
#Hamda codimiz anchagina qisqa boldi yuqoridagiga nisbatan

#consoleda agar cars desak
#cars
#Out[153]: 
#[{'model': 'lacetti',
#  'rang': 'oq',
#  'yil': 2018,
#  'narh': 13000,
#  'km': 50000,
#  'karobka': 'avtomat'},
# {'model': 'nexia 3',
#  'rang': 'qora',
#  'yil': 2015,
#  'narh': 9000,
#  'km': 89000,
#  'karobka': 'mexanika'},
# {'model': 'gentra',
#  'rang': 'qizil',
#  'yil': 2019,
#  'narh': 15000,
#  'km': 20000,
#  'karobka': 'mexanika'}]

#Bu yerda 3ta lugat bor alohida murojat qilishimiz uchun consoleda cars[0] [1] [2] deb murojat qilishimiz mumkin

#Deylik car0dagi model nomini chiqarmoqchi man 
#cars[0]['model']
#Out: 'lacetti'

#------------------------------------------------------------------------------

#FOR sikli yordamida bosh lugatlar royxatini ham  yaratib olishimiz mumkin

#malibus =[]
#for n in range(10):  #n 0-10 gacha bolgan qiymatlarni oladi
#    new_car = {
#        'model':'malibu',
#        'rang':None, #rangi noaniq
#        'yil':2020,
#        'narh':None,
#        'km':0,
#        'karobka':'avto'
#        }               #Bu sikl 10martta takrorlanadi range10
#    malibus.append(new_car)
    
#Buni bajarsak bizda 10ta bir xil natija chiqadi   

#malibus
#Out[158]: 

# [{'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'},
#  {'model': 'malibu',
#   'rang': None,
#   'yil': 2020,
#   'narh': None,
#   'km': 0,
#   'karobka': 'avto'}]

#Endi birinchi 3ta mashinaga rangini qizil qilib bermoqchimiz 

#for malibu in malibus [:3]:
#   malibu['rang'] = 'qizil'     #boshidagi har bir malibuni chaqirib olib uni rangini qizilga ozgartiramiz
    
#for malibu in malibus:
#    print(malibu)
#natija    
#{'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
#{'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
#{'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0,

# qolganlari esarangi nomalum endi qolganlarini ham rangini ozgartiramiz

#for malibu in malibus [3:6]:  #etibor bering 6 kirmaydi 
#    malibu['rang'] = 'qora'

#for malibu in malibus [6:]:
#    malibu['rang']='qora'
#    malibu['karobka']='mexanika'
    
#for malibu in malibus:
#    print(malibu)    
    

# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexanika'}

#Mana endi 3tasi qizilga qolgani qora va karobka mexanikaga ozgardi

#Agar avtomat bolsa narxini qimmatroq agar mexanika bolsa arzonroq qilib narx beramiz

#for malibu in malibus:
#    if malibu ['karobka']=='avto':
#        malibu ['narh'] = 40000
#    else:
#        malibu['narh']=35000
        
#for malibu in malibus:
#    print(malibu)      
    
#Natija

# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexanika'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexanika'}

#------------------------------------------------------------------------------

#ENDI NESTINGGA BOSHQA MISOL KORAMIZ
#LUGAT ICHIDA ROYXAT YARATAMIZ

#dasturchilar = {
#    'ali':['python','C++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['C++','C#']
#    }

#Agar bizga bitta kalitga bir nechta qiymatlar berish talab qilinsa biz mana shunday korinishda amalga oshirsak boladi

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#       print(til.upper())
        

# Ali quyidagi dasturlash tillarini biladi:
# PYTHON
# C++
 
# Vali quyidagi dasturlash tillarini biladi:
# HTML
# CSS
# JS
 
# Hasan quyidagi dasturlash tillarini biladi:
# PHP
# SQL
 
# Husan quyidagi dasturlash tillarini biladi:
# PYTHON
# PHP

# Maryam quyidagi dasturlash tillarini biladi:
# C++
# C#        

#Odatda print funksiyasi har bir amal bajarilganda ozi qator tashlab ketadi
#Buni oldini olish uchun end=''  argumentdan foydalanamiz masalan       

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(f'{til.upper()} ', end='')
        
# Ali quyidagi dasturlash tillarini biladi:
# PYTHON C++ 
# Vali quyidagi dasturlash tillarini biladi:
# HTML CSS JS 
# Hasan quyidagi dasturlash tillarini biladi:
# PHP SQL 
# Husan quyidagi dasturlash tillarini biladi:
# PYTHON PHP 
# Maryam quyidagi dasturlash tillarini biladi: 

#--------------------------------------------------------------

#NESTINGGA YANA BIR MISOL
#LUGAT ICHIDA LUGAT   
#Bunday qilish juda ham majbur bolmasangiz qilinmaydi sababi lugat juda ham murakkablashib ketadi uni ustida ishlash ham

hamkasblar ={
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o`rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items(): 
   print(f"\n{ism.title()} {info['familiya'].title()}, "
           f"{info['tyil']}-yilda tug`ilgan. "
           f"Ma`lumoti: {info['malumot']}. \n"
           "Quyidagi dasturlash tillarini biladi:")
     
     #Nesting bolib ketti
for til in info['tillar']:
    print(til.upper())

#Ali Valiyev, 1995-yilda tug`ilgan. Ma`lumoti: oliy. 
#Quyidagi dasturlash tillarini biladi:

#Vali Aliyev, 2001-yilda tug`ilgan. Ma`lumoti: o`rta-maxsus. 
#Quyidagi dasturlash tillarini biladi:

#Hasan Husanov, 1999-yilda tug`ilgan. Ma`lumoti: maxsus. 
#Quyidagi dasturlash tillarini biladi:
#PYTHON
#PHP    
    
#info deb biz hamkasblar ichidagi qiymatni oldik lekin infoni ozi ham lugat bolayapti
#CHunki bizda u ham alohida qiymat (familiya,tyil,malumot,tillar)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
           
 












