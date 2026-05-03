print("========= LEMPAR DADU =========")
import random
while True:
    tanya = input("Mau lempar dadu(y/n): ")
    if tanya == "y":
        angka1 = random.randint(1,6)
        angka2= random.randint(1,6)
        print(f"({angka1},{angka2})")
    elif tanya == "n":
        print("Baiklah")
        break
    else:
        print("Permintaan invalid")



print("========== GAME TEBAK ANGKA ==========")

import random
angka_asli = random.randint(1,100)
percobaan = 0
while True:
   try:
        tanya = int(input("Silahkan pilih 1 angka dari 1 - 100: "))
        percobaan += 1
        if tanya == angka_asli:
            print(f"Selamat Anda benar")
            print(f"Anda berhasil menebak dalam {percobaan} kali percobaan")
            break
        elif tanya < angka_asli:
            print(f"Angka terlalu kecil")
        elif tanya > angka_asli:
            print(f"Angka terlalu besar")
   except ValueError:
            print("Input tidak valid")




print("======== BATU GUNTING KERTAS ==========")

import random
bot = ["GUNTING",'BATU','KERTAS']
pilihan_bot = random.choice(bot)

main = 0
menang = 0
kalah = 0
seri = 0

while True:
    pilihan_user = input("Gunting,batu,kertas: ").upper()
    main += 1
    if pilihan_user != "GUNTING" and pilihan_user != "BATU" and pilihan_user != "KERTAS":
        print("Pilihan tidak valid")
        main -= 1
    elif pilihan_user == "GUNTING" and pilihan_bot == "BATU":
        print(f"pilihan kamu: {pilihan_user} ")
        print(f'pilihan komputer: {pilihan_bot}')
        print("kamu kalah")
        kalah += 1
    elif pilihan_user == "KERTAS" and pilihan_bot == "GUNTING":
        print(f"pilihan kamu: {pilihan_user} ")
        print(f'pilihan komputer: {pilihan_bot}')
        print("kamu kalah")
        kalah += 1
    elif pilihan_user == "BATU" and pilihan_bot == "KERTAS":
        print(f"pilihan kamu: {pilihan_user} ")
        print(f'pilihan komputer: {pilihan_bot}')
        print("kamu kalah")
        kalah += 1

    elif pilihan_user == pilihan_bot:
        print(f"pilihan kamu: {pilihan_user} ")
        print(f'pilihan komputer: {pilihan_bot}')
        print("Seri")
        seri += 1
    else:
        print(f"Pilihan kamu: {pilihan_user} ")
        print(f'pilihan komputer: {pilihan_bot}')
        print("kamu menang")
        menang += 1

    Main = input("Mau main lagi(y/n): ")
    if not Main == "y":
        print("Baiklah")
        break


print()
print("----------------------")
print(f'''Total bermain : {main} kali
Menang        : {menang} kali
Kalah         : {kalah} kali
Seri          : {seri} kali''')