from os import read, remove, system
import random, string

def clear():
    print("Enter back to MENU")
    a = input()
    _ = system('cls')
    return menu()

def menu():
    print('\n***** SELAMAT DATANG DI NF LIBRARY *****')
    print('Menu:')
    print ("[1] Penambahan Anggota Baru")
    print ("[2] Penambahan Buku Baru")
    print ("[3] Peminjaman Buku")
    print ("[4] Pengembalian Buku")
    print ("[5] Lihat Data Peminjam")
    print ("[6] Fitur Kelalaian Anggota")
    print ("[7] Keluar")

    a = int(input("Masukan Pilihan Anda: "))
    print("")
    if (a == 1):
        fiturAnggota()
    elif (a == 2):
        fiturBuku()
    elif (a == 3):
        fiturPinjam()
    elif (a == 4):
        fiturKembalikan()
    elif (a == 5):
        fiturLihatData()
    elif (a == 6):
        fiturBonus()
    elif (a == 7): 
        print("Terimakasih Atas Kunjungan Anda🙏")

# Fitur Penambahan Anggota 
def anggotaBaru(Uname, type):
    file = open("anggota.txt", "a")
    kode = "LIB" + ''.join(random.choice(string.digits) for i in range(3))
    file.write(kode + "," + Uname + "," + str(type) + '\n')
    file.close()
    return print("Pnambahan anggota baru dengan kode " + kode + " atas nama " + Uname + " Berhasil!")

def fiturAnggota():
    print("=== Penambahan Anggota Baru ===")
    Uname = input("Masukan Nama Anda: ")
    grup = input("Apakah Anda Merupakan Karyawan NF Group? (Y/T) : ")
    if (grup.upper() == "Y"):
        anggotaBaru(Uname, 1)
    elif (grup.upper() == "T"):
        anggotaBaru(Uname, 2)
    return clear() #Akhir Fitur Penambahan Anggota

# Fitur Penambahan Buku
def bukuBaru(buku, penulis, stokBuku):
    kodeBuku = penulis[0:3]
    kode = ''.join(kodeBuku.upper()) + ''.join(random.choice(string.digits) for j in range(3))
    file = open("buku.txt", "a")
    file.write(kode + "," + buku + "," + penulis + "," + str(stokBuku) + '\n')
    file.close()
    print("Penambahan buku baru dengan kode " + kode + " dan judul "+ buku + " berhasil!")

def fiturBuku():
    print("=== Penambahan Buku ===")
    buku = input("Masukan Judul Buku: ")
    penulis = input("Masukan Nama Penulis: ")
    stokBuku = input("Masukan Stok Buku: ")
    bukuBaru(buku, penulis, stokBuku)
    return clear() #Akhir Penambahan Buku

#Fitur Peminjaman Buku
def readBuku():
    dataBuku = []
    f = open('buku.txt')
    for line in f:
        dataBuku.append(line.strip())
    f.close()
    return dataBuku

def readAnggota():
    dataAnggota = []
    f = open('anggota.txt')
    for line in f:
        dataAnggota.append(line.strip())
    f.close()
    return dataAnggota

def readPinjamBuku():    
    Alist = []
    f = open("peminjaman.txt")
    for i in f:
        Alist.append(i.strip())
    f.close()
    return Alist

def cek_buku(Kbuku):
    for i in readBuku():
        if i[:6] == Kbuku:
            return True
    return False

def cek_anggota(Kanggota):
    for i in readAnggota():
        if i[:6] == Kanggota:
            return True
    return False

def cek_stok(Kbuku):
    dataBuku = readBuku()
    for i in range (len(dataBuku)):
        if dataBuku [i][:6] == Kbuku:
            dataBuku[i] = dataBuku[i].split(",")
            if int(dataBuku[i][-1]) > 0:
                return True
    return False

def kurangStok(Kbuku):
    dataBuku = readBuku()
    for i in range(len(dataBuku)): 
        if dataBuku[i][:6] == Kbuku: 
            dataBuku[i] = dataBuku[i].split(",") 
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) - 1)
            dataBuku[i] = ",".join(dataBuku[i])
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n")
    myfile.close()

