from view.input_nilai import *

data_mahasiswa = {}

# Menambahkan data
def tambah_data():
    global data_mahasiswa
    ulangi = 'y'
    while ulangi =='y':
        nama = input_nama()
        nim = input_nim()
        nilai_tugas = input_tugas()
        nilai_uts = input_uts()
        nilai_uas = input_uas()
        nilai_akhir = akhir()
        data_mahasiswa[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]
        ulangi = (input('tambah data?(y/t) : '))

        if ulangi == 't':
            print('\nData berhasil di tambah!!!')
            return data_mahasiswa

# Menghapus data
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
        print("\nData '{}' berhasil dihapus!!!".format(nama))
    else:
        print("Data '{}' tidak ditemukan!!!".format(nama))

# Mengubah data
def ubah_data():
    nama = input("Masukan nama untuk mengubah data : ")
    if nama in data_mahasiswa.keys():
        print("\nAnda ingin mengubah apa?")
        sub_data = input("(Semua), (NIM), (Tugas), (UTS), (UAS) : ")
        if sub_data.lower() == "semua":
            print("==========================")
            print("Ubah data {}.".format(nama))
            print("==========================")
            data_mahasiswa[nama][1] = input("Ubah NIM         :")
            data_mahasiswa[nama][2] = int(input("Ubah Nilai Tugas : "))
            data_mahasiswa[nama][3] = int(input("Ubah Nilai UTS   : "))
            data_mahasiswa[nama][4] = int(input("Ubah Nilai UAS   : "))
            data_mahasiswa[nama][5] = data_mahasiswa[nama][2] *30/100 + data_mahasiswa[nama][3]*35/100 + data_mahasiswa[nama][4] *35/100
            print("\nBerhasil ubah data!")

        elif sub_data.lower() == "nim":
            data_mahasiswa[nama][1] = input("\nNIM  :")
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "tugas":
            data_mahasiswa[nama][2] = int(input("\nNilai Tugas : "))
            data_mahasiswa[nama][5] = data_mahasiswa[nama][2] *30/100 + data_mahasiswa[nama][3]*35/100 + data_mahasiswa[nama][4] *35/100
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uts":
            data_mahasiswa[nama][3] = int(input("\nNilai UT : "))
            data_mahasiswa[nama][5] = data_mahasiswa[nama][2] *30/100 + data_mahasiswa[nama][3]*35/100 + data_mahasiswa[nama][4] *35/100
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uas":
            data_mahasiswa[nama][4] = int(input("\nNilai UAS : "))
            data_mahasiswa[nama][5] = data_mahasiswaa[nama][2] *30/100 + data_mahasiswa[nama][3]*35/100 + data_mahasiswa[nama][4] *35/100
            print('\nData berhasil di ubah!')
        else:
            print("\nmenu tidak ditemukan!!!")

    else:
        print("Data '{}' tidak ditemukan!!!".format(nama))

# Mencari data
def cari_data():
    print("Mencari data: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari data : ")
    print('\nResult')
    print("==============================================================")
    print("|      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
    print("==============================================================")
    if nama in data_mahasiswa.keys():
        print("| {0:14} | {1:9} | {2:5} | {3:5} | {4:5} | {5:5}"
            .format(nama, data_mahasiswa[nama][1], data_mahasiswa[nama][2], data_mahasiswa[nama][3], data_mahasiswa[nama][4], data_mahasiswa[nama][5]))
        print('--------------------------------------------------------------')
    else:
        print("Data '{}' tidak ditemukan!!!".format(nama))