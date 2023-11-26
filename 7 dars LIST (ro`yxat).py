mevalar = ['olma' , 'shaftoli' , "o'rik" , 'gilos' ]
narxlar = [12000, 15000, 25000, 30000, -25, 63.2]
sonlar = ['bir' , 'ikki' , 1, 2, 3]
ismlar = []

#Pythonda yokida umuman deyarli hamma dasturlash tillarid sanash 0 dan boshlanadi

#print(mevalar[0])
#olma

#print(narxlar[3])
#30000

#Shuningdek biz teskarisiga ham sanay olamiz yani -1 qilsak royxat oxxiridagi elementni chaqirgan bolamiz
#print(mevalar[-1])
#gilos

#shuningdek biz avvalgi darslarimizda matn uchun foydalangan kodlarimizni buyerda ham foydalana olamiz

#print(mevalar[2].upper())
#O'RIK

#print(mevalar[1].title())
#Shaftoli

#Sonlar bolgani uchun ularning ustida turli xil arifmetik amallarni ham bajarishimiz mumkin

#narxlar [1] + narxlar [2]
#Out[17]: 40000

#narxlar [1] + 25000
#Out[18]: 40000

#Shuningdek biz royxatni ichidagi malumotlarni ham ozgartirishimiz mumkin

#mevalar
#Out[24]: ['olma', 'shaftoli', "o'rik", 'gilos']

#mevalar[0] = 'anor'

#mevalar
#Out[26]: ['anor', 'shaftoli', "o'rik", 'gilos']

#mevalar[-1] = 'uzum'

#mevalar
#Out[30]: ['anor', 'shaftoli', "o'rik", 'uzum']

# .append()

#Royxatning ichiga malumot qoshsak ham boladi buning uchun bizga .append() kerak boladi

#mevalar.append("o'rik")

#mevalar
#Out[33]: ['anor', 'shaftoli', "o'rik", 'uzum', "o'rik"]

#.append har doim royxatning oxxiriga malumot qoshadi

# .insert

#Shuningdek biz royxatning malum bir joyiga boshiga ortasiga malumot kirgizmoqchimiz
#Buning uchun biz .insert dan foydalanamiz

#mevalar.insert(0,'banan')

#mevalar
#Out[42]: ['banan', 'anor', 'shaftoli', 'gilos', 'uzum', "o'rik"] # boshiga qoshildi

#mevalar.insert(3, 'ananas')

#mevalar
#Out[44]: ['banan', 'anor', 'shaftoli', 'ananas', 'gilos', 'uzum', "o'rik"]
#Endi esa ortasiga qoshildi

# del

#Royxatdan biror malumotni ozgartirmoqchi bolsak  del dan foydalanamiz

#del cars[2]   indexini beramiz

#cars
#Out[56]: ['Lacetti', 'Nexia', 'Malibu'] mana bittasi ochib ketti

#endi qoshish uchun yana cars.insert(2, 'cobalt') yozamiz

# va bizga u quyidagi natijani beradi

#cars
#Out[61]: ['Lacetti', 'Nexia', 'Cobalt', 'Malibu']

#Deylik royxat juda uzun va biz ochirmoqchi bolgan narsamizni indexini bilmaymiz
#Bu holatda remove dan foydalanamiz yani

#cars.remove('Nexia')

#cars
#Out[64]: ['Lacetti', 'Cobalt', 'Malibu']

#Remove metodi royxatda faqatgina birinchi uchragan malumotnigina ochirib yuboradi malasan

hayvonlar = ['it' , 'mushuk' , 'sher' , 'jirafa' , 'ot', 'mushuk',]

#hayvonlar.remove("mushuk")

#hayvonlar
#Out[69]: ['it', 'sher', 'jirafa', 'ot', 'mushuk']

# korib turganimizdek royxatda birinchi uchragan makumotnigina ochirib yubordi

# hammasini ochirish uchun bu metodni qayta qayta takrorlashimizga togri keladi

bozorlik = ["yog`" "un" "piyoz" "banan" "go`sht"]  
mahsulot = bozorlik.pop(3) #Royxatdan sug`urib oladi.

print("Men " + mahsulot + " sotib oldim")  # Natijasi Men banan sotib oldim chiqadi
print("Olinmagan mahsulotlar : " , bozorlik)

#natija
#Men banan sotib oldim
#Olinmagan mahsulotlar :  [”yog’”, “un”, “piyoz”, “go`sht”]

