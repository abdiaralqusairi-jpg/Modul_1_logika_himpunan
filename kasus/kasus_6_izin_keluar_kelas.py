izin_guru = False
keperluan_penting = False

izin_keluar = izin_guru or keperluan_penting

if izin_keluar:
    print("Boleh keluar kelas")
else:
    print("Tidak boleh keluar kelas")