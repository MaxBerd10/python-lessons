 #ism = input("Ismingiz nima")
#savol = f"Salom, {ism.title()}. Yoshingiz nechchida? "
#yosh = input(savol)
#height = input("Bo`yingiz nechchi metr?")
#height = float(height)

#While (toki) tsikli 

#son = 1
#while son<=5:
#    print(son, end=' ')
#    son = son +1
    
#while and input

# =============================================================================
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kvadratini kiriting "
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"
# qiymat =''
# while qiymat != 'exit':
#       qiymat = input(savol)
#       if qiymat != 'exit':
#          print(float(qiymat)**2)
# print('Dastur tugadi')
# =============================================================================

#Foydalanuvchidan qiymat so'raganingizda input()ichidagi savolni aniq va tushunarli qilib yozing. 
#Masalan: input("Tug'ilgan yilingizni kiriting: ")

# WHILE TSIKLI bilan tanishamiz

#Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir ro'yxatni olib, ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni takrorlar edi. 
#while ham takrorlash operatori bo'lib, for dan farqli ravishda, toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi. 

# while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.   

#son = 1        # songa 1 qiymatini beramiz
#while son<=5:   # toki don 5 dan kichik yoki teng ekan.......
#    print(son, end=' ')    #son ni konsolga chiqaramiz,
#    son = son+1     # songa 1 qo`shamiz. 

#consoleda natija:  1 2 3 4 5 chiqadi

#Yuqoridagi kodni tahlil qilamiz:

#    avval son degan o'zgaruvchi yaratdik va unga 1 qiymatini berdik.
#    2-qatorda esa toki son 5 dan kichik yoki teng ekan 3-4-qatorlarni bajar dedik.
#    3-qatorda son ni konsolga chiqardik
#    4-qatorda son ga 1 qo'shdik.
#    4-qatordan so'ng kod yana 2-qatorga qaytadi va son<=5 shartini tekshiradi, agar shart bajarilsa 3-4 qator qayta-qayta bajarilaveradi.
#    5-qadamdan so'ng son=5 bo'lganda while tsikli to'xtaydi.
 
#Pythonda += operatori bor. Bu operator o'ng tarafdagi qiymatni chap tarafdagi qiymatga qo'shadi. Misol uchun, yuqorida son = son + 1 o'rniga son += 1 deb yozishimiz mumkin.

#------------------------------------------------------------------------------

# WHILE va INPUT() 

# Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarayotgan edi.
# While tsikli yordamida dasturni to`xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to`xtatish uchun 'exit' deb yozing): "  # +- teppadagi savolga yana qoshing degani
#qiymat = ''   #foydalanuvchi kiritsa yuklanadi bu yerga
#while qiymat != 'exit':       # != (teng bolmasa) degani
#    qiymat = input(savol)
#    if qiymat !='exit' :
#        print(float(qiymat)**2)
#print('Dastur tugadi')        
#Yuoqridagi dasturimiz toki foydalanuvchi exit deb yozguniga qadar takrorlanaveradi.

#Bu yerda while ssikli bajarilishi uchun bitta shart qoydik 
#Ammo bazida bizdan bir nechta shartni bajarish soralishi mumkin

#Deylik oyin oyin toxtash uchun shart otib qoyishi, portlashi, chuqurga tushub ketishi vaho kazo

#-------------------------------------------------------------------------

# Ishora (Flag)  ishora ozgaruvchi yaratib olamiz
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"
#ishora = True    #Toki ishora true bolguncha pastdagi code bajarilaveradi. Qachonki false bolsa bajarilishdan toxtaydi.
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False     #ishora false bolsa dastur toxtaydi
#    else:
#        print(float(qiymat)**2)
#print('Dastur to`xtadi!')

#------------------------------------------------------------------------------

#Dasturning toxtatish yollari kop hozir biz ishora yordamida toxtatish va shartni tekshirish yordamidaa toxtatishni kordik
# Break yordamida toxtatishni koramiz 

