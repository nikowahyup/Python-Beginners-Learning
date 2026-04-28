# Dalam kondisi ini,kita akan sering bahkan selalu menggunakan statement if-else.
# Seperti artinya,if-else(jika-jika tidak),kita akan mengatur suatu kode dijalankan atau tidak sesuai dengan kondisi
# Jika kondisi bernilai benar/True/1,maka kode akan berjalan. Jika tidak,kode tidak akan berjalan
# Dalam if statement,kode harus diberi indentasi(spasi) setelah statement if-else.
# Ini akan mengartikan bahwa kode yang berjalan sebenarnya masih di dalam sebuah kondisi if-else
# Jangan lupa untuk memberikan tanda titik 2 setelah pernyataan kondisi

# Kita akan membuat contoh menggunakan if-else digabunng dengan operasi logika matematika

# Contoh sederhana

nama = "John" # Saya membuat variabel nama yang berisi nama saya

if nama == "Niko Wahyu Pratama": # Inilah kondisinya. Ini dibaca,"Jika 'nama' isinya ' Niko Wahyu Pratama'"
    print(f"Halo niko") # Jika kondisinya sesuai,maka akan muncul kalimat "Halo Niko" di konsol

else: # Ini adalah kondisi jika nilai variabel nama bukan "Niko Wahyu Pratama". Bebas mau apapun
    print("Kamu siapa ya?")# Jika nama bukan "Niko Wahyu Pratama",akan muncul pesan ini di konsol


# Mengecek apakah suatu bilangan positif atau negatif

a = 0

if a > 0:
    print(f"{a} adalah bilangan postif")
else:
    print(f"{a} adalah bilangan negatif")




# ELIF, ini gabungan dari else-if.
# Maksudnya adalah jika kondisi tidak termasuk di dalam kondisi utama(if) dan else(kebaliakan if),kita bisa menambah kondisi lagi
# Singkatnya kita bisa menambah sebanyak-banyaknya kondisi menggunakan elif

nilai = 92

if nilai < 75:
    print("Maaf,kamu tidak lulus")
elif nilai == 75:
    print("Grade C-")
elif nilai > 75 and nilai <= 80:
    print("Grade C+")
elif nilai > 80 and nilai <= 85:
    print("Grade B-")
elif nilai > 85 and nilai <= 89:
    print("Grade B+")
elif nilai > 89 and nilai <= 91:
    print("Grade A-")
elif nilai > 91:
    print("Grade A+")
else:
    print("Kamu belum ujian")