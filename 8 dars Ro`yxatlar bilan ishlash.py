# 8 - dars **Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar (Tuples)**

#cars = [ 'bmw', 'mercedes benz', 'gm', 'tesla', 'volvo', 'audi']
#cars.sort()
#print(cars)
#malumotlarni alfabit boyicha qilishda yani A-Z cars.sort() funksiyasidan foydalanamiz
#bilamizki katta harflar doim birichi keladi shuning uchun  agar royxatda Bmw qilsak u birnchi keladi
#Natija cars.sort()
#print(cars)
#['Bmw', 'audi', 'gm', 'mercedes benz', 'tesla', 'volvo']

#bazida esa bizdan teskarisiga royxatimizni taklashga togri kelib qolishi mumkin bunda cars.sort(reverse=True) shundan foydalanamiz
#Natija:   ['volvo', 'tesla', 'mercedes benz', 'gm', 'bmw', 'audi']

#bazida royxatga tegmasdan ozgartirishimiz talab qilinishi mumkin

# bunda print(sorted(cars)) funksiyasidan foydalanamiz bunda bizda asl royxat ketma ketligi ozgarmaydi ammo konsoleda A~Z bolib chiqadi

# Natija: print(sorted(cars))

#['audi', 'bmw', 'gm', 'mercedes benz', 'tesla', 'volvo']

# asosiy malumot bazasida esa volvo

#tesla mercedes benz gm bmw audi shunday edi taxlanmagan xolatda va bu holatda biz asl royxatga tegmasdan ozgartirdik

#huddi shu xolatni asl royxatga tegmagan xolatda teskarisiga ham chiqarsek boladi
#print(sorted(cars, reverse=True)) natija: ['volvo', 'tesla', 'mercedes benz', 'gm', 'bmw', 'audi']

#sonlar bilan ham ishlay olamiz

#sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]
#print(sorted(sonlar))
#natija: [-7.2, -5, 1, 12, 23, 45, 56, 998]

# bu holatda ham asosiyda ozgarmaydi asosiyda ham ozgartimoqchi bolsa sonlar.sort() qilsak ozgaradi

# teskarisiga qilish un reverse dan ham foydalansak boladi sonlar.sort(reverse=True)

#ROYXATNI AYLANTIRIB QOYISH
#cars.reverse() qilsak  natijaa: ['bmw', 'mercedes benz', 'gm', 'tesla', 'volvo', 'audi'] chiqadi

#QANDAY QILIB ROYXAT UZUNLIGINI OLCHAYMIZ
#buning uchun len() funksiyasidan foydalanamiz
#len(cars)
#Out[31]: 6

#RANGE FUNKSIYASI range() malum bit oraliqdagi sonlarni qaytaradi misol uchun 1-10 gacha ramge(0, 10) bini royxatga otkazish uchun esa list(range(0,10))

#sonlar = list(range(0,10))

#sonlar
#Out[37]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] etibor berishmiz kerak 10gacha bogan sonlar kiradi 10 ni ozi kirmaydi

#list(range(0,11))
#Out[40]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#sonlar = list(range(0,11))

#sonlar
#Out[42]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#sonlar = list(range(1,11))

#sonlar
#Out[44]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Qadamni ham qilsak boladi maslan
#toq_sonlar = list(range(1,20,2))

#toq_sonlar
#Out[47]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#juft_sonlar

#juft_sonlar = list(range(0,20,2))

#juft_sonlar
#Out[51]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#sanash = list(range(0,101,10))

#print(sanash)
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#demak bizda toq va juft sonlar bor ular yordamida oddiy arifmetik amallarni bajarishimiz mumkin

# MAX MIN SUM

#sonlar
#Out[58]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#toq_sonlar
#Out[59]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#max_qiymat = max(toq_sonlar)

#max_qiymat #Out[61]: 19 demak toq sonlar ichidagi eng katta qiymat 19 ekan

narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]

#narxlar
#Out[63]: [12000, 22500, 23456, 9800, 5600, 9934, 32874]

#min(narxlar)
#Out[64]: 5600

#max(narxlar)
#Out[65]: 32874

#sum(narxlar)
#Out[66]: 116164  narxlarni umumiy qiymatini chiqarib berdi

arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon narx" , arzon, "Eng qimmati" , qimmat, "jami" , jami)

#ROYXATNI KESISH
#Avvalgi darslarimidan korgan edik biror bir elementni chaqirmoqchi bolsak masala: cars[0]

# qilar edik shunda bizga bmw chiqib keladi sababi u birinchida turibdi

#Lekin bazida bizdan royxatning malum bir qismini ajratib olish talab qilinishi mumkin
#rint(cars[0:3])
#'bmw', 'mercedes benz', 'gm']  bu yerda ham range kabi oxxirgisi kirmaydi bu holatda 3 kirmaydi

# yarmidan ham olsak boladi

#print(cars[2:5])
#'gm', 'tesla', 'volvo']

# Deylik qiymatni boshini qoymadik [ :3] qildik unda oz ozidan 0 ni oladi yani [0:3] deb oladi

#print(cars[:3])
#'bmw', 'mercedes benz', 'gm']

#huddi shuningdek oxxirgi elementni bermasak masalan[1:] qilsek u xolda oxxirigacha kesadi
#rint(cars[1:])
#'mercedes benz', 'gm', 'tesla', 'volvo', 'audi']

#ROYXATDAN NUSXA OLISH

# my_cars = cars deb nusxa olib olamiz

#cars
#out[95]: ['bmw', 'mercedes benz', 'gm', 'tesla', 'volvo', 'audi']

#my_cars
#out[96]: ['bmw', 'mercedes benz', 'gm', 'tesla', 'volvo', 'audi']

#agar malum birini olib tashlamoqchi bolsak .remove()dan foydalanamiz

#my_cars.remove('volvo')

#print(my_cars)
#'bmw', 'mercedes benz', 'gm', 'tesla', 'audi']
#etibor bersek volvo yoq endi royxatda

#royxat ichidagi malumotni ozgartiramiz
#my_cars[0] = 'lacetti'

#my_cars[0] = 'lacetti'

#my_cars
#out[100]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi']

#my_cars
#out[100]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi']

#print(cars)
#'lacetti', 'mercedes benz', 'gm', 'tesla', 'audi']

# etibor bergan bolsak biz faqat my_cars ustida ishlagan edik ammo carsdagi malumotlar ham ozgarib bizniki bilan bir xil bolib qoldi

#cars
#out[103]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi']

#my_cars
#out[104]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi']

#cars.append('bmw')

#cars
#out[106]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi', 'bmw']

#my_cars
#out[107]: ['lacetti', 'mercedes benz', 'gm', 'tesla', 'audi', 'bmw']

#Nega bir xil bolib qolayapti sababi yuqorida biz my_cars ham cars ham xotiradagi bitta malumot bilan ishlaydigan bolib qoldi. Unda nusxa olish qanday boladi.

#cars = ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
#cars
#out[111]: ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']

#my_cars = cars [:] # qilsak endi nusxa oladi

#cars
#out[115]: ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']

#my_cars
#out[116]: ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']

#my_cars.remove('bmw')

#cars
#out[118]: ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']

#my_cars
#out[119]: ['mercedes benz', 'volvo', 'gm', 'tesla', 'audi']

#endi my_carsdagi ozgardi carsdagi esa shunday qoldi

#yangi royxat turi bn tanishamiz bu TUPLE bu ozgarmas royxat degani

toys = ('bus', 'car', 'bear', 'dino' ,'snake' , 'lizard' )

toys
Out[131]: ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

toys[0]
Out[132]: 'bus'

toys[-1]
Out[133]: 'lizard'

toys[2:5]
Out[134]: ('bear', 'dino', 'snake')

toys[3:]
Out[135]: ('dino', 'snake', 'lizard')

toys[0] = "teddy"
Traceback (most recent call last):

Cell In[136], line 1
toys[0] = "teddy"

TypeError: 'tuple' object does not support item assignment

# yoki yangi element qoshmoqchi bolsak ham xatolik beradi sababi tupleni ozgartirib bolmaydi

toys.append("teddy")
Traceback (most recent call last):

Cell In[138], line 1
toys.append("teddy")

AttributeError: 'tuple' object has no attribute 'append'

Remove bilan ochirib ham bolmaydi

Deylik majbur bolib qoldik unda nima qilamiz bunday holatda biz tupleni listga ozgartiramiz

toys
Out[140]: ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

toys = list(toys)

type(toys)
Out[142]: list

toys.append("teddy")

toys
Out[144]: ['bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'teddy']

Ana endi oxxiriga qoshildi

Endi qanday qilib tuplega qaytaramiz

toys = tuple(toys)

type(toys)
Out[146]: tuple

[9 - dars F**or tsikli bilan tanishamiz**](https://www.notion.so/9-dars-For-tsikli-bilan-tanishamiz-77cd3eff558a4c31ad196ca6d8230c4b?pvs=21)