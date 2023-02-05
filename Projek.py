import time
from datetime import datetime
now = datetime.now()
tanggal = now.strftime("%d - %B - %Y, %H:%M:%S")

print("================== Rental Kendaraan Jaya Abadi ===================")


class Rental:
    def menu():
        print('''\n----------------- Menu -----------------
        1. Sewa Kendaraan
        2. Kembalikan Kendaraan
        3. Daftar Kendaraan
        4. Syarat dan Ketentuan
        5. Keluar 
==========================================================
\n''')
        while True:
            nomor = int(input("Masukan Pilihan: "))
            if (nomor == 1):
                pilih.sewakendaraan()
                pilih.ulang()
            elif (nomor == 2):
                pilih.kembalikan()
                pilih.ulang()
            elif (nomor == 3):
                pilih.daftar()
                pilih.ulang()
            elif (nomor == 4):
                pilih.syarat()
                pilih.ulang()
            elif (nomor == 0):
                time.sleep(0.5)
                print("Terima Kasih, Silakan Input Lagi! ")
                quit()
            elif (nomor == 5):
                print('Terima Kasih, Sampai Bertemu Lagi ^_^ ')
                quit()
            else:
                print('Pilihan tidak tersedia')
                pilih.ulang()

    def ulang():
        time.sleep(1)
        ulang = input('Apakah Anda ingin mencoba lagi? (Y/N) :')
        print('=====================================================')
        if (ulang == 'Yes' or ulang == 'yes' or ulang == 'Y' or ulang == 'y'):
            pilih.menu()
        elif (ulang == 'No' or ulang == 'no' or ulang == 'N' or ulang == "n"):
            time.sleep(0.5)
            print('Terima Kasih, sampai jumpa kembali ^_^ ')
            quit()
        else:
            print("Inputan anda salah ! silakan pilih (Y/N) !")
            pilih.ulang()

    def sewakendaraan():
        time.sleep(1)
        print('\n========== Silakan Isikan Data Penyewa ==========\n')
        while True:
            try:
                nama = str(input("Nama Penyewa : "))
                break
            except ValueError:
                print('Nama tidak menggunakan angka!')
                continue
        jaminan = str(input('Jaminan Penyewa KTP/SIM : '))

        jeniskendaraan = str(
            input('Jenis Kendaraan yang disewa [motor/mobil/truk/bus]: '))
        if jeniskendaraan == 'motor' or jeniskendaraan == 'MOTOR':
            print(''' Silakan Pilih Jenis Motor 

                    1. Beat                             : Rp. 50.000
                    2. Scoopy                           : Rp. 55.000
                    3. Supra X 125                      : Rp. 60.000
                    4. Vario 150                        : Rp. 75.000
                    5. Nmax                             : Rp. 85.000
                    6. Yamaha R25                       : Rp. 90.000
                    7. Yamaha Xabre                     : Rp. 80.000
                    8. Suzuki GSX R150                  : Rp. 70.000
                    9. Honda CBR 150                    : Rp. 87.000
                    10. Kawasaki Ninja 250 SE ABS       : Rp. 75.000
                    (masukan nomor)\n''')
            mtr = input('Jenis Motor : ')
            if mtr == '1':
                harga = 50000
                namamotor = ("Beat")
            elif mtr == '2':
                harga = 55000
                namamotor = ("Scoppy")
            elif mtr == '3':
                harga = 60000
                namamotor = ("Supra X 125")
            elif mtr == '4':
                harga = 75000
                namamotor = ("Vario 150")
            elif mtr == '5':
                harga = 85000
                namamotor = ("Nmax")
            elif mtr == '6':
                harga = 90000
                namamotor = ("Yamaha R25")
            elif mtr == '7':
                harga = 80000
                namamotor = ("Yamaha Xabre")
            elif mtr == '8':
                harga = 70000
                namamotor = ("Suzuki GSX R150")
            elif mtr == '9':
                harga = 87000
                namamotor = ("Honda CBR 150")
            elif mtr == '10':
                harga = 75000
                namamotor = ("Kawasaki Ninja 250 SE ABS")
            else:
                print('Anda salah memasukan input, Silahkan coba lagi !')
                pilih.sewakendaraan()
            while True:
                try:
                    jmlhari = int(input('Jumlah Hari Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            while True:
                try:
                    tgl = int(input('Tanggal Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
            while True:
                try:
                    jmlh = int(input('Jumlah Motor yang disewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            sewamtr = harga*jmlhari
            jml = sewamtr*jmlh
            ppn = jml*0.1
            total = jml+ppn
        elif (jeniskendaraan == 'mobil' or jeniskendaraan == 'MOBIL'):
            print(''' Silakan Pilih Jenis Mobil 

                    1. Brio                     : Rp. 150.000
                    2. Jazz                     : Rp. 150.000
                    3. Avanza                   : RP. 160.000
                    4. Fortuner                 : Rp. 200.000
                    5. HRV                      : Rp. 200.000
                    6. Xpander                  : Rp. 190.000
                    7. Lamborghini Gallardo     : Rp. 500.000
                    8. BMW M3 GTR               : Rp. 450.000
                    9. Lamborghini Murcielago   : Rp. 550.000
                    10. Nissan 350z             : Rp. 350.000
                    (masukan nomor)\n''')
            mbl = input('Jenis Mobil : ')
            if mbl == '1':
                harga = 150000
                namamobil = ("Brio")
            elif mbl == '2':
                harga = 150000
                namamobil = ("Jazz")
            elif mbl == '3':
                harga = 160000
                namamobil = ("Avanza")
            elif mbl == '4':
                harga = 200000
                namamobil = ("Fortuner")
            elif mbl == '5':
                harga = 200000
                namamobil = ("HRV")
            elif mbl == '6':
                harga = 190000
                namamobil = ("Xpander")
            elif mbl == '7':
                harga = 500000
                namamobil = ("Lamborghini Gallardo")
            elif mbl == '8':
                harga = 450000
                namamobil = ("BMW M3 GTR")
            elif mbl == '9':
                harga = 550000
                namamobil = ("Lamborghini Murcielago")
            elif mbl == '10':
                harga = 350000
                namamobil = ("Nissan 350z")
            else:
                print('Anda Salah Memasukan Input, Silahkan Coba Lagi !')
                pilih.sewakendaraan()
            while True:
                try:
                    jmlhari = int(input('Jumlah Hari Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            while True:
                try:
                    tgl = int(input('Tanggal Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
            while True:
                try:
                    jmlh = int(input('Jumlah Mobil yang disewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            sewamtr = harga*jmlhari
            jml = sewamtr*jmlh
            ppn = jml*0.1
            total = jml+ppn
        elif (jeniskendaraan == 'truk' or jeniskendaraan == 'TRUK'):
            print(''' Silakan Pilih Jenis Truk 

                    1. Pick Up      : Rp. 200.000
                    2. Gobang       : Rp. 260.000
                    3. Engkel       : Rp. 290.000
                    4. Fuso         : Rp. 450.000
                    5. Hino Ranger  : Rp. 450.000
                    6. Tronton      : Rp. 500.000
                    7. Kontainer    : Rp. 550.000
                    8. Wingbox      : Rp. 600.000
                    9. Trintin      : Rp. 650.000
                    10. Diesel Colt : Rp. 700.000
                    (masukan nomor)\n''')
            trk = input('Jenis Truk : ')
            if trk == '1':
                harga = 200000
                namatruk = ("Pick Up")
            elif trk == '2':
                harga = 260000
                namatruk = ("Gobang")
            elif trk == '3':
                harga = 290000
                namatruk = ("Engkel")
            elif trk == '4':
                harga = 450000
                namatruk = ("Fuso")
            elif trk == '5':
                harga = 450000
                namatruk = ("Hino Ranger")
            elif trk == '6':
                harga = 500000
                namatruk = ("Tronton")
            elif trk == '7':
                harga = 550000
                namatruk = ("Kontainer")
            elif trk == '8':
                harga = 600000
                namatruk = ("Wingbox")
            elif trk == '9':
                harga = 650000
                namatruk = ("Trintin")
            elif trk == '10':
                harga = 700000
                namatruk = ("Diesel Colt")
            else:
                print('Anda salah memasukan input, silakan coba lagi ! ')
                pilih.sewakendaraan()
            while True:
                try:
                    jmlhari = int(input('Jumlah Hari Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            while True:
                try:
                    tgl = int(input('Tanggal Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
            while True:
                try:
                    jmlh = int(input('Jumlah Truk yang disewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            sewamtr = harga*jmlhari
            jml = sewamtr*jmlh
            ppn = jml*0.1
            total = jml+ppn
        elif (jeniskendaraan == 'bus' or jeniskendaraan == 'BUS'):
            print(''' Silakan Pilih Jenis Bus
            
                    1. Elf (minibus)    : Rp. 100.000
                    2. Medium           : Rp. 300.000
                    3. Big              : Rp. 480.000
                    (masukan nomor)\n''')
            bus = input('Jenis Bus : ')
            if bus == '1':
                harga = 100000
                namabus = ("Elf (minibus)")
            elif bus == '2':
                harga = 300000
                namabus = ("Medium")
            elif bus == '3':
                harga = 480000
                namabus = ("Big")
            else:
                print('Anda salah memasukan input, Silahkan coba lagi !')
                pilih.sewakendaraan()
            while True:
                try:
                    jmlhari = int(input('Jumlah Hari Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            while True:
                try:
                    tgl = int(input('Tanggal Sewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
            while True:
                try:
                    jmlh = int(input('Jumlah Bus yang disewa : '))
                    break
                except ValueError:
                    print('Anda salah memasukan input! Silakan coba lagi')
                    continue
            sewamtr = harga*jmlhari
            jml = sewamtr*jmlh
            ppn = jml*0.1
            total = jml+ppn
        else:
            print("Anda salah memasukan data, silahkan coba lagi !")
            pilih.sewakendaraan()

        print('\n\n')
        print('================= STRUK PEMBAYARAN ==================')
        print('Struk ini dicetak pada       : ', tanggal)
        print('Nama Penyewa                 : ', nama)
        print('Jaminan                      : ', jaminan)
        print('Jenis Kendaraan              : ', jeniskendaraan)
        if jeniskendaraan == 'motor' or jeniskendaraan == 'MOTOR':
            print("Nama Kendaraan Motor         : ", namamotor)
        elif jeniskendaraan == 'mobil' or jeniskendaraan == 'MOBIL':
            print("Nama Kendaraan Mobil         : ", namamobil)
        elif jeniskendaraan == 'bus' or jeniskendaraan == 'BUS':
            print("Jenis Bus yang dirental      : ", namabus)
        elif jeniskendaraan == 'truk' or jeniskendaraan == 'TRUK':
            print("Nama Kendaraan Truk          : ", namatruk)
        print('Jumlah Hari sewa             : ', jmlhari)
        print('Tanggal Penyewaan            : ', tgl)
        print('Jumlah Kendaraan yang disewa : ', jmlh)
        print('Jumlah Bayar                 : Rp.', jml)
        print('Pajak 10%                    : Rp.', ppn)
        print('===================================================')
        print('Total Bayar                  : Rp.', total)
        uang = int(input("Uang Tunai Pembeli           :     "))
        print('Kembalian                    : Rp.', (uang-total))

    def kembalikan():
        time.sleep(1)
        nama = str(input('Nama Penyewa : '))
        jenis = str(input('Jenis Kendaraan : '))
        jmlknd = int(input('Jumlah Kendaraan : '))
        while True:
            try:
                tgl = int(input('Tanggal Sewa : '))
                break
            except ValueError:
                print('Anda salah memasukan input! Silakan coba lagi')
        while True:
            try:
                tgl2 = int(input('Tanggal Pengembalian : '))
                break
            except ValueError:
                continue
        while True:
            try:
                tgl3 = int(input('Tanggal Sekarang : '))
                break
            except ValueError:
                print('Anda salah memasukan input! Silakan coba lagi')
        if tgl3 > tgl2:
            print('ANDA TELAT MENGEMBALIKAN, ANDA AKAN DIKENAKAN DENDA 7500 PER JAM !\n')
            jam = int(input('Jumlah Jam Lewat : '))
            denda = jam*7500
        else:
            print('Terima Kasih telah mengembalikan tepat waktu  ^_^ ')
            denda = 0
        print('==================== Struk Pengembalian ====================\n')
        print('Nama Penyewa             : ', nama)
        print('Jenis Kendaraan          : ', jenis)
        print('Jumlah Kendaraan         : ', jmlknd)
        print('Tanggal Sewa             : ', tgl)
        print('Tanggal Pengembalian     : ', tgl2)
        print('Denda                    : ', denda)
        print('Struk ini dicetak pada   : ', tanggal)
        print('''=============================================================
        \nTerima Kasih sudah menyewa di tempat kami, kepuasan Anda adalah prioritas kami''')
        pilih.ulang()
        quit()

    def daftar():
        time.sleep(1)
        print(''' \t\tDaftar Kendaraan PT. Jaya Abadi
                \n\n
                1. Motor -->    A. Beat                         : Rp. 50.000
                                B. Scoopy                       : Rp. 55.000
                                C. Supra X 125                  : Rp. 60.000
                                D. Vario 150                    : Rp. 75.000
                                E. Nmax                         : Rp. 85.000
                                F. Yamaha R25                   : Rp. 90.000
                                G. Yamaha Xabre                 : Rp. 80.000
                                H. Suzuki GSX R150              : Rp. 70.000
                                I. Honda CBR 150                : Rp. 87.000
                                J. Kawasaki Ninja 250 SE ABS    : Rp. 75.000
                \n\n                
                2. Mobil -->    A. Brio                     : Rp. 150.000
                                B. Jazz                     : Rp. 150.000
                                C. Avanza                   : Rp. 160.000
                                D. Fortuner                 : Rp. 200.000
                                E. HRV                      : Rp. 200.000
                                F. Xpander                  : Rp. 190.000
                                7. Lamborghini Gallardo     : Rp. 500.000
                                8. BMW M3 GTR               : Rp. 450.000
                                9. Lamborghini Murcielago   : Rp. 550.000
                                10. Nissan 350z             : Rp. 350.000
                \n\n
                3. Truk -->     1. Pick Up      : Rp. 200.000
                                2. Gobang       : Rp. 260.000
                                3. Engkel       : Rp. 290.000
                                4. Fuso         : Rp. 450.000
                                5. Hino Ranger  : Rp. 450.000
                                6. Tronton      : Rp. 500.000
                                7. Kontainer    : Rp. 550.000
                                8. Wingbox      : Rp. 600.000
                                9. Trintin      : Rp. 650.000
                                10. Diesel Colt : Rp. 700.000

                \n\n
                4. Bus -->      A. Elf (minibus)      : Rp. 100.000
                                B. Medium Bus         : Rp. 300.000
                                C. Big Bus            : Rp. 480.000
                                \n\n''')

    def syarat():
        time.sleep
        print('''============================ Syarat Dan Kentetuan ================================
        1. Penyewa harus Memberikan Jaminan Berupa KTP/SIM
        2. Harus Memiliki SiM A B dan C
        3. Minimal Ber Usia 18 tahun
        4. Segala Jenis Kerusakan Menjadi Tanggung Jawab Penyewa
        5. Sewa Maksimal 1 Minggu
        6. Pihak rental Berhak Membatalkan Sewa Jika Data tidak Lengkap
        7. Keterlambatan Pengembalian Akan Dikenakan Denda Seusai Waktu
        8. Keterlambatan Pengembalian setiap 1 jam akan di kenakan biaya 7500
        9. Motor hanya di pakai di wilayah Sejabodetabek
        10. Segala tindak kejahatan akan kami serahkan kepada pihak yang Berwajib
        11. Penyewa Memahami dan Mengikuti Syarat Dan ketentuan yang tertera di atas
        \n''')


pilih = Rental
pilih.menu()
