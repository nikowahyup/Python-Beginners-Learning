#   Kali ini saya membuat sistem perpustakaan sederhana menggunakan konsep class,function,while loop dan if-else.

# Ini adalah class pertama saya:Buku
class Buku:
    # Saya menambahkan 4 atribut untuk tiap objek buku saya
    def __init__(self,judul,penulis,halaman,stok):
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman
        self.stok = stok

    # ini adalah fungsi yang nanti akan membantu siswa menemukan buku pilihan mereka
    def info_buku(self):
        status = "Tersedia" if self.stok > 0 else "Habis terpinjam"
        print(f"Judul Buku      : {self.judul}")
        print(f"Penulis Buku    : {self.penulis}")
        print(f"Jumlah halaman  : {self.halaman}")
        print(f"Stok            : {self.stok}({status})")


# Ini adalah class kedua saya:Siswa
class Siswa:
    def __init__(self,nama,kelas): # Saya menambah 2 atribut untuk tiap objek siswa
        self.nama = nama
        self.kelas = kelas
        self.pinjam = [] # saya juga menambah default atribut untuk tiap objek yang berisi daftar buku yang sudah dipinjam
        self.limit = 3 # Ini adalah default atribut seberapa banyak tiap siswa boleh meminjam buku

    # Ini fungsi untuk memudahkan siswa nanti mengetahui kondisi pinjaman mereka
    def info_siswa(self):
        print(f"Nama            : {self.nama}")
        print(f"Kelas           : {self.kelas}")
        print(f"Daftar pinjaman : {",".join(self.pinjam)}")
        print(f'Limit pinjaman  : {self.limit}/3')


# Ini adalah class ketiga dan class utama saya kali:Perpustakaan
class Perpustakaan:
    # Saya hanya menambahkan 2 default atribut: Daftar siswa dan daftar buku yang tersimpan dalam bentuk list
    def __init__(self):
        self.daftar_buku = []
        self.daftar_siswa = []


    # fungsi untuk menambah buku ke dalam "rak" perpustakaan
    def tambah_buku(self,buku):
        self.daftar_buku.append(buku)
        return


    # fungsi untuk menambah nama siswa ke daftar anggota perpustakaan(hanya anggota yang boleh meminjam buku)
    def tambah_siswa(self,siswa):
        self.daftar_siswa.append(siswa)
        return


    # fungsi untuk salah satu fitur perpustakaan nanti:Menampilkan seluruh daftar buku di perpustakaan
    def lihat_semua_buku(self):

        # jika tidak ada satupun buku yang dimasukkan ke perpustakaan
        if not self.daftar_buku:
            print("⚠️Perpustakaan masih kosong")
            return

        # jika sudah ada buku,kode ini akan berjalan
        for i,buku in enumerate(self.daftar_buku,start=1):
            print(f"{i}. {buku.judul}")
            print(f"Penulis : {buku.penulis}")
            print(f"Halaman : {buku.halaman}")
            print(f"Stok    : {buku.stok}")
            print()



    # fungsi ini salah satu fitur perpustakaan nanti:Mencari tahu kondisi pinjaman tiap siswa
    def cari_siswa(self,nama):
        for siswa in self.daftar_siswa:
            if siswa.nama == nama:
                siswa.info_siswa()
                return
        print("⚠️Nama siswa tidak ditemukan")




    # salah satu fitur perpustakaan juga:Mencari judul buku keinginan siswa
    def cari_buku(self,judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                print(f"✅Buku {buku.judul} ditemukan")
                buku.info_buku()
                return

        print(f"❌Buku {judul} tidak tersedia")



    # ini adalah fungsi untuk memvalidasi adanya objek buku atau tidak(nanti akan diperlihatkan di bagian while loop)
    def cari_siswa_obj(self,nama):
        for siswa in self.daftar_siswa:
            if siswa.nama == nama:
                return siswa
        return None



    # ini juga sama,akan diperlihatkan di while loop
    def cari_buku_obj(self,judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                return buku
        return None



    # ini adalah salah satu fitur perpustakaan:Pinjam-meminjam buku
    def pinjam_buku(self,buku,siswa):

        # ini akan dijelaskan di dalam while loop
        if buku is None:
            print("❌Buku tidak tersedia")
            return

        # ini juga akan dijelaskan di dalam while loop
        if siswa is None:
            print("❌Siswa tidak terdaftar")
            return

        # kondisi jika siswa sudah meminjam buku yang sama(tidak boleh meminjam buku yang sama)
        if buku.judul in siswa.pinjam:
            print(f"⚠️Kamu sudah meminjam buku ini")
            return

        # kondisi jika stok buku sudah habis
        if buku.stok == 0:
            print("❌Maaf,stok buku ini sudah habis")
            return

        # kondisi jika limit peminjaman siswa mencapai batas
        if siswa.limit == 0:
            print("⚠️Limit peminjamanmu telah tercapai")
            return

        # proses peminjaman
        siswa.pinjam.append(buku.judul) # buku ditambahkan ke dalam daftar pinjam siswa
        buku.stok -= 1 # stok buku berkurang karena dipinjam
        siswa.limit -= 1 # limit siswa berkurang karena meminjam

        print(f"✅Selamat membaca buku {buku.judul},{siswa.nama}!")


    # salah satu fitur perpustakaan:Siswa dapat mengembalikan buku pinjaman mereka
    def kembalikan_buku(self,buku,siswa):

        # penjelasannya sama seperti fungsi pinjam_buku
        if buku is None:
            print("❌Buku tidak tersedia")
            return


        # ini juga sama
        if siswa is None:
            print("❌Siswa tidak terdaftar")
            return

        # kondisi jika siswa tidak meminjam buku
        if buku.judul not in siswa.pinjam:
            print("⚠️Kamu tidak meminjam buku ini")
            return

        # proses pengembalian
        siswa.pinjam.remove(buku.judul) # judul buku dihapus dari daftar pinjam siswa
        siswa.limit += 1 # limit siswa ditambahkan karena sudah mengembalikan buku
        buku.stok += 1 # stok buku bertambah 1 karena sudah dikembalikan

        print(f"✅Terima kasih telah membaca buku {buku.judul},{siswa.nama}!")


# INI MULAI MEMBUAT OBJEK-OBJEK. BARIS 182-194

# Objek siswa(5 objek)
siswa = Siswa("Niko Wahyu Pratama","XII-IPA2")
siswa1 = Siswa("Christiano Ronaldo","XII-IPA2")
siswa2 = Siswa("Masashi Kishimoto",'XII-IPS1')
siswa3 = Siswa('Justin Bieber','XII-IPS2')
siswa4 = Siswa('Donald Trump',"XII-BAHASA2")
# Objek buku(5 objek)
buku = Buku("Hujan","Tere",340,5)
buku1 = Buku("Harryy Potter:Batu Bertuah","J.K.Rowling",384,4)
buku2 = Buku('Atomic Habits','James Clear',380,3)
buku3 = Buku('The Alchemist','Paulo Coelho',224,2)
buku4 = Buku("The Things You Can See Only When You Slow Down","Heamin Sunim",288,4)
# Objek perpustakaan(1 objek)
perpus = Perpustakaan()

# proses memasukkan 2 objek(siswa dan buku) ke dalam perpustakaan. Baris 198-208
perpus.tambah_siswa(siswa)
perpus.tambah_siswa(siswa1)
perpus.tambah_siswa(siswa2)
perpus.tambah_siswa(siswa3)
perpus.tambah_siswa(siswa4)

perpus.tambah_buku(buku)
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)
perpus.tambah_buku(buku4)



# INI ADALAH SISTEM PERPUSTAKAAN
while True:
    # informasi tentang fitur-fitur perpustakaan
    print("="*30)
    print("SELAMAT DATANG DI PERPUSTAKAAN")
    print()
    print("1. Lihat daftar buku")
    print("2. Cari buku")
    print("3. Pinjam buku")
    print("4. Kembalikan buku")
    print("5. Lihat daftar pinjaman kamu")
    print("6. Keluar")
    print()

    # siswa dapat memilih apa yang ingin dilakukan
    pilihan = input("Pilihan kamu: ")
    if pilihan == "1":
        perpus.lihat_semua_buku() # Jika siswa memilih 1,cukup panggil fungsi lihat buku yang sudah kita buat tadi
        print()

    elif pilihan == "2":
        judul = input("Masukkan judul buku yang kamu cari: ").title()
        perpus.cari_buku(judul) # Jika siswa memilih 2,cukup panggil fungsi mencari buku
        print()

    # ini adalah fitur yang cukup sederhana dari kodenya,tapi secara sistem lumayan kompleks
    elif pilihan == "3":
        nama = input("Masukkan nama lengkap kamu: ").title() # pertama kita tanyakan nama lengkap(jika siswa tidak terdaftar,tidak boleh meminjam buku)
        judul = input("Masukkan judul yang ingin kamu pinjam: ").title() # kedua kita tanyakan judul buku(jika buku tidak terdaftar,tidak bisa meminjam buku)
        buku_obj =perpus.cari_buku_obj(judul) # ini adalah konversi dari inputan yang berupa data string menjadi objek dari input judul
        siswa_obj = perpus.cari_siswa_obj(nama) # ini adalah konversi dari inputan yang berupa data string menjadi objek dari input nama
        print()
        perpus.pinjam_buku(buku_obj,siswa_obj) # hasil 2 konversi tadi baru kita masukkan ke fungsi pinjam
        print()

    elif pilihan == "4":
        nama = input("Masukkan nama lengkap kamu: ").title() # siswa perlu memasukkan nama lengkap
        judul = input("Masukkan judul yang ingin kamu kembalikan: ").title() # siswa perlu memasukkan judul buku yang dipinjam
        buku_obj =perpus.cari_buku_obj(judul) # sama,konversi data
        siswa_obj = perpus.cari_siswa_obj(nama) # konversi data
        print()
        perpus.kembalikan_buku(buku_obj,siswa_obj) # hasil konversi baru dimasukkan ke fungsi kembalikan buku
        print()

    elif pilihan == "5":
        nama = input("Masukkan nama lengkap kamu: ").title() # siswa perlu memasukkan nama lengkap
        perpus.cari_siswa(nama) # kemudian dimasukkan ke dalam fungsi
        print()

    elif pilihan == "6":
        print("TERIMA KASIH TELAH BERKUNJUNG")
        break


# KENAPA KITA PERLU MENGONVERSI DATA???
# fungsi input() pada dasarnya memberi kita data string,jadi saat kita memasukkan nama lengkap ataupun judul buku,kita mendapat data string
# masalahnya,apa yang kita simpan di dalam class Perpustakaan itu bukanlah string,melainkan objek. Objek yang memiliki atribut string
# nama siswa,judul buku,nama penulis,kelas siswa,itu semua adalah data string yang melekat pada objek
# khususnya jika kita melakukan pinjaman hanya dengan memasukkan salah satu atribut saja,misal judul buku,atribut lain tidak akan terpengaruh
# ini berpengaruh nantinya pada sistem peminjaman dan pengembalian

# tujuan konversi dulu adalah kita akan mencari dulu apakah ada objek yang memiliki atribut seperti yang dimasukkan user
# misal,saya ingin meminjam buku berjudul Hujan,sistem akan mencari dulu apakah ada objek yang memiliki atribut Hujan(dalam hal ini tentu judul buku)
# jika ada,fungsi akan mengolah objek tersebut,jika meminjam maka fungsi akan mengurangi stok buku,jika mengembalikan buku,fungsi akan menambah kembali stok buku
# atribut stok dan atribut judul berbeda tipe data bukan? satunya integer satunya lagi string

# KENAPA DALAM FUNGSI CARI_SISWA ATAU CARI_BUKU TIDAK PERLU KONVERSI???

# karena kita tidak mengolah objek. Kita hanya ingin tau seperti apa kondisi objek. Kita tidak mengurangi stok buku dalam melihat kondisi objek buku bukan?
# oleh karena itu,kita tidak perlu konversi,fungsi kita mendapat input judul buku atau nama siswa lalu menampilkan kondisinya saja


# SEKIAN PROYEK KECIL DARI SAYA. SAYA BERHARAP BISA MENINGKATKAN SKILL SAYA MENJADI LEBIH BAIK LAGI
# MAAF JIKA PENJELASAN SAYA AGAK BELIBET. MOHON KOREKSINYA JIKA SAYA ADA SALAH KONSEP. TERIMA KASIH...


