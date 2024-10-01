login = 0

while(login<3):
   username = input("Masukkan nama: ")
   password = input("Masukkan Password: ")
   if username == "triya" and password == "38":
      print("Berhasil login.") 
        
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
         
      ulang = input("Ulang?[ya/tidak]: ")
      if ulang == "ya":
         continue
      else:
         break 
   else:
         login += 1
         print("Ulangi lagi")

print("Kesempatan Anda sudah habis.")

         





   