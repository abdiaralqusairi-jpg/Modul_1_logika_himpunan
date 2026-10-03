prestasi_akademik = False
prestasi_nonakademik = True

bantuan = prestasi_akademik or prestasi_nonakademik

if bantuan:
    print("Berhak mendapatkan bantuan")
else:
    print("Tidak mendapatkan bantuan")