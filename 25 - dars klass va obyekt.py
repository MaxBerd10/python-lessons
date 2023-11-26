# 25 - dars
# Klass va Obyekt
# Bu alohida va juda katta mavzu lekin data scienceda biz tayyor data bilan ishlaymiz

# OOP object oriented Programming

# Obyekt nima?
# Pythonda shu paytgacha ozgaruvchilar funksiyalar yaratdik ularning hammasi object deb ataladi
# Object deyilishiga sabab hayotta bor narsalarni pythonda programmada korsatib berganimiz un ham object deymiz

# Obyekt odatda 2 xil boladi
#   1 Hususiyatlari  (parametrlar)

#   2 Metodlari # (funksiyalar)


#------------------------------------------------------------------------------

# Masalan Avtomobile                    
# model
#rang               >>>>>>>>>>            Hususuiyatlari
#narh

#start()
#stop()             >>>>>>>>>>>           metodlar
#tezlash()

#------------------------------------------------------------------------------


#matn = "Assalomu alaykum"

# Bu matnni parametri bor bu uni ichida saqlanayotgon matni

#matnni metodlari bor 
# matn.lower()        'assalomu alaykum'
# matn.upper()        'ASSALOMU ALAYKUM'

# print(type(matn))
# <class 'str'>         demak matnimiz string degan classga tegishli object ekan


# Klass bu bor yog`i object yaratish uchun shablon

# Deylik sizda kompyuterlar bor onlab siz uni sotasiz va har doim ularni qayta qayta
# yozavermay shablon yaratib olsangiz qayta qayta ishlataverasiz

#class Kompyuter:
#    def __init__(self, model, ram, hdd, gpu, cpu):
#        self.model = model
#        self.ram = ram
#        self.hdd = hdd
##        self.gpu = gpu
#        self.cpu = cpu
        
# Bu klass boldi
# Biz bu klassdan yangi object yaratishimiz mumkin

#macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1" )


# consoleda macbook desak
# <__main__.Kompyuter at 0x2536ee24460>  Kompyuter klassidagi object deyapti

# Endi men uning parametrlarini kormoqchiman 
# macbook.ram
# Out[62]: '8GB'

# macbook.cpu
# Out[63]: 'M1'

# macbook.hdd
# Out[64]: '512GB'

# Hususiyatlar def __init__ deb beriladi shuningdek bu object bajaradigan turli xil funksiyalar ham bolishi mumkin
# self dedik bu objectning ozi degani yani yuqorida u macbook

#def info(self):         #odatda biz bilmaymiz nomini oldindan shuning uchun self deb qoyamiz
#        inf = f"{self.model}, RAM: {self.ram}, SSD:{self.hdd}, CPU: {self.cpu}"
#return inf
#macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1" ) 
  
#print(macbook.info())



class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"{self.model}, RAM: {self.ram}, SSD:{self.hdd}, CPU: {self.cpu}"
        return inf

macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1" )

#macbook.info()
#Out[103]: 'Apple Macbook, RAM: 8GB, SSD:512GB, CPU: M1'

#Demak objectlarni hammasini qandaydir parametrlari va funksiyalari bor























        
        