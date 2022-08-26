#capstone module 1 
#berisikan datacollection (inputasi )
#conditional statement (if, elseif,else)
#looping (for,while,etc)

#project capstone rental mobil 

from re import A
from tkinter import N
from turtle import back
print('Rental Mobil Purwadhika')
nama_penyewa = input('masukkan nama anda :\n')
nomor_ktp  = int(input('maskkan nomor ktp yang bersangkutan: \n '))
nomor_sim = input('masukkan nomor sim anda :\n')
Avanza_harian = 500000
total_1 = 2 
Pregio_harian = 750000
total_2= 2
Toyota_commuter_harian = 1500000
total_3=2
Travello_harian = 800000
total_4 = 1
isuzu_elf_harian = 800000
total_5 = 1
medium_bus_harian =1750000
total_6= 1

print('data list di bawah adalah harga penyewaan')
print('termasuk bbm , mobil dalam 24 jam dan juga supir ')
print(('harga harian avansa {}+sopir+bbm termasuk'.format(Avanza_harian)))
print('kode nama untuk di input 1')
print(('harga harian pregio {}+sopir+bbm termasuk'.format(Pregio_harian)))
print('kode nama untuk input 2')
print(('harga harian toyota commuter {}+sopir+bbm termasuk'.format(Toyota_commuter_harian)))
print ('kode nama untuk input 3')
print(('harga harian travello  {}+sopir+bbm termasuk'.format(Travello_harian)))
print('kode nama untuk input 4')
print(('harga harian isuzu elf {}+sopir+bbm termasuk'.format(isuzu_elf_harian)))
print('kode nama untuk input 5')
print(('harga harian medium bus harian {}+sopir+bbm termasuk'.format(medium_bus_harian)))
print('kode nama untuk input 6')
print('untuk jenis mobil yang di pilih ')
print('dapat di input pada terimnal')
jenis_mobil=(int(input('jenis mobil yang mana yang ingin di gunakan'))) 

if (jenis_mobil==1) :
        total_mobil_disewa_elf = 0
        total_mobil_disewa_travello = 0
        total_mobil_disewa_medium_bus= 0
        total_mobil_disewa_toyota_commuter = 0
        total_mobil_disewa_pregio =0   
        jenis_mobil = ('avanza')
        print('avansa cocok untuk keluarga muat untuk 5 orang nyaman dan pilihan yang baik dengan harga {} / hari '.format(Avanza_harian))
        while(True):
            total_mobil_disewa_avanza = int(input('masukkan mobil avanza yang ingin di sewa'))
            if(total_mobil_disewa_avanza > total_1) :
                    print ('jumlah mobil yang ingin di pinjam tidak cukup \n jumlah avanza hanya :'+str(total_1))
            else: 
             print('mobil avanza siap di sewa ')
             break
         

elif (jenis_mobil==2) : 
        total_mobil_disewa_avanza=0
        total_mobil_disewa_elf=0
        total_mobil_disewa_medium_bus=0
        total_mobil_disewa_toyota_commuter =0
        total_mobil_disewa_travello =0
        jenis_mobil = ('pregio')
        print('pregio jenis mobil mini bus bisa muat sekitar 7 orang dapat menempuh jalan jauh hingga keluar kota dengan harga {}'.format(Pregio_harian))
        while(True):
            total_mobil_disewa_pregio = int(input('masukkan mobil preggio yang ingin di sewa'))
            if(total_mobil_disewa_pregio > total_2) : 
            
                print('jumlah mobil yang ingin di pinjam tidak cukup \n jumlah mobil preggio hanya : '+str(total_2))
            else:
                print('mobil pregio siap untuk di sewa')
            break    
elif (jenis_mobil==3) : 
    total_mobil_disewa_avanza =0 
    total_mobil_disewa_elf=0
    total_mobil_disewa_medium_bus=0
    total_mobil_disewa_travello=0
    total_mobil_disewa_pregio = 0
    jenis_mobil=('toyota commuter')
    print('toyota commuter adalah jenis mobil travel yang luar biasa dengan suspensi bagus dapat memuat orang 12 dengan harga {}'.format(Toyota_commuter_harian))
    while(True): 
            total_mobil_disewa_toyota_commuter = int(input('maskkan jumlah mobil toyota commuter yang ingin di sewa'))
            if(total_mobil_disewa_toyota_commuter > total_3):
                print(f'jumlah mobil toyota commuter yang ingin di pinjam '+str(total_3))
            else:
                print('mobil toyota commuter siap untuk di sewa ')
            break
