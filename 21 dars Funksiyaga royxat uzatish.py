# 21 dars Funksiyaga royxat uzatish 

def bahola(ismlar):
    baholar = {}
    while ismlar:  #ismlar ichidagi har bir element uchun takrorlanadi va har gal ismlar ichidan bitta elementni olib baholab lugatga joylashtiramiz   
        ism = ismlar.pop()   #pop() yoramida bitta elementni sugurib olib uzatayapmiz
        baho =input(f"Talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism]=int(baho)   #ism baho korinishidagi lugat
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)

# pop() metodi odatda royxatning oxxiridan boshlaydi 
# =============================================================================
# Talaba Husan ning bahosini kiriting: 4
# Talaba Hasan ning bahosini kiriting: 5
# Talaba Vali ning bahosini kiriting: 4
# Talaba Ali ning bahosini kiriting: 3
# {'husan': 4, 'hasan': 5, 'vali': 4, 'ali': 3}
# =============================================================================

# Bu yerda etibor beradigan narsa agar biz print(talabalar) desak consoleda royxatimiz bosh chiqadi []
# Lekin biz talabalar = ['ali', 'vali', 'hasan', 'husan'] yaratgan edik
# Gap shundaki biz funksiyaga royxat uzatkan payt uning nusxasini emas aslini uzatib yuboradi

# Agar bir xil narsani ikkita ozgaruvchiga berib qoysak ikkalasi boglanib qoladi 

# talabalar ----------
#                     >>>>>>>>>>>>>>['ali', 'vali', 'hasan', 'husan']
# ismlar -------------
# bolib qoldi shuning ucun endi biz funksiyani ichiga qandaydir ozgartirsh kiritsak funkiya tashqarisiga ham bu narsa tasir qiladi 

# Bu juda muhim 

#--------------------------------------------------------------------------

# Unday bolsa biz qanday qilib asl royxatimizni saqlab qolishimiz mumkin

# ROYXATDAN NUSXA OLISH funksiyasidan foyxalanamiz [:]
baholar = bahola(talabalar[:]) #endi bu bu royxatni ozini emas nusxasini funksiyaga uzatayapti
print(baholar)
print(talabalar)

# =============================================================================
# Talaba Husan ning bahosini kiriting: 5
# Talaba Hasan ning bahosini kiriting: 4
# Talaba Vali ning bahosini kiriting: 4
# Talaba Ali ning bahosini kiriting: 5
# {'husan': 5, 'hasan': 4, 'vali': 4, 'ali': 5}
# ['ali', 'vali', 'hasan', 'husan']  Mana endi asl royxatimiz ham turibdi
# =============================================================================

# Funksiyalar bilan ishlashda ehtiyot bolishimiz kerak va asl royxatimiz ozgarib ketmasligini oldini olishimiz kerak


# talabalar2 = talabalar deb qoysak consoleda ikkalasi bitta bob qoladi
# natija bir xil chiqaveradi ikki xil nom yozsak ham u bilan biror ish qilsak ham masalan pop()

# oddiy ozgaruvchilarda masalan integer float ularda bunday muammo yoq bu narsa royxatlarga tegishli




















