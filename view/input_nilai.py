# Menginput data
def input_nama():
    print("\nMasukkan data mahasiswa")
    global nama
    nama = input("\nNama : ")
    return nama


def input_nim():
    global nim
    nim = input("NIM  : ")
    return nim


def input_tugas():
    global nilai_tugas
    nilai_tugas = int(input("Masukkan nilai tugas : "))
    return nilai_tugas


def input_uts():
    global nilai_uts
    nilai_uts = int(input("Masukkan nilai UTS   : "))
    return nilai_uts


def input_uas():
    global nilai_uas
    nilai_uas = int(input("Masukkan nilai UAS   : "))
    return nilai_uas


# Nilai akhir
def akhir():
    global nilai_akhir
    nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100
    return nilai_akhir