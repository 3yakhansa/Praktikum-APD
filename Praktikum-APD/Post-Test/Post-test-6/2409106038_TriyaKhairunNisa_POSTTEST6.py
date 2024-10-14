
print("""
     =======================================================
     | Selamat Datang di Manajemen Data Webtoon Indonesia  |
     |               Silahkan Registrasi!                  |
     =======================================================
    """)

#Penyimpanan Data

users = {}

while True:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            role = input("Masukkan role (admin/pengguna): ")
            
            if role == "admin" or role == "pengguna":
                 users.update({'username' : username, 
                               'password' : password,
                               'role' : role})
                 print("Registrasi berhasil!")
                 break
            else:
                 print("gagal login")

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
                komik_webtoon ={}
                while True:
                    pilih = int(input("PILIH: "))
                    if pilih == 1:
                          judul = input("Judul Webtoon: ")
                          pembaca = input("Jumlah Pembaca: ")
                          genre = input("Genre: ")
                          rating = input("Rating: ")
                          komik_webtoon[judul] = {
                                'Pembaca': pembaca,
                                'Genre': genre,
                                'Rating': rating
                                }
                          
                    elif pilih == 2:
                                for i in range(len(komik_webtoon)):
                                            print(komik_webtoon)
                                            break
                            
                    elif pilih == 3:
                                judul_lama = input("Judul Webtoon lama: ")
                                if judul_lama == judul:
                                    pembaca_baru = input("Masukkan jumlah pembaca baru: ")
                                    genre_baru = input("Masukkan genre baru: ")
                                    rating_baru = input("Masukkan rating baru: ")
                                    komik_webtoon[judul] = {
                                    'Pembaca': pembaca_baru,
                                    'Genre': genre_baru,
                                    'Rating': rating_baru
                                    }
                                else:
                                    print("Data tidak valid.")
                                    
                                                         
                    elif pilih == 4:
                         judul_hapus = input("Masukkan judul yang ingin dihapus: ")
                         if komik_webtoon.get(judul_hapus):
                                komik_webtoon.pop(judul_hapus)
                         else:
                            print("Data tidak")
         
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
                komik_webtoon = {}
                while True:
                    pilih = int(input("PILIH: "))
                    if pilih == 1:
                          judul = input("Judul Webtoon: ")
                          pembaca = input("Jumlah Pembaca: ")
                          genre = input("Genre: ")
                          rating = input("Rating: ")
                          komik_webtoon[judul] = {
                                'Pembaca': pembaca,
                                'Genre': genre,
                                'Rating': rating
                                }
                          
                    elif pilih == 2:
                                for i in range(len(komik_webtoon)):
                                            print(komik_webtoon)
                                            break
                            
                    elif pilih == 3:
                                judul_lama = input("Judul Webtoon lama: ")
                                if judul_lama == judul:
                                    pembaca_baru = input("Masukkan jumlah pembaca baru: ")
                                    genre_baru = input("Masukkan genre baru: ")
                                    rating_baru = input("Masukkan rating baru: ")
                                    komik_webtoon[judul] = {
                                    'Pembaca': pembaca_baru,
                                    'Genre': genre_baru,
                                    'Rating': rating_baru
                                    }
                                else:
                                    print("Data tidak valid")
                                    
                    elif pilih == 4:
                       print("Terima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia")
                       exit()      
                  
                
    else:
         print("Gagal Login.")
         login += 1
           
else:
     print("Silahkan Ulangi Program.")