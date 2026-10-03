kursi_depan = False
kursi_belakang = False

pilihan_kursi = kursi_depan ^ kursi_belakang

if pilihan_kursi:
    print("Pilihan kursi valid")
else:
    print("Pilihan kursi tidak valid")