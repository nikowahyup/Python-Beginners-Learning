# Kita akan membuat sistem sederhana tentang toko pizza
# Kita akan menggunakan materi input(),typecasting,variabel,Aritmatika,dan if-else

print("="*15,"TOKO PIZZA","="*15)
print()
print('''       SILAHKAN PILIH MENU ANDA
        Reguler          $4.50
        Large            $7.65
        Mini             $3.45
        Extra cheese     $5.20
        Extra topping    $5.20
        Soda             $1.50
        
        ''')

pilihan = input("Mau pesan apa: ").capitalize()
berapa = int(input("Mau pesan berapa: "))

if pilihan == "Reguler":
    total = berapa * 4.50
    print(f"Total ${total:.2f}")
elif pilihan == "Large":
    total = berapa * 7.65
    print(f"Total ${total:.2f}")
elif pilihan == "Mini":
    total = berapa * 3.45
    print(f"Total ${total:.2f}")
elif pilihan == "Extra cheese":
    total = berapa * 5.20
    print(f"Total ${total:.2f}")
elif pilihan == "Extra topping":
    total = berapa * 5.20
    print(f"Total ${total:.2f}")
elif pilihan == "Soda":
    total = berapa * 1.50
    print(f"Total ${total:.2f}")
else:
    print("Maaf,menu tidak tersedia")

print("TERIMA KASIH TELAH ORDER")




