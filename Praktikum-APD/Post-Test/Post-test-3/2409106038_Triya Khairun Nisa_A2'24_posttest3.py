nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
print(nama + " " + "dengan NIM" + " " + str(nim))

jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
lama_cicilan = int(input("Masukkan lama cicilan [1/2/3]: "))

if lama_cicilan == 1:
    jumlah_bulan = (lama_cicilan * 12)
    bunga_per_bulan = (0.07/12) * int(jumlah_pinjaman)
    cicilan_per_bulan = int((jumlah_pinjaman + bunga_per_bulan) / jumlah_bulan)
    print("Total bunga per bulan Anda adalah " + "Rp." + str(int(bunga_per_bulan)) + " dan cicilan per bulan Anda adalah Rp." + str(cicilan_per_bulan))

elif lama_cicilan == 2:
    jumlah_bulan = (lama_cicilan * 12)
    bunga_per_bulan = (0.13/12) * int(jumlah_pinjaman)
    cicilan_per_bulan = int((jumlah_pinjaman + bunga_per_bulan) / jumlah_bulan)
    print("Total bunga per bulan Anda adalah " + "Rp." + str(int(bunga_per_bulan)) + " dan cicilan per bulan Anda adalah Rp." + str(cicilan_per_bulan))


elif lama_cicilan == 3:
    jumlah_bulan = (lama_cicilan * 12)
    bunga_per_bulan = (0.19/12) * int(jumlah_pinjaman)
    cicilan_per_bulan = int((jumlah_pinjaman + bunga_per_bulan) / jumlah_bulan)
    print("Total bunga per bulan Anda adalah " + "Rp." + str(int(bunga_per_bulan)) + " dan cicilan per bulan Anda adalah Rp." + str(cicilan_per_bulan))

else:
    print("Ulangi Program.")
