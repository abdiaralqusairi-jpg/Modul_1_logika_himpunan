sudah_daftar = True
membawa_kartu_pelajar = True
hadir_tepat_waktu = False

ikut_lomba = sudah_daftar and membawa_kartu_pelajar and hadir_tepat_waktu

if ikut_lomba:
    print("Peserta boleh mengikuti lomba")
else:
    print("Peserta tidak boleh mengikuti lomba")