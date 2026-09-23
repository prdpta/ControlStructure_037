def evaluasi_performa():
    print("--- Program Evaluasi Performa Mahasiswa ---")
    try:
        persentase = float(input("Masukkan persentase nilai (%): "))
        
        if persentase >= 90:
            print("Predikat: Excellent performance")
        elif persentase >= 80:
            print("Predikat: Very Good performance")
        elif persentase >= 70:
            print("Predikat: Good performance")
        elif persentase >= 60:
            print("Predikat: average performance")
        else:
            print("Predikat: Perlu peningkatan (Di bawah 60)")
            
    except ValueError:
        print("Error: Harap masukkan angka yang valid!")

if __name__ == "__main__":
    evaluasi_performa()