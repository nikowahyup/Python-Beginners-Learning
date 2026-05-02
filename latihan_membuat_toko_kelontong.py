barang = {"Kopi":1500,'Telur':2500,"Tepung Terigu":12500,"Gula":15000,"Minyak":10000} # Persiapan barang
total = 0 # Persiapan total harga
belanjaan = {} # persiapan untuk total harga tiap jenis barang
item = {} # Persiapan untuk total item tiap barang
# 4 KODE DI ATAS SAYA BUAT DI LUAR FUNGSI KARENA MEMERHATIKAN SCOPE/JANGKAUN KARENA KEGUNAAN 4 KODE DI ATAS

def daftar(barang): # fungsi untuk menampilkan daftar barang
    print("="*15,"DAFTAR BARANG","="*15)
    for nama,value in barang.items(): # Untuk menampilka barang-barangnya,saya menggunakan for loop
        rupiah = f"{value:,}".replace(",", ".") # Dekorasi agar terlihat mirip format rupiah
        print(f"        {nama:18}: Rp{rupiah}")


def belanja(barang, total, belanjaan, item): # fungsi untuk berbelanja
    while True: # saya menggunakan while loop agar user bisa menambah barang tanpa keluar masuk tiap kali menambah barang
        tanya = input("Barang apa yang ingin Anda beli (q untuk keluar): ").title()
        if tanya == "Q": # ketik "q" jika mau kelur
            break

        if tanya not in barang: # jika inputan user tidak ada,akan menampilkan di bawah ini
            print("Maaf, barang tidak tersedia")
            continue

        try: # saya menggunakan try jikalau user tidak sengaja mengklik huruf
            jumlah = int(input(f"Berapa {tanya} yang ingin Anda beli: "))


            if tanya not in item: # kondisi ini adalah kondisi awal jika barang yang diinput user belum ada di "keranjang" mereka
                item[tanya] = 0
                belanjaan[tanya] = 0

            # MULAI BARIS 33-36 ADALAH CARA SAYA MENAMBAH INPUTAN USER KE DALAM "KERANJANG" MEREKA
            total_sementara = jumlah * barang[tanya]
            belanjaan[tanya] += total_sementara
            item[tanya] += jumlah
            total += total_sementara

            print(f" {tanya} x{jumlah} berhasil ditambahkan ke keranjang")
            print()
        except ValueError:
            print("Silahkan masukkan angka")
    return total # Tak lupa return total agar value variabel total berubah


def kembali(barang,total,item): # ini adalah fungsi untuk mengembalikan barang
    while True: # Alasan saya menggunakan while loop sama seperti fungsi belanja
        tanya = input("Barang apa yang ingin Anda kembalikan (q untuk keluar): ").title()
        if tanya == "Q":
            break

        if total == 0:
            print("Keranjang Anda masih kosong") # barangkali user salah input
        if tanya not in item:
            print("Maaf,barang tidak ada di keranjang") # jika barang yang diinput user tidak ada di dalam "keranjang"nya,otomatis mereka akan keluar
            break
            # DI BAWAH INI ADALAH PROSES PENGEMBALIAN BARANG YANG SAYA RANCANG
        if tanya in barang:
            try: # kembali menggunakan try
                jumlah = int(input("Berapa yang ingin Anda kembalikan: "))
                if item[tanya] < jumlah:
                    print("Jumlah pengurangan yang Anda inginkan melebihi jumlah di keranjang Anda")
                    break
                elif item[tanya] >= jumlah:
                    total_sementara = jumlah * barang[tanya]
                    item[tanya] -= jumlah
                    belanjaan[tanya] -= total_sementara
                    total -= total_sementara
                    print(f"{tanya} x{jumlah} berhasil dikembalikan")
            except ValueError:
                print("Silahkan masukkan angka")
        print()
    return total # tak lupa return total agar nilainya berubah


def lihat_keranjang(total,item): # ini adalah fungsi untuk melihat total sementara dan jumlah item user

    print("="*15,"KERANJANG ANDA","="*15)
    format_total = f"{total:,}".replace(",", ".") # kembali menghias agar seperti format rupiah asli
    if belanjaan == {}:
        print("Keranjang masih kosong")
    for nama,value in item.items(): # saya menggunakan for loop untuk menampilkan barang yang sudah ada di keranjang
        print(f"    {nama:18}: x{value:,}")
    print("-"*46)
    print(f"   total Rp{format_total}      total item = {sum(item.values())} item")
    print()


def bayar(total,item,belanjaan): # Ini adalah fungsi bayar. Tak banyak yang bisa dibahas
    print("-"*10,"STRUK BELANJA","-"*10)
    print("        Toko Kelontong Makmur")

    print()
    for nama,value in item.items():
        format = f"{belanjaan[nama]:,}".replace(",",".") # format rupiah asli

        print(f'''-x{value} {nama:15} Rp{format:4}
-----------------------------------''')

    print("="*35)
    format_total = f"{total:,}".replace(",", ".") # ini juga format rupiah asli
    print(f"     total akhir : Rp{format_total}")
    print("=" * 35)
    print("   TERIMA KASIH TELAH BERBELANJA")



#  MULAI BARIS 108-138 ADALAH KODE YANG MENJALANKAN TOKO KELONTONG SAYA
while True:
    print("================= TOKO KELONTONG MAKMUR ================= ")
    print()
    print("1. Lihat daftar barang")
    print("2. Tambah barang")
    print("3. Kembalikan barang")
    print("4. Lihat keranjang")
    print("5. Bayar")
    print("6. Keluar")
    print()
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        daftar(barang)
        print()
    elif pilihan == "2":
        total = belanja(barang,total,belanjaan,item)
        print()
    elif pilihan == "3":
        total = kembali(barang,total,item)
        print()
    elif pilihan == "4":
        print()
        lihat_keranjang(total,item)
    elif pilihan == "5":
        bayar(total,item,belanjaan)
        break
    elif pilihan == "6":
        print("Sampai jumpa")
        break
    else:
        print("Pilihan tidak valid")



#   SEKIAN TOKO KELONTONG BUATAN SAYA. MASIH BANYAK YANG PERLU DIPERBAIKI,SAYA YAKIN.
