# 13
#Avvalgi darsda if else haqida dars otgan edik agar shartimiz togri bolsa birtta shart notogri bolsa boshqa shart bajariladi
# if else ning kamchiligi biz faqatgina bitta shartni tekshirib kora olamiz holos.

#son = 50
#if son<0:
#    print("Manfiy son")
#else:
#    print("Musbat son")

# natija 
# Musbat son deb chiqib keladi consoleda
# korib turibmizki if else bilan bitta shartni tekshirib kora olyapmiz holos.


#---------------------------------------------------------------------------------------




# endi pastdan bir necca shartni tekshirishni organamiz 

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    print('Sizga kirish bepul.')
#elif yosh<=12:
#    print('Sizga kirish 5000 so\'m')
#elif yosh<=18:
#    print("Sizga kirish 8000 so'm ")
#else:
#    print('Sizga kirish 10000 so\'m')
    
 # elif ni biz istalgancha qoyishimiz mymkin 
    
 # buyerda korib turganimizdek print ni kop ishlatayapmiz uning orniga biz ....
 
#yosh = int(input(' Yoshingiz nechchida? '))
#if yosh<=4:
#     narx = 0
#elif yosh<=12:
#     narx = 5000
#elif yosh<=18:
#     narx = 8000
#else:
#     narx = 10000
 
#print(f"Sizga kirish {narx} so'm ")
      
# Bu usulning kamchiligi bu shartlardan birortasi bajarilsa qolganlarini tekshirib otirmaymiz 


#----------------------------------------------------------------------------------------



# Lekin bazida shunday holar boladiki bizdan bir necta shartlarni bajarishga togri kelishi mumkin
# buni bajarish uchun bizda OR hamda AND operatorlari bor 
#kun = input('Bugun nima kun ? >>>')
#if kun.lower()=='shanba' or kun.lower()=='yakshanbaga':
#   print('Bugun dam olish kuni.')
#else:
#    print('Bugun ish kuni. ')
    
# korib turibmizki bu yerda or operatori yordamida birdaniga ikkita shartni tekshirayapmiz
# bu ikki shartdan qaysi biri togri bolsa ham mana bu yuqoridagi code bajariladi.  




#---------------------------------------------------------------------------------------




# endi AND operatori bu ham bir nechta shartni bajarishda ishlatiladi

#kun = input('Bugun nima kun? >>>')
#harorat = float(input('Havo harorati qanday ?'))

#if kun.lower()=='yakshanba' and harorat>=30:
#    print('Cho`milishga kettik!')
#elif kun.lower()=='yakshanba' and harorat<=30:
#    print('Uyda qolamiz !')
    
# AND operatoini OR operatoridan farqi ikkala shart ham togri kelishi kerak code bajarilishi uchun  ikkala shart ham true qiymat qaytarish kerak
# demak chomilgani kettik deyish uchun kun yakshanba va harorat 30dan baland bolishi kerak

#------------------------------------------------------------------------------




# Biz and va or operatorlarini birga qoshib ham ishlatishimiz mumkin
#kun = input('Bugun nima kun? >>>')
#harorat = float(input('Havo harorati qanday ?'))

#if (kun.lower()=='yakshanba' or kun.lower()=='shanba' ) and harorat>=30: 
#  print('Cho`milgani kettik !')
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#  print('Uyda dam olamiz')
    

#korib turganimizdek OR va AND operatorlarini ishlatib bir necta shartlarni ham bajarasak boladi

#---------------------------------------------------------------------------------








#BOOLEAN = Ma`lumotlar turi
# Bu mantiqiy malumot turi bolib avvalda biz string float integer tanishgan edik boolean ham shularga oxshash 


#print(kun)
#yakshanba

#kun =='yakshanba'
#Out[27]: True

#Manashu true ni biror bir ozgaruvchiga yuklab qoyishimiz mumkin

#-----------------------------------------------------------------------------------






#Restoran uchun dastur yaratamiz 

#narx = 15000   mijoz 15ming somga taom oldi
#choy = True       mijoz choy ham oldi
#salat = False         mijoz salat olmadi

