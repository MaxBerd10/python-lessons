import random as r  # r ga ozgartirdikmi endi bu r dan boshqa joyda foydalanmang

# randint() berilgan sonla ichidagi biror sonni random qilib qaytaradi
#son = r.randint(0,100)
#print(son)
# bu yerda odatda har doim burun son qaytadi

#------------------------------------------------------------------------------

# =============================================================================
# # Yana bir funksiya bu CHOICE() funksiyasi 
# # Sizdagi royxatni ichidan biror bir tasodifiy qiymatni tanlab oladi
# 
# ismlar = ['olim', 'anvar', 'hasan', 'husan']
# ism = r.choice(ismlar) #bu yerda bittadan kop qiymat berishimiz kerak
# print(ism)
# # shular ichidan birortasini tanlab beradi tasodifan
# print(r.choice(ism))  #bizda olim chiqdi endi olimning ichidan ham bitta tasodifiy qiymat tanlagin deyapmiz
# 
# =============================================================================




#sonlar bilan qilamiz
# =============================================================================
# x = list(range(0,51,5)) # 0 dan 51gacha bolgan sonlarni 5 qadam bilan royxatini tuzamiz
# # undan keyin royxat ichidan tasodifiy bitta qiymatni tanlaymiz
# print(x)
# print(r.choice(x))
# 
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# 30
# 
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# 45
# =============================================================================



# shuffle (aralashtirib tashlash) biz bergan qiymatimizni ornini almashtirib tashlaydi
x = list(range(11))
print(x)
r.shuffle(x)
print(x)

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[2, 8, 1, 6, 0, 4, 3, 7, 5, 9, 10]