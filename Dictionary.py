daftar = {"Nama": "Nomor Pengguna"}
kontak = {"Ari": "081267888","Dina": "087677776"}

print("# Nama   | Nomor Pengguna")
for daftar in kontak:
   print("# {:6} | {:10}".format(daftar ,kontak[daftar]))

print('> Menampilkan Kontak Ari | Ari :',kontak['Ari'])

kontak['Riko']='087654544'
print('> Menambahkan Kontak Riko Dengan Nomor 087654544')
print("Data Sesudah Di Ubah")
print("# Nama   | Nomor Pengguna")
for daftar in kontak:
    print("# {:6} | {:10}".format(daftar ,kontak[daftar]))

kontak['Dina']='088999776'
print('> Mengubah Kontak Dina Dengan Nomor 088999776')
print("Data Sesudah Di Ubah")
print("# Nama   | Nomor Pengguna")
for daftar in kontak:
    print("# {:6} | {:10}".format(daftar ,kontak[daftar]))

print('> Menampilkan Semua Nama')
print(kontak.keys())
print('> Menampilkan Semua Nomor')
print(kontak.values())
print('> Menampilkan Semua Item')
print(kontak.items())

del kontak['Dina']
print('> Menghapus Kontak Dina')
print("Data Sesudah Di Ubah")
print("# Nama   | Nomor Pengguna")
for daftar in kontak:
    print("# {:6} | {:10}".format(daftar ,kontak[daftar]))