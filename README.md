# Mini-Project-1-Daspro
Nama: Zyrus Alfredo Randan Malinggato NIM: 2409116120 Sistem Informasi C '2024  - Tugas Pratikum, Mini Project (1) Daspro -

1). Membuat sebuah program menggunakan bahasa pemrograman Python, dimana program tersebut dapat menghitung total harga barang berdasarkan harga barang dan jumlah pembelian.
    Jika, jumlah harga lebih dari Rp250.000 maka mendapatkaan diskon sebesar 25%, jika tidak total harga akan tetap sama.

![Screenshoot (Kode Mini Project (1)) - Pratikum Daspro](https://github.com/user-attachments/assets/37a7f0de-4c2d-430e-820b-0ec1a4249105)

Penjelasan:
Pertama-tama membuat kode "Login Sederhana" dengan menginput Nama & Nim. Di sini saya memakai while True agar terjadi loop sampai dengan kondisi yang sesuai.
Lalu saya membuat variable Nama = "Zyrus" dan Nim = "120". Variable Nama & Nim saya definisikan untuk menginput Nama sebagai Username, dan Nim sebagai Password. maka yang terjadi

if Username == Nama and Password == Nim:
        print ("Halo, Selamat Datang",Nama)
    else:
        print("Username dan Password tidak sesuai, silahkan coba lagi")
        continue

Mengapa pada bagian else saya menambahkan perintah "Continue" agar program tetap meminta pengguna untuk menginput ulang Username dan Password jika tidak sesuai. Tanpa perintah "Continue" program akan terus
berlanjut meskipun Username & Password yang kita masukkan tidak sesuai.

Kedua, masuk pada pembuatan kode "Input Harga Barang dan Jumlah Barang". Sama seperti sebelumnya, saya masih memakai while True agar terjadi loop sampai dengan kondisi yang sesuai. 
Membuat beberapa variable seperti HargaBarang, JumlahBarang, TotalHarga, Diskon, HargaSetelahDiskon, dan Pilihan. Pada HargaBarang saya menggunakan float saat menginput, mengapa? Karena penulisan bentuk harga berupa desimal seperti contoh (Rp250.000) maka dari itu saya menggunakan tipe data float. lalu untuk JumlahBarang saya menggunakan tipe data int saat menginput, mengapa? Karena penulisan jumlah barang cukup dengan bilangan bulat. Selanjutnya, untuk menghitung TotalHarga saya membuat seperti ini: 
TotalHarga = HargaBarang * JumlahBarang - Yang dimana HargaBarang dan JumlahBarang akan di kalikan dengan simbol (*).

Ketiga, "Mengecek Apakah Total Harga Lebih dari Rp250.0000 Untuk Diskon Sebesar 25%" . Disini saya menggunakan percabangan, if dan else. Untuk mengecek apakah akan mendapatkan diskon sebesar 25% dengan syarat TotalHarga harus lebih dari Rp250.000 . Maka saya membuat

if TotalHarga > 250.0000:
jadi, jika TotalHarga lebih besar dari 250.000 akan mendapatkan diskon sebesar 25% dengan cara:
Diskon = TotalHarga * 0.25
         HargaSetelahDiskon = TotalHarga - Diskon
         print("Selamat, anda mendapatkan diskon sebesar 25%")
         print("TotalHarga: Rp.", HargaSetelahDiskon)
    else:
        print("Total Harga: Rp.", TotalHarga)

variable Diskon = TotalHarga dikali 0.25 - Mengapa 0.25 itu karena 25% sama dengan 0.25 lalu untuk menghasilkan ouput dari TotalHarga setelah diskon adalah dengan cara TotalHarga - Diskon. Lalu akan d print yang menyatakan bahwa mendapatkan diskon sebesar 25%. 
Jika tidak mendapatkan diskon (TotalHarga kurang dari 250.000) akan beralih ke else dan akan di print Total Harga.

Terakhir, "Memberikan pilihan apakkah ingin menghitung total harga kembali atau keluar dari program"
variable Pilihan akan menginput 2 pernyataan yaitu Ya/Tidak
Jika memilih Ya(if), maka akan loop dan dapat menghitung total harga kembali. 
Jika memilih Tidak(else), maka akan keluar dari program exit()

  2). Membuat Flowchart
![MiniProject(1) Daspro - Zyrus Alfredo Randan Malinggato (2409116120)](https://github.com/user-attachments/assets/10a6d58a-c333-418f-ab63-de553f4791c5)
Pada awalan kita memberikan "Mulai" selanjutnya akan di proses pada bagian page Login untuk menginput username & password, setelah itu akan di proses dengan ketentuan 
Username = Zyrus
Password = 120
jika sesuai akan lanjut ke proses berikutnya, jika tidak sesuai akan kembali ke halaman page Login untuk menginput kembali username & password hingga sesuai.
Setelah masuk pada proses Input Harga Barang dengan contoh penulisan (Rp250.000) dan menginput jumlah barang. Selanjutnya akan d proses untuk mengitung total harga barang dari harga barang dan jumlah barang. Selanjutnya, jika Total Harga lebih dari Rp250.000 maka akan mendapatkan diskon sebesar 25%, sebaliknya jika tidak maka tidak akan mendapatkan diskon (Total Harga tetap sama). Setelah melalui proses tersebut output ny akan menampilkan Total Harga dengan ketentuan TotalHarga > 250.000 jika Ya mendapatkan diskon 25% jika Tidak maka tidak akan mendapatkan diskon. Dan terakhir diakhiri dengan selesai

Sekian penjelasan program yang saya buat, terimakasih.
