def fibonacci_series():
    print("--- Program Deret Fibonacci ---")
    try:
        n = int(input("Masukkan jumlah suku (n): "))
        
        if n <= 0:
            print("Masukkan angka positif lebih dari 0.")
            return

        a, b = 0, 1
        print(f"Deret fibonacci hingga suku ke-{n}:")
        
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
        
    except ValueError:
        print("Error: Harap masukkan angka bulat!")

if __name__ == "__main__":
    fibonacci_series()