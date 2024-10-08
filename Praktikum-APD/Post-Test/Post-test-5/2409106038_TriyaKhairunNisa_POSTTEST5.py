
print("""
     =======================================================
     | Selamat Datang di Manajemen Data Webtoon Indonesia  |
     |               Silahkan Registrasi!                  |
     =======================================================
    """)

#Penyimpanan Data

users = []
komik_webtoon = []

while True:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            role = input("Masukkan role (admin/pengguna): ")


            if role not in ["admin", "pengguna"]:
                    print("Pilih role admin atau pengguna.")
                
            for username in users:
                    if users[1] == username:
                        print("Username sudah terdaftar. Silakan gunakan username lain.")

            users.append([username, password, role])
            print("Registrasi berhasil!")
            break
            


login = 0
while login < 3:
    print("================= Login User =========================")
    username_in = input("Masukkan Username : ")
    password_in = input("Masukkan Password : ")
    role_in = input("Masukkan role (admin/pengguna): ")
    if username_in == username and password_in == password and role_in == "admin":
         while True:
 
                print("""
                    ==================================================
                    [      MANAJEMEN DATA KOMIK WEBTOON INDONESIA     ]
                    ==================================================
                    [1. TAMBAH DATA                                   ]
                    [2. TAMPILKAN DATA                                ]
                    [3. UBAH DATA                                     ]
                    [4. HAPUS DATA                                    ]
                    [5. KELUAR                                        ]
                    ===================================================
                    """)
                
                #Pendataan
                komik_webtoon =[]
                while True:
                    pilih = int(input("PILIH: "))
                    if pilih == 1:
                          judul = input("Judul Webtoon: ")
                          pembaca = input("Jumlah Pembaca: ")
                          genre = input("Genre: ")
                          rating = input("Rating: ")
                          komik_webtoon.append([judul,pembaca,genre,rating])
                    elif pilih == 2:                       
                          for i in range(len(komik_webtoon)):
                            print(f"\n komik_webtoon ke-{i+1}\nJUDUL : {komik_webtoon[i][0]}\nJUMLAH PEMBACA : {komik_webtoon[i][1]}\nGENRE : {komik_webtoon[i][2]}\nRATING: {komik_webtoon[i][3]}")
                            break   
                    elif pilih == 3:
                          judul_lama = input("Judul yang ingin diganti: ")
                          for i in range(len(komik_webtoon)):
                               if judul_lama == komik_webtoon[i][0]:
                                    komik_webtoon[i][0] = input("Judul baru: ")
                                    komik_webtoon[i][1] = input("Jumlah Pembaca baru: ")
                                    komik_webtoon[i][2] = input("genre baru: ")
                                    komik_webtoon[i][3] = input("Rating baru: ")
                               else:
                                    print("Data tidak ditemukan")                                   
                    elif pilih == 4:
                         judul_hapus = input("Masukkan judul yang ingin dihapus: ")
                         for i in range(len(komik_webtoon)):
                            if judul_hapus == komik_webtoon[i][0]:
                                del komik_webtoon[i]
                                break
                                
                    elif pilih == 5:
                       print("Terima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia")
                       exit()   

                    
                    

    elif username_in == username and password_in == password and role_in == "pengguna":
        while True:     
                print("""
                    ==================================================
                    [      MANAJEMEN DATA KOMIK WEBTOON INDONESIA     ]
                    ==================================================
                    [1. TAMBAH DATA                                   ]
                    [2. TAMPILKAN DATA                                ]
                    [3. UBAH DATA                                     ]
                    [4. KELUAR                                        ]
                    ===================================================
                    """)
                
                #Pendataan
                komik_webtoon = []
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1:
                        judul = input("Judul Webtoon: ")
                        pembaca = input("Jumlah Pembaca : ")
                        genre = input("Genre: ")
                        rating = input("Rating: ")
                        komik_webtoon.append([judul,pembaca,genre,rating])
                        

                    elif pilih == 2:
                        for i in range(len(komik_webtoon)):
                            print(f"\n komik_webtoon ke-{i+1}\nJUDUL : {komik_webtoon[i][0]}\nJUMLAH PEMBACA : {komik_webtoon[i][1]}\nGENRE : {komik_webtoon[i][2]}\nRATING: {komik_webtoon[i][3]}")
                            break   
                    elif pilih == 3:
                        judul_lama = input("Judul yang ingin diganti: ")
                        for i in range(len(komik_webtoon)):
                               if judul_lama == komik_webtoon[i][0]:
                                    komik_webtoon[i][0] = input("Judul baru: ")
                                    komik_webtoon[i][1] = input("Jumlah Pembaca baru: ")
                                    komik_webtoon[i][2] = input("genre baru: ")
                                    komik_webtoon[i][3] = input("Rating baru: ")
                               else:
                                    print("Data tidak ditemukan") 
                    elif pilih == 4:
                        print("Terima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia")
                        exit()        
                  
                
    else:
         print("Gagal Login.")
         login += 1
           
else:
     print("Silahkan Ulangi Program.")