#if choy and salat:        agar mijoz choy ham salat ham olgan bolsa
#    narx = narx + 10000     narxga 10 ming som qoshamiz 
#elif choy or salat:        agar choy yoki salat olgan bolsa
#    narx = narx + 5000      narxga 5 ming som qoshamiz
    
#print(f"Jami {narx} so`m")    yakuniy narx chiqaramiz
      
#Agar yuqorida salatni ham true qilib qoysek unda natija 20000 som emas 25000 som chiqadi


#Lekin bu if elif zanjirining kamchiligi bitta shart bajarilsa python boshqa shartlarni tekshirb otirmaydi

#----------------------------------------------------------------------------





#Agar bizdan bir necta shartlarni bajarish talab qilinsachi 

#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
    
#print(f"Jami {narh} so'm")

#Bir necta iflardan foydalansek boladi va python hammasini alohida birma bir tekshirb chiqadi 

#natija 

#Mijoz choy oldi.
#Mijoz non oldi.
#Mijoz kompot oldi.
#Jami 25000 so'm

#shu orinda yuqoridagi true false ning orniga 1 yoki 0 qoyib ketishmiz ham kumkin
#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = 1
#salat = 0
#non = 1
#kompot = 1
#assorti = 0
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
    
#print(f"Jami {narh} so'm")

#Bu holatda ham code ishlayveradi natija bir xil 

#-----------------------------------------------------------------------------


#console da
#menu = [ 'osh' , 'qazon kabob' , 'shashlik' , 'norin' , 'somsa' ]
#'manti' in menu
#'somsa' in menu 

#Deb yozsek  natija  
#'manti' in menu
#Out[9]: False

#'somsa' in menu
#Out[10]: True 




#-----------------------------------------------------------------------------

#menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
#    print('Buyurtmangiz qabul qilindi')
#else:
#    print("Afsuski bizda bunday ovqat yo`q")



# Natija
#Nima ovqat yeysiz?>>>osh
#Buyurtmangiz qabul qilindi

#Nima ovqat yeysiz?>>>shorva
#Afsuski bizda bunday ovqat yo`q

#-------------------------------------------------------------------------------





# NOT IN operatori 

#not in operatori yordamida esa biror element royxatda yoqligini tekshiramiz masalan

#menu = ["osh" , "qozonkabob" , "shashlik" , "norin" , "somsa"]
#"manti" not in menu
#Natija True beradi yani manti yoqmi deyapmiz va javobda true togri yoq deyapti

#huddi shu joyiga agar 
#'osh' not in menu desam 
#False deydi yani xato osh bor toyxatda deydi


#-----------------------------------------------------------------------------------






#menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
#ovqat = input('Nima ovqat yeysiz ?>>>')
#if ovqat.lower() not in menu:
#    print("Afsuski bizda bunday ovqat yo`q")
#else:
#    print('Buyurtmangiz qabul qilindi.')
    

#not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin.
# Misol uchun: if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi.

#------------------------------------------------------------------------------




#IKKI ROYXATNI SOLISHTIRISH
  
#Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:
    
#menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
#buyurtmalar = ["osh" , "somsa" , "manti" , "shashlik"]

#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo`q")
    
#Natija     
#    Menuda osh bor
#    Menuda somsa bor
#    Kechirasiz, menuda manti yo`q
#    Menuda shashlik bor
    
#--------------------------------------------------------------------------------


#ROYXAT BOSH EMASLIGINI TEKSHIRISH

#Yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur qilyapmiz. 
#Lekin foydalanuvchidan bo'sh ro'yxat kelsachi? Demak for tsiklini bajarishdan avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak.
#Buning uchun avvalgi kodimizni quyidagicha o'zgartiramiz:


menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
buyurtmalar = ['osh' , 'somsa' , ',manti' , 'shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh!")
    
    
#Demak if royxat_nomi: ifodasi agar ro'yxatda bir dona element bo'lsa ham TRUE qiymat qaytaradi, aks holda FALSE qiymatini qaytaradi.




























































