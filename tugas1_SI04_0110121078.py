print('***********************************')
print('   Form Pendaftaran Anggota Baru')
print('***********************************')
print()

import datetime
import sys
import re

username = input("Nama Lengkap: ")


tglLahir = input("Tanggal Lahir (format DD-MM-YYYY): ")
tanggalLahir = datetime.datetime.strptime(tglLahir, "%d-%m-%Y")
tanggal = datetime.datetime.today().year - tanggalLahir.year
usia = tanggal

if usia >= 17:
    True
else:
    print("Mohon maaf. Anda belum mencukupi untuk menjadi anggota.")
    sys.exit()



penghasilan = int(input("Penghasilan Per bulan: "))
if penghasilan < 5000000:
    kelas = 'Silver'
elif penghasilan >= 5000000 and penghasilan < 10000000:
    kelas = 'Gold'
else:
    kelas = 'Diamond'




while True:
    address = str(input("Email Address:  "))
    if(re.match('.+@.+', address)) is None:
        print("Email tidak valid. Ulangi")
    elif(re.search('.com', address)) is None:
        print("Email tidak valid. Ulangi")
    elif(re.search('mail', address)) is None:
        print("Email tidak valid. Ulangi")
    else:
        break



while True:
    password = input("Masukan Password: ")
    if len(password) < 8:
        print("Pastikan password anda minimal 8 huruf dan memiliki huruf kapital, angka, dan karakter spesial didalamnya")
    elif re.search('[0-9]',password) is None:
        print("Pastikan password anda minimal 8 huruf dan memiliki huruf kapital, angka, dan karakter spesial didalamnya")
    elif re.search('[A-Z]',password) is None: 
        print("Pastikan password anda minimal 8 huruf dan memiliki huruf kapital, angka, dan karakter spesial didalamnya")
    elif re.search('[@, #, $, !]', password) is None:
        print("Pastikan password anda minimal 8 huruf dan memiliki huruf kapital, angka, dan karakter spesial didalamnya")
    else:
        break



while True:
    confirm = input("Konfirmasi Password: ")
    if confirm != password:
        print("Password tidak sesuai")
    else:
        break


print("")
print("Pendaftaran berhasil. Berikut data Anda:")
print("Nama: ", username)
print("Email: ", address)
print("Level: ", kelas)