# 18 dars WHILE va RO`YXATLAR

# =============================================================================
# print('Yaqin do`stlaringiz ro`yxatini tuzamiz.')
# ismlar = []
# n=1  #ismlarni sanash uchun o`zgaruvchi
# while True:
#     savol = f"{n}-do`stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo`shasizmi? (ha/yo`q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
#     
# print("Do`stlaringiz ro`yxati:")
# for ism in ismlar:
#     print(ism.title())    

    

# Yaqin do`stlaringiz ro`yxatini tuzamiz.
# 1-do`stingiz ismini kiriting:borya
# Yana ism qo`shasizmi? (ha/yo`q)ha
# 2-do`stingiz ismini kiriting:ota
# Yana ism qo`shasizmi? (ha/yo`q)ha
# 3-do`stingiz ismini kiriting:abduhalil
# Yana ism qo`shasizmi? (ha/yo`q)ha
# 4-do`stingiz ismini kiriting:baxrom
# Yana ism qo`shasizmi? (ha/yo`q)yo`q
# Do`stlaringiz ro`yxati:
# Borya
# Ota
# Abduhalil
# Baxrom
# =============================================================================

# =============================================================================
# print("Do`stlaringiz yoshini saqlaymiz.")
# dostlar = {}  #royxat yaratib oldik
# ishora = True  # ishora yordamida toxtatmoqchimiz
# while ishora:  # bu yerda true va u toki false bolgunga qadar bajariladi
#     ism = input("Do`stingiz ismini kiritng:")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")  
#     dostlar[ism] = int(yosh)  #dostlar lugat(ism kalit)  yodh esa qiymat
#     
#     javob = input("Yana ma`lumot qo`shasizmi (ha/yo`q)")
#     if javob == "yo`q":
#        ishora = False   #yoq desa tsiklimiz toxtaydi
#     
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

    

# Do`stlaringiz yoshini saqlaymiz.
# Do`stingiz ismini kiritng:borya
# Boryaning yoshini kiriting: 28
# Yana ma`lumot qo`shasizmi (ha/yo`q)ha
# Do`stingiz ismini kiritng:abduhalil
# Abduhalilning yoshini kiriting: 28
# Yana ma`lumot qo`shasizmi (ha/yo`q)yo`q
# Borya 28 yoshda
# Abduhalil 28 yoshda    
# =============================================================================

#print(dostlar)
#{'borya': 28, 'abduhalil': 28}     lugat va kalit 
    
#--------------------------------------------------------------------------

# WHILE tsikli yordamida bir nechta royxatlarni ochirishni organamiz

# biz royxat bilan ishlashda .remove ni korgan edik ammo uning kamchiligi
# agar royxatda bir xil narsa kop bolsa faqat birinchi kelgan bittasini ochirib tashlaydi

#cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
#while 'nexia' in cars:   #toki nexia bor ekan royxatda 
#    cars.remove('nexia')  # bu operatorni bajar
#print(cars)    

#  natija:    ['lacetti', 'toyota', 'audi', 'malibu']    

#----------------------------------------------------------------------------------

 
# ha deb mashina nomini yozavermaslik uchun car deb ozgaruvchi berib qoysak boladi

# =============================================================================
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia', 'lacetti']
# car = 'lacetti'
# while 'car' in cars:   #toki nexia bor ekan royxatda 
#     cars.remove(car)  # bu operatorni bajar
#     
# print(cars)
# 
# 
# ?????????????????????????????????????
# 
# =============================================================================


# =============================================================================
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:         # toki talabalar ichida bitta element bolsa ham pastdagi tsiklni bajar deyapmiz
#     talaba = talabalar.pop()    # royxatdan pop yordamida bitta elementni sugurib olyapmiz va talabaga yuklayapti odatda oxxiridan boshlaydi
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)    #talaba ism baho qiymat boladi
# 
# Botirning bahosini kiriting: 5
# Botir baholandi
# Olimning bahosini kiriting: 2
# Olim baholandi
# Husanning bahosini kiriting: 4
# Husan baholandi
# Hasanning bahosini kiriting: 4
# Hasan baholandii
# 
# Endi consoleda print(talabalar) qilsak [] bosh royxat beradi sababi tugadi toyxat ichidagilar    
# Aksincha agar print(baholangan_talabalar) chiqarsak endi
# {'botir': 5, 'olim': 2, 'husan': 4, 'hasan': 4}   elementlar 4 ta boldi
# 
# =============================================================================

  





























   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    