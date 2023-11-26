#import avto_info_mod

#avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#avto_info_mod.info_print(avto1)
# Agar module nomini yozmasak xato beradi
#Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# va togridan togri module nomi bilan muroja qila olishimiz uchun har ikkala faylimiz bitta papkada bolishi kerak

#------------------------------------------------------------------------------

#Deylik module nomi juda ham uzunlik qilayapti 
# Uni nomlasa ham boladi qisqa nom qilib ozimizga qulay qilib

#import avto_info_mod as aim   # as deb nom berdik
#aim.info_print(avto1)

#Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$

#------------------------------------------------------------------------------

#from avto_info_mod import avto_info, info_print

#avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#info_print(avto1)

# Deylik modul ichidan biror funksiyani chqirib olmoqchimiz va ularni nomi bir xil
# Bunday holatda funksiyani nomini ham ozgartirsak boladi

#from avto_info_mod import avto_info as ainfo, info_print as iprint
#avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#iprint(avto1)

#Bunday qilishimizga sabab yo funksiyani nomi uzun yoki nomi bir xil nomlik narsa bor 

#------------------------------------------------------------------------------

#from avto_info_mod import * # hamma funksiyani chaqirib olyapmiz
# endi yuqoridagi kabi nomma nom funksiyalarga murojat qilishimiz mumkin

#avto1 = avto_info("GM", "malibu", "Qora", "avtomat", 2020,40000)
#info_print(avto1)

#natija
#Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$

#Lekin bu usuldan foydalanish maslahat berilmaydi sababi har bir modul ichida kop funksiyalar bor 
# hammasini ulab tashlasak qorishib ketadi va nomi bir xil funksiya bolib qolsa dasturimiz xato ishlashni boshlaydi