def pinjamBuku(Kbuku, Kanggota):
    dataPinjam = readPinjamBuku()
    ada = 0
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == Kbuku:
            dataPinjam[i] = dataPinjam[i]+","+Kanggota
            ada = 1
    if ada == 1:
        f = open('peminjaman.txt',"w+")
        for i in dataPinjam:
            f.write(i+"\n")
        f.close()
    else:
        f = open('peminjaman.txt',"a+")
        f.write(Kbuku + "," + Kanggota+"\n" )
        f.close()

def fiturPinjam():

    print("=== Peminjaman Buku ===")
    Kbuku = input("Masukan Kode buku: ")
    if cek_buku(Kbuku):
            Kanggota = input("Masukan Kode anggota: ")
            if cek_anggota(Kanggota):
                if cek_stok(Kbuku):
                    pinjamBuku(Kbuku, Kanggota)
                    kurangStok(Kbuku)
                    print("Peminjaman buku "+Kbuku+" oleh "+Kanggota+" berhasil.")
                    return clear()
                else:
                    print("Stok buku kosong. Peminjaman gagal.")
                    return menu()
            else:
                print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
                return menu()
    else:
        print("Kode buku tidak ditemukan. Peminjaman gagal.\n")
        return menu() #Akhir Fitur peminjaman


#fitur pengembalian buku
def cek_statusAngggota(Kanggota):
    dataAnggota = readAnggota()
    for i in range(len(dataAnggota)):
        if dataAnggota[i][:6] == Kanggota:
            if dataAnggota[i][-1] == "1":
                return True
            else:
                return False

def tambahStok(Kbuku):
    dataBuku = readBuku()
    for i in range(len(dataBuku)): 
        if dataBuku[i][:6] == Kbuku: 
            dataBuku[i] = dataBuku[i].split(",") 
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) + 1)
            dataBuku[i] = ",".join(dataBuku[i])
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n")
    myfile.close()
                
def anggota_pinjam(Kbuku, Kanggota):
    dataPinjam = readPinjamBuku()
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == Kbuku:
            dataPinjam[i] = dataPinjam[i].split(",")
            if dataPinjam[i].count(Kanggota) == 1:
                return True
            else:
                return False
    
def remove_anggota(Kbuku, Kanggota):
    convert = ""
    tampungan_peminjaman = []
    f = open("peminjaman.txt", "r")
    l = f.readlines()
    for i in range(len(l)):
        l[i]= l[i].strip()
        tampungan_peminjaman.append(l[i].split(","))

    if len(tampungan_peminjaman) > 0:
        for i in range(len(tampungan_peminjaman)):
            if tampungan_peminjaman[i][0] == Kbuku:
                tampungan_peminjaman[i].remove(Kanggota)

    f = open ("peminjaman.txt", "w")
    f.write(convert)
    
    for i in range(len(tampungan_peminjaman)):
        tampungan_peminjaman[i][-1] += "\n"

    f = open("peminjaman.txt", "a")
    for i in range(len(tampungan_peminjaman)):
        convert = ",".join(tampungan_peminjaman[i])
        f.write(convert)
    f.close()

def fiturKembalikan():
    print("=== PENGEMBALIAN BUKU ===")
    Kbuku = input("Masukan Kode Buku: ")
    if cek_buku(Kbuku):
            Kanggota = input("Masukan Kode anggota: ")
            if anggota_pinjam(Kbuku, Kanggota):
                denda = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                if cek_statusAngggota(Kanggota):
                    denda = 1000 * denda
                else:
                    denda = 2500 * denda
                print("Total denda =",denda)
                print("Silakan membayar denda keterlambatan di kasir.") 
                print("Pengembalian buku "+Kbuku+" oleh "+Kanggota+" berhasil.")
                remove_anggota(Kbuku, Kanggota)
               
                tambahStok(Kbuku)
                return clear()

            else:
                print("Kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal.\n")
                return clear()
    else:
        print("Kode buku salah. Pengembalian buku gagal.")
        return clear() #Akhir Pengembalian Buku

