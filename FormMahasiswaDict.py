print("="*50)
print("                 Program Input Data")
print("="*50)

dict = {}
while True:
    print("Pilih Menu Yang Disediakan")
    data = input("[(l)ihat,(t)ambah,(u)bah,(h)apus,(c)ari,(k)eluar] : ")

    if data == "l" or data == "L":
        if dict.items():
            print("Daftar Nilai")
            print("-"*73)
            print("|No. |    Nama    |     NIM     |  UTS  |  UAS  |  Tugas  |  Akhir       |")
            print("-"*73)
            i = 0 
            for y in dict.items():
                i += 1
                print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7} |".format
                (y[0][:50], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))        
        else:
            print("Daftar Nilai")
            print("-"*73)
            print("|No. |    Nama    |     NIM     |  UTS  |  UAS  |  Tugas  |  Akhir       |")
            print("-"*73)
            print("|                           TIDAK ADA DATA                               |") 
            print("-"*73)      
    elif data == 't' or data == 'T':
        print("Tambah Data")
        nama = input("Masukan Nama        : ")
        nim = int(input("Masukan NIM         : "))
        tugas = int(input("Nilai Tugas         : "))
        uts = int(input("Nilai UTS           : "))
        uas = int(input("Nilai UAS           : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        dict[nama] = nim, uts, uas, tugas, hasil
    elif data == 'u' or data == 'U':
        print("Ubah Data")
        nama = input("Masukan Nama            : ")
        if nama in dict.keys():
            nim = int(input("Masukan NIM         : "))
            tugas = int(input("Nilai Tugas         : "))
            uts = int(input("Nilai UTS           : "))
            uas = int(input("Nilai UAS           : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35                
            dict[nama] = nim, tugas, uts, uas, hasil
        else:
            print("Nama {0} Tidak di Tentukan".format(nama))
    elif data == "h" or data == "H":
        print("Hapus Data")
        nama = input("Masukan Nama      : ")    
        if nama in dict.keys():
            del dict[nama]
        else:
            print("Nama {0} Tidak di Temukan".format(nama))
    elif data == "c" or data == "C":
        print("cari Data")            
        nama = input("Masukan Nama      : ")
        if nama in dict.keys():
            print("-"*73)
            print("Daftar Nilai")  
            print("-"*73)
            print("Nama  :",nama)
            print("Nim   :", nim)
            print("UTS   :", uts)
            print("UAS   :", uas)
            print("tugas :", tugas)
            print("Hasil :",hasil)
            print("-"*73)
        else:
            print("Nama {0} Tidak di Tentukan".format(nama))
    elif data == "k" or data == "K":
        print("Terima Kasih")
        break
    else:
        print("Pilih Menu Yang Disediakan")