# =============================================================================
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to`xtatish uchun 'exit' deb yozing):"
# 
# while True:         #abadiy tsikl aylanaveradi
#     qiymat = input(savol)
#     if qiymat == 'exit':
#        break    #tsiklni toxtatish   qachonki qiymat exitga teng bolsa break ishlaydi
#     else:
#        print(float(qiymat)**2)
# print('Dastur to`xtadi')
# =============================================================================
       
# Break operatorini faqat while ssikl uchun emas for tsikli uchun ham qollashimiz mumkin
    
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")
    
# Natija 4gacha chiqdi uyogiga esa toxtadi    
#1 ning kvadrati 1 ga teng
#2 ning kvadrati 4 ga teng
#3 ning kvadrati 9 ga teng
#4 ning kvadrati 16 ga teng

#sababi teppada biz shart qoydik agar son 5ga teng bolsa break deb

#---------------------------------------------------------------------------------

# Breakning aksi ham bor bu CONTINUE
# biz bu bilan tsiklni ichida bitta qadam tashlab otib ketishimiz mumkin

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")

#natija 
#1 ning kvadrati 1 ga teng
#2 ning kvadrati 4 ga teng
#3 ning kvadrati 9 ga teng
#4 ning kvadrati 16 ga teng
#6 ning kvadrati 36 ga teng
#7 ning kvadrati 49 ga teng
#8 ning kvadrati 64 ga teng
#9 ning kvadrati 81 ga teng
#10 ning kvadrati 100 ga teng

# agar son 5ga teng bolsa continue dedik tsiklni boshiga qaytgin dedik

#----------------------------------------------------------------------------------------------

# WHILE ning ichida CONTINUE dan foydalanamiz

# =============================================================================
# son = 0
# while son<10:       #toki son 10dan kichkina ekan
#     son += 1
#     if son%2!=0:    # % sonni qoldigi bormi yomi tekshiradi va bu sonni juft yoki toq ekanligini tekshiradi
#         continue
#     else:
#         print(son)
# =============================================================================

#2
#4
#6
#8
#10

# Agar == qilsak 

#son = 0
#while son<10:       #toki son 10dan kichkina ekan
#    son += 1
#    if son%2==0:    # % sonni qoldigi bormi yomi tekshiradi va bu sonni juft yoki toq ekanligini tekshiradi
#        continue
#    else:
#        print(son)
# agar son son%2==0:  2 ga bolinsa continue boshiga qayt printni bajarma deyapmiz


#1
#3
#5
#7
#9

#endi toq sonlar chiqib keldi  %2 module 2 yordamida sonning qoldigi yoki juft yoki toqligini tekshiryapmiz

#----------------------------------------------------------------------------------------------


# Tsikllar bilan ishlashda biz abadiy tsikl yaratishdan ehtiyot bolishimiz kerak


#son = 0
#while son<10:
#    if son%2!=0:      #agar son toq bolsa boshiga qaytyapti
#        continue
#    else:
#        print(son)
# natija to`xtamay 00000000000 chiqaveradi 
# nima xato boldi biz songa +1 qoyish esimizdan chiqib qoldi       
# son += 1        

# =============================================================================
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:      #agar son toq bolsa boshiga qaytyapti
#         continue
#     else:
#         print(son)
# =============================================================================
        
#2
#4
#6
#8
#10

# =============================================================================
# son = 0
# while son<10:
#     if son%2!=0:      #agar son toq bolsa boshiga qaytyapti
#         continue
#     else:
#         print(son)
#     son += 1    
# =============================================================================

# natija 0 chiqadi lekin toxtamaydi stop qilishimiz kerak
# bu yerda nima xato boldi biz ornini alishtirib qoydik   son += 1 


#son = 1
#while son>0:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
        
# bunda ham code toxtamaydi ketaveradi  bu yerda xatolik  son>0 boldi       




savol = input('Maxkamning sevgilisi kim?')
if savol == 'Diyora':
    print('To`ppa to`g`ri')
else:
    print('Damingni olipsaan')
          
# =============================================================================




























   