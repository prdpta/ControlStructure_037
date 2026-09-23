def cetak_desain_pola():
    print("--- Program Desain Pola Angka ---")
    try:
        n = int(input("Masukkan nilai n (misal 5): "))
        
        print("\nHasil Desain:")
        # Perulangan baris dari 1 sampai n
        for i in range(1, n + 1):
            # Perulangan kolom untuk mencetak angka sebanyak nilai baris (i)
            for j in range(i):
                print(i, end=" ")
            print() # Pindah ke baris baru setiap satu baris selesai
            
    except ValueError:
        print("Error: Harap masukkan angka bulat!")

if __name__ == "__main__":
    cetak_desain_pola()