def cari_angka_terbesar():
    print("--- Program Mencari Angka Terbesar ---")
    try:
        # Mengubah float() menjadi int() agar hasilnya berupa bilangan bulat
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        c = int(input("Masukkan angka ketiga: "))
        
        # Logika perbandingan
        if (a >= b) and (a >= c):
            terbesar = a
        elif (b >= a) and (b >= c):
            terbesar = b
        else:
            terbesar = c
            
        print(f"Angka terbesar adalah: {terbesar}")
        
    except ValueError:
        print("Error: Harap masukkan angka bulat yang valid!")

if __name__ == "__main__":
    cari_angka_terbesar()