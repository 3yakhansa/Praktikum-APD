def salam():
    print("""
        =======================================================
        | Selamat Datang di Manajemen Data Webtoon Indonesia  |
        |               Silahkan Registrasi!                  |
        =======================================================
        """)
salam()

users={}

username = input("Masukkan username: ")
password = input("Masukkan password: ")
role = input("Masukkan role (admin/pengguna): ")

def data_user(username, password,role):    
    while True:               
        if role == "admin" or role == "pengguna":
            users.update({'username' : username, 
                            'password' : password,
                            'role' : role})
            print("Registrasi berhasil!")
            break
        else:
            print("Pilih role antara admin atau pengguna.")
            role = input("Masukkan role [admin/pengguna]: ")
            users.update({'role' : role})

def login_user(login=0):
    if login >= 3:
        print("Terlalu banyak percobaan. Program akan keluar.")
        exit()

    print("================= Login User =========================")
    username_in = input("Masukkan Username: ")
    password_in = input("Masukkan Password: ")
    role_in = input("Masukkan role (admin/pengguna): ")

    if username_in == username and password_in == password and role_in == "admin":
        show_menu_admin()
        return True
    elif username_in == username and password_in == password and role_in == "pengguna":
        show_menu_pengguna()
        return True
    else:
        print("Gagal login.")
        return login_user(login + 1)

         
komik_webtoon = {}

def tambah_data():
    judul = input("Judul Webtoon: ")
    pembaca = input("Jumlah Pembaca: ")
    genre = input("Genre: ")
    rating = input("Rating: ")
    komik_webtoon[judul] = {
            'Pembaca': pembaca,
            'Genre': genre,
            'Rating': rating
            }          

def tampil_data():
    if komik_webtoon:
        for judul, data in komik_webtoon.items():
            print(f"{judul}: {data}")
    else:
        print("Tidak ada data untuk ditampilkan.")

def update_data():
    judul_lama = input("Judul Webtoon lama: ")
    if judul_lama in komik_webtoon:
        pembaca_baru = input("Masukkan jumlah pembaca baru: ")
        genre_baru = input("Masukkan genre baru: ")
        rating_baru = input("Masukkan rating baru: ")
        komik_webtoon[judul_lama] = {
                'Pembaca': pembaca_baru,
                'Genre': genre_baru,
                'Rating': rating_baru
                }
        print(f"Data {judul_lama} berhasil diubah.")
    else:
        print("Data tidak valid.")
                

def hapus_data():
    judul_hapus = input("Masukkan judul yang ingin dihapus: ")
    if judul_hapus in komik_webtoon:
        komik_webtoon.pop(judul_hapus)
        print(f"Data {judul_hapus} berhasil dihapus.")
    else:
        print("Data tidak valid.")

def end_data():
    print("Terima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia")
    exit()
       

def show_menu_admin():     
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
    while True:
        try:
            pilihan = int(input("PILIH: "))        
            if pilihan == 1:
                    tambah_data()
            elif pilihan == 2:
                    tampil_data()
            elif pilihan == 3:
                    update_data()
            elif pilihan == 4:
                    hapus_data()
            elif pilihan == 5:
                end_data()
        except ValueError:
            print("Pilihan tidak valid. Pilih angka 1/2/3/4/5")


def show_menu_pengguna(): 
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
    while True:
        try:
            pilihan = int(input("PILIH: "))        
            if pilihan == 1:    
                tambah_data()
            elif pilihan == 2:
                tampil_data()
            elif pilihan == 3:
                update_data()
            elif pilihan == 4:
                end_data()
        except ValueError:
            print("Pilihan tidak valid. Pilih angka 1/2/3/4/5")

while True:
      data_user(username, password,role)
      login_user()