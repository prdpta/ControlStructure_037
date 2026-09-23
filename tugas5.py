def cetak_desain_pola():
    print("--- Program Desain Pola Angka ---")
    try:
        n = int(input("Masukkan nilai n (misal 5): "))
        
        print("\nHasil Desain:")
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end=" ")
            print()
            
    except ValueError:
        print("Error: Harap masukkan angka bulat!")

if __name__ == "__main__":
    cetak_desain_pola()