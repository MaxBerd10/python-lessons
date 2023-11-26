ism = "Max"

shahar = "фаргона" # O`zgaruvchini o`zi istagan tilda bo`lishi mumkin ammo o`zgaruvchini o`zi lotin tilida bo`lishi kerak.

# Unicodeni ichidagi hammasi ishlatiladi

smayl = "🤗"

print(smayl)

#string ustida amallar

# Biz plus yordamida matnlarni bir biriga qo`shishimiz mumkin.

ism = "Ahmad"
print("Mening ismim " + ism)

ism = "Leo"
familiya = "Messi"
print(ism + familiya)

# Bo`shliq bo`lmaydi orasida masalan; LeoMessi shunday bo`lib chiqadi.

print(ism + ' ' + familiya) # Leo Messi bo`ladi.

# f-string bilan ham jamlasak bo`ladi

ism = "Leo"
familiya = "Messi"

ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

# Javobi Leo Messi bo`lib chiqadi.

ism = "James"
familiya = "Bond"
print(f"Salom mening ismim {familiya}. {ism} {familiya}")

# Salom mening ismim Bond. James Bond deb chiqadi consoleda.

# Mahsus belgilar

print("Hello World")
print("Hello \tWorld") # orasida uzun boshliq qoldiradi
print("Hello \nWorld") #boshqa qatorga kochiradi.

# Javobi

#Hello World
#Hello 	World
#Hello
#World

# String methodlar

#Biz string (Matn) lar ustida turli xil amallarni bajarishimiz mumkin. 

#Bular Metodlar deb aytiladi. 

#Biz Metodlarga  MATN.METOD.() ko’rinishida murojat qilamiz. 

#Masalan: 

ism = “james”

familiya = “bond”

ism_sharif = f”{ism} {familiya}”

String ning o`ziga hos metodlari mavjud. 

### .upper()

print(ism_sharif.upper())                                                      out: JAMES BOND

**Biz bu metodni qo`llaganimizda variable (o`zgaruvchi) ning ichidagi malumot o`zgarmaydi. Faqatgina outcome o`zgaradi.** 

**.upper() ni ishlatsak string dagi hamma harf katta xarf bilan yoziladi.** 

---

Agar variableda ham o`zgartirmoqchi bo`lsak 

ism_sharif = ism_sharif.upper()                                variableda ham katta harfda bo`ladi JAMES BOND

---

### .lower()

print(ism_sharif.lower()) 

stringdagi hamma harflarni kichik harf bilan chiqaradi. 

---

### .title()

**Matnni birinchi harflarini katta qilib beradi.**

print(ism_sharif.title())                                                                out: James Bond

---

### .capitalize()

**Matnni faqatgina birinchi harfini katta qilib beradi.** 

print(ism_sharif.capitalize())                                                  out: James bond

---

### .lstrip() va .rstrip()

**Chap tarafdagi boshliqni olib tashlaydi.**

meva = “                    olma                        “                    variableda ham :  _________olma______chiqadi.

print(”Men + meva.lstrip() + “yaxshi ko`raman”)             out: Men olma ________ yaxshi ko`raman

print(”Men + meva.rstrip() + “yaxshi ko`raman”)           out: Men_________ olma yaxshi ko`raman

---

### .strip()

**Ikkala tarafdagi bo`shliqni olib tashlaydi.**

print(”Men + meva.strip() + “yaxshi ko`raman”)                      **** out: Men olma yaxshi ko`raman

---

### input

**Bu funksiyaning maqsadi foydalanuvchidan ham malumot olish masalan.**

Foydalanuvchidan so`raymiz.

ism = input(”Ismingiz nima?”) 

print(”Assalomu alaykum,” + ism)  

Buni bajarsak consoleda 

**Ismingiz nima ?** deydi 

Mahkam desak. Pastdan 

**Assalomu alaykum Mahkam** deb javob beradi.

**ism = input(”Ismingiz nima?”\n >>>”)**                                       **\n** yangi qatordan yozish.

**consoleda :**

Ismingiz nima ? 

>>>> max 

shu ko`rinishda pastdan chiqadi. 

---

Katta harfda qilmoqchi bo`lsak 

print(”Assalomu alaykum,” + ism.title())  qilamiz 

out:  **Assalomu alaykum Max** deb chiqadi.

 

