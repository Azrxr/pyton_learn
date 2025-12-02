import hello

persegi_panjang1 = hello.mencari_luas_persegi_panjang(5,10)
print(persegi_panjang1)
print(hello.nama) #akses variable tambahan

#import spesifik
from hello import mencari_luas_persegi_panjang, nama
#tidak perlu menyebutkan hello pada setiap kode yang berhasil diimpor dari modul hello.

persegi_panjang2 = mencari_luas_persegi_panjang(20, 30)
print(persegi_panjang2)

print(nama)