#fitur Lihat Data Peminjam
def lihatAnggota():
    temp = []
    dataBuku = {}
    file = open("buku.txt")
    for i in file:
        temp =  i.split(",") 
        dataBuku[temp[0]] = [temp[1],temp[2],str(int(temp[3]))] 
    file.close()

    temp = []
    dataAnggota = {}
    file = open("anggota.txt")
    for i in file:
        temp = i.split(",") 
        dataAnggota[temp[0]] = [temp[1],str(int(temp[2]))] 
    file.close()

    temp = []
    dataPinjam = {}
    file = open("peminjaman.txt")
    for i in file:
        temp = i.split(",") 
        temp[-1] = temp[-1][0:-1]
        dataPinjam[temp[0]] = temp[1:] 
    file.close()

    print("=== DAFTAR PEMINJAMAN BUKU ===")
    for i in dataPinjam.keys():
        nomer = 0
        print("Judul : " + dataBuku[i][0])
        print("Penulis : " + dataBuku[i][1])
        print("Daftar Peminjaman:")
        for j in dataPinjam[i]:
            nomer +=1
            print(str(nomer)+". "+str(dataAnggota[j][0])+("(*)" if dataAnggota[j][1] == "1" else ""))
        print()
    
def fiturLihatData():
    lihatAnggota()
    return clear() #Akhir Lihat Data Peminjam0


# fitur bonus
def bacaDatapinjam(Kbuku, Kanggota):
    dataPinjam = readPinjamBuku()
    ada = 0
    for i in range(len(dataPinjam)): #Ini adalah perulangan 
        if dataPinjam[i][:6] == Kbuku:
            dataPinjam[i] = dataPinjam[i]+","+Kanggota
            ada = 1
    if ada == 1:
        f = open('peminjaman.txt',"r")
        for i in dataPinjam:
            f.close()
   
def removeDataPinjam(Kbuku, Kanggota):
    dataPinjam = readPinjamBuku()
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == Kbuku:
            dataPinjam[i] = dataPinjam[i].split(",")
            dataPinjam[i].remove(Kbuku) and remove(Kanggota)
            if len(dataPinjam[i]) == 1 :
                del dataPinjam[i]
            else:
                dataPinjam[i] = ",".join(dataPinjam[i])
        
    myfile = open('peminjaman.txt', 'w+')
    for i in dataPinjam:
        myfile.write(i + "\n")
    myfile.close()
        
def fiturBonus():
        print("             ====KELALAIAN PENGGUNA====\n")
        print("                 SESUAI DENGAN KENTENTUAN YANG BERLAKU                  ")
        print("JIKA ANGGOTA MENGHILANGKAN ATAU MERUSAK BUKU MAKA AKAN DIKENAKAN DENDA\n")
        print("1. MENGHILANGKAN BUKU")
        print("2. MERUSAK BUKU")
        dendaHilang = 150000
        dendaRusak = 50000
        denda = int(input("Masukan Pilihan Anda: "))
        if denda == 1:
            Kbuku = input("Masukan Kode Buku: ")
            if cek_buku(Kbuku):
                Kanggota = input("Masukan Kode anggota: ")
                if cek_anggota(Kanggota):
                    bacaDatapinjam(Kbuku, Kanggota)
                    print("Anggota dengan kode  " + Kanggota + " Telah melaporkan hilangnya buku milik NF Library dengan kode " + Kbuku)
                    print("Maka anda dikenakan denda sebesar " + str(dendaHilang))
                    removeDataPinjam(Kbuku, Kanggota)
                    print("Silahkan melakukan pembayaran segera. Terimakasih")
                    return clear()
                else:
                    print("Kode anggota tidak terdaftar.\n")
                    return menu()
            else:
                print("Kode buku tidak terdaftar.\n")
            return menu()

        elif denda == 2:
            Kbuku = input("Masukan Kode Buku: ")
            if cek_buku(Kbuku):
                Kanggota = input("Masukan Kode anggota: ")
                if cek_anggota(Kanggota):
                    bacaDatapinjam(Kbuku,Kanggota)
                    print("Anggota dengan kode  " + Kanggota + " Telah melaporkan rusaknya buku milik NF Library dengan kode " + Kbuku)
                    print("Maka anda dikenakan denda sebesar " + str(dendaRusak))
                    print("Silahkan melakukan pengembalian buku dan membayar denda.")
                    return clear()
                else:
                    print("Kode anggota tidak terdaftar.\n")
                    return menu()
            else:
                print("Kode buku tidak terdaftar.\n")
            return menu()

menu()