# List : Tempat untuk menyimpan banyak data dalam satu variabel
# List menggunakan tanda kurung siku []

lst = [] # list adalah list kosong
buah = ["Mangga","Pepaya","Anggur"] # Ini adalah list yang menyimpan 3 nama buah
negara = ["Indonesia","Malaysia","Thailand","Filipina","Singapura"] # List yang menyimpan 3 nama negara

# Dalam list,kita bisa menyimpan tipe data apapun. Data dalam list juga bisa diduplikasi
bebas = [1,"Niko",True,6.78,"Indonesia"] # 4 jenis data dapat tersimpan dalam 1 list

# APA YANG DAPAT KITA LAKUKAN DENGAN LIST

#1. Mengetahui banyak item dalam list

# print(len(buah)) # bisa menggunakan len() untuk mengetahui banyak item dalam suatu list

# #2. Akses item di dalam list
# print(negara[0]) # Untuk mengakses item dalam list,bisa menggunakan indexing seperti mengakses karakter string
# print(negara[2:])
#
#
# print(help(list))

#3. MEMODIFIKASI ITEM DALAM LIST
print(buah)
buah[0] = "Apel"
print(buah[0]) # Kita bisa mengubah item list dengan memilih index mana yang akan diubah
buah[0:3] = "Semangka","Nanas","Rambutan"
print(buah)


# MENAMBAH ITEM DI DALAM LIST. append() atau insert()
buah.append("Markisa")
print(buah)
buah.insert(0,"Srikaya") # insert() bisa menempatkan item berdasarkan yang kita mau
print(buah)


# # MENGHAPUS ITEM. remove() atau pop()
# buah.remove("Semangka")
# print(buah)
# buah.pop(2)
# print(buah)

# MENGGABUNG LIST DENGAN LIST. extend()
buah.extend(negara) # Menggunakan method extend()
print(buah)

#MENGURUTKAN DATA. sort()
nilai = [78,98,99,81,72,90,85]# akan mengurutkan dari terkecil ke terbesar
nilai.sort()
print(nilai)
nilai.reverse()# diurutkan juga,tapi dari terbesar ke terkecil
print(nilai)

nama = ["Budi","Calvin","Angga","Niko"]
nama.sort() #Jika huruf,akan diurutkan berdasarkan urutan huruf alphabet
print(nama)
