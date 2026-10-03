jalur_online = True
jalur_offline = False

pilihan = jalur_online ^ jalur_offline

if pilihan:
    print("Pilihan jalur valid")
else:
    print("Pilihan jalur tidak valid")