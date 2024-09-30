print("----------------------------------------------------------")
print("Nama    : Zyrus Alfredo Randan Malinggato   ")
print("NIM     : 2409116120")
print("Kelas   : Sistem Informasi C 2024")
print("Program : Mini Project 1 (NIM Genap) - Pratikum Daspro -")
print("----------------------------------------------------------")

# Menerapkan Login Sederhana (Input Nama & NIM)
while True:

    Nama = "Zyrus"
    Nim = "120"

    print("Selamat Datang Di Program Mini Project (1) Daspro, Silahkan masukkan Username & Password yang sesuai")
    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")
    if Username == Nama and Password == Nim:
        print ("Halo, Selamat Datang",Nama)
    else:
        print("Username dan Password tidak sesuai, silahkan coba lagi")
        continue
    
#Input Untuk Harga Barang Dan Jumlah Barang
    while True:
        HargaBarang = float(input("Masukkan Harga Barang(Contoh: 150.000): Rp. "))
        JumlahBarang = int(input("Masukkan Jumlah Barang: "))
        TotalHarga = HargaBarang * JumlahBarang

    # Mengecek Apakah Total Harga Lebih dari Rp250.0000 Untuk Diskon Sebesar 25%
        if TotalHarga > 250.0000:
            Diskon = TotalHarga * 0.25
            HargaSetelahDiskon = TotalHarga - Diskon
            print("Selamat, anda mendapatkan diskon sebesar 25%")
            print("TotalHarga: Rp.", HargaSetelahDiskon)
        else:
            print("Total Harga: Rp.", TotalHarga)

    # Memberikan pilihan apakkah ingin menghitung total harga kembali atau keluar dari program
        Pilihan = input("Apakah Anda Ingin Menghitung Total Kembali? (Ya/Tidak): ")
        if Pilihan == "Ya":
            continue
        else:
            print("Terimakasih, Have A Nice Day!")
            
            exit()