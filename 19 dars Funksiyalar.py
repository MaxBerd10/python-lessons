# 19 dars FUNKSIYALAR
# Funksiya malum bir codelarning yegindisi yani bir necha qator codelarning yegindisi
# nega bizga ular kerak sababi dastur davomida bir necha qator qator codelarni bir necha bor ishlatish talab qilinishi mumkin
# Ularni qayta qayta yozavermasik uchun ularni bitta funksiyaga joylab qoyishimiz mumkin
# Masalan print, type, range ular ham funksiya
# Funksiya yaratishda biz Def kalit sozi bilan boshlaymiz

#def salom_ber():
#    """Salom beruvchi funksiya""" # Bu kelajakda boshqa odam foydalanganda unga hint qilib berishimiz uchun eslatma
#    print("Assalomu alaykum")
    
#salom_ber()   #natija Assalomu alaykum 
# Keyingi safar bizga bu kerak bolsa shunchaki salom ber desak boldi   
# Funksiyalarga nom berganda imkon qadar fel yani biror bir harakatni bajaruvchi bolsin 
# Kelajakda ozgaruvchi bilan adashtirib qoymaslik uchun
# Ozgaruvchiga ot yani ism yosh familiya
# funksiyalarga esa fel 

#------------------------------------------------------------------------------

#def salom_ber(ism):             # qovus ichidagi parametr deyiladi
#    """Foydalanuvchi ismini qabul qilib,
#       unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")    

#salom_ber('maxkam')
#salom_ber('barot')

# =============================================================================
# Assalomu alaykum, hurmatli Maxkam!
# Assalomu alaykum, hurmatli Barot!
# =============================================================================


# biz (ism) ni parametr dedik
# pastda esa foydalanuvchu kiritgan qiymatni argument deb ataymiz (maxkam) (barot)

# biz funksiya parametrini qayerdan bilamiz oddiy usullaridan biri consolega salom_ber(  qilsak tagida yozuvi kelib chiqadi
# va bu DOCSTRING deyiladi va biz buni imkon qadar tushunarli qilib yozishimiz kerak ayniqsa bu murakkab funksiya bolsa
# Yoki 

#print(salom_ber.__doc__)  # qilsak consolega ham chiqib keladi 
#       Foydalanuvchi ismini qabul qilib,
#       unga salom beruvchi funksiya


# Bazida biz  funksiyamizga bir nechta parametr ham kirgizishimiz mumkin 
#------------------------------------------------------------------------------

def toliq_ism(ism, familiya):
    """Foydalanuvchining ism va familiyasini jamlab chiqaruvchi funksiya """
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
#pastdagi kabi qilsak
toliq_ism(familiya='hakimov', ism='olim')

#endi bizga ketma ketlikni fariq yoq natija togri chiqaveradi    
    
#toliq_ism('olim', 'hakimov')

#natija
# Foydalanuvchi ismi: Olim
# Foydalanuvchi familiyasi: Hakimov

# bu yerda bir narsaga etibor berishimzi kerak biz argumentlarni kirgizishda yuqoridagi ketma ketligda kiritishimiz kerak 
# yani ism keyin familiya 
# agar teskarisiga yozib qoysak ismi hakimov bob qoladi

#==============================================================================

# Bazida orin almashritib qoyishlik xatoga ham ooib keladi masalan

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur """
    print(f"{ism.title()}, {2020-tugilgan_yil} yoshda")

#yosh_hisobla('olim', 1997)     # Natija Olim, 23 yoshda
# Bu yerda 1997 'olim' qilib qoysak xatolik beradi


#Bunday xatolikni qanday qilib oldini olishimiz mumkin

# parametr nomini yozib ketamiz va u funksiya ichidagi bilan bir xil bolishi kerak masalan

yosh_hisobla(tugilgan_yil=1997, ism='olim')

#natija Olim, 23 yoshda
# agar biz ornini alishtirib yozsak ham bir xil natija chiqaveradi endi

#------------------------------------------------------------------------------

# Funksiya yaratganimizda biz bazi bir parametrlarga standart qiymat ham berib ketishimiz mumkin

def yosh_hisobla(tugulgan_yil, joriy_yil=2020):  #2020 deb standart qiymat berib kettik. Sababi agar foydalanuvchi joriy yilni kiritmasa ham biz standard qiymatdan foydalanamiz
    """ Foydalanuvchi yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugulgan_yil} yoshdasiz")
yosh_hisobla(1995, 2020)   #bu yerda biz joriy yilni berdik
yosh_hisobla(1993)  # bu yerda esa yoq



















     