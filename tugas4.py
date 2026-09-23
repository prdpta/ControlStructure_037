def cetak_ganjil():
    print("--- Program Angka Ganjil ---")
    try:
        n = int(input("Masukkan batas angka (n): "))
        
        print(f"Angka ganjil dari 1 sampai {n}:")
        # Menggunakan range dengan langkah (step) 2, mulai dari 1
        for i in range(1, n + 1, 2):
            print(i, end=" ")
        print()
        
    except ValueError:
        print("Error: Harap masukkan angka bulat!")

if __name__ == "__main__":
    cetak_ganjil()