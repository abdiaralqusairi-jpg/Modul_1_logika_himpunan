skor_kredit_bagus = True
penghasilan_stabil = True
tidak_ada_uang_macet = True

setuju_kredit = skor_kredit_bagus and penghasilan_stabil and tidak_ada_uang_macet 

if setuju_kredit:
  print("pengajuan kredit DISETUJUI")
else:
  print("pengajuan kredit DITOLAK")