elif (jenis_mobil==4)  :
    total_mobil_disewa_avanza =0 
    total_mobil_disewa_toyota_commuter =0 
    total_mobil_disewa_elf=0
    total_mobil_disewa_pregio=0
    total_mobil_disewa_medium_bus =0 
    jenis_mobil=('travello')
    print('travello merupakan jenis mini  travel yang bisa dalam perjalanan jauh di rekomendasikan jumlah penumpang ... cocok untuk keluar kota dengan harga{}'.format(Travello_harian))
    while(True):
            total_mobil_disewa_travello= int(input('masukkan jumlah mobil travello yang ingin di sewa'))
            if(total_mobil_disewa_travello > total_4):
                print(f'jumlah mobil travello yang ingin di pinjam tidak mencukupi'+str(total_4))
            else:
                print('mobil travello siap untuk di sewa')
            break
elif(jenis_mobil==5) : 
    total_mobil_disewa_avanza = 0
    total_mobil_disewa_pregio =0 
    total_mobil_disewa_medium_bus =0 
    total_mobil_disewa_toyota_commuter=0
    total_mobil_disewa_travello=0
    jenis_mobil = ('izusu elf')
    print('izusu elf harian merupakan mobil yang sangat luas jumlah penumpang yang di rekomendasikan sekitar ... dengan biaya ')
    while(True):
            total_mobil_disewa_elf= int(input('masukkan jumlah mobil elf yang ingin di sewa : '))
            if(total_mobil_disewa_elf > total_5):
                print(f'jumlah mobil elf tidak mencukupi'+str(total_5))
            else : 
                print('mobil elf yang ingin disewa siap untuk di sewa')
            break
elif(jenis_mobil==6):
    total_mobil_disewa_avanza =0 
    total_mobil_disewa_pregio=0
    total_mobil_disewa_toyota_commuter =0 
    total_mobil_disewa_elf = 0
    total_mobil_disewa_travello=0
    jenis_mobil = ('medium bus')
    print('medium bus adalah kategori terbesar dalam bisnis rental mobil ini dengan kapasitas ... dan dengan biaya sewa {}')
    while(True):
            total_mobil_disewa_medium_bus= int(input('masukan jumlah mobil medium bus yang ingin di sewa : '))
            if(total_mobil_disewa_medium_bus > total_6):
                print(f'jumlah mobil medium bus tidak mencukup'+str(total_6))
            else : 
                print('mobil medium bus yang ingin di sewa siap ')    
            break
else :
        print('kesalahan pengetikan jalankan ulang terminal ')

verivikasi_ulang = int(input('verivikasi ulang kode jenis mobil :'))
print('tunggu beberapa saat data sewa {} sedang di proses '.format(nama_penyewa))
for tunggu in range(30) :
    print('tunggu dalam beberapa detik{}'.format(tunggu))
print('data penyewa sudah di terima ')
print('berapa lama anda ingin menyewa?')
lama_penyewaan = int(input('input durasi penyewaan yang di inginkan :'))
if (verivikasi_ulang ==1) :
    total_pembayaran = Avanza_harian *total_mobil_disewa_avanza * lama_penyewaan
elif (verivikasi_ulang == 2) : 
    total_pembayaran =  Pregio_harian*total_mobil_disewa_pregio * lama_penyewaan
elif (verivikasi_ulang== 3) : 
    total_pembayaran = Toyota_commuter_harian* total_mobil_disewa_toyota_commuter * lama_penyewaan
elif (verivikasi_ulang == 4): 
    total_pembayaran = Travello_harian * total_mobil_disewa_travello * lama_penyewaan
elif(verivikasi_ulang == 5):
    total_pembayaran = isuzu_elf_harian * total_mobil_disewa_elf * lama_penyewaan
else :
    total_pembayaran = medium_bus_harian * total_mobil_disewa_medium_bus * lama_penyewaan

print('NOTA PENYEWAAN ')
print('nama penyewa {} '.format(nama_penyewa))
print('nomor ktp penyewa {}'.format (nomor_ktp))
print('nomor sim penyewa {}'.format (nomor_sim))
print('jenis mobil yang di sewa adalah : {} '. format(jenis_mobil))
data =int(input('apakah data yang terambil sudah benar jika benar ketik benar ketik 1 jika salah ketik 2: \n'))
 
if (data == 1 ): 
    print('data yang di terima sudah terverivikasi')
    print('total pembayaran anda: Rp {},00 '.format(total_pembayaran))
    print ( 'dari jumlah RP{},00 silahkan lakukan pembayaran ke nomor rekening (BCA) 11709496  '.format(total_pembayaran))
    alamat = input('alamat mobil akan di antar ke lokasi bersama supir : ')
    print('mobil yang anda ingin pesan segera berangkat ke {} lokasi anda '.format(alamat))
    print('terimakasih sudah menggunakan rental purwadhika semoga perjalanan anda menyenangkan ')
else  :
        print('gagal tidak terverifikasi')
         



        
         
        