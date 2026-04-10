def input_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        row = list(map(int, input(f"Masukkan baris {i+1}: ").split()))
        matriks.append(row)
    return matriks

def tampilkan(m):
    for row in m:
        print(row)

def penjumlahan(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        hasil.append(row)
    return hasil

def pengurangan(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        hasil.append(row)
    return hasil

def perkalian(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        hasil.append(row)
    return hasil

while True:
    print("\n=== MENU OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Exit")

    pilihan = int(input("Pilih menu (1-4): "))

    if pilihan == 4:
        print("Program selesai.")
        break

    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    print("Matriks A:")
    A = input_matriks(baris, kolom)
    print("Matriks B:")
    B = input_matriks(baris, kolom)

    if pilihan == 1:
        hasil = penjumlahan(A, B)
        print("Hasil Penjumlahan:")
        tampilkan(hasil)

    elif pilihan == 2:
        hasil = pengurangan(A, B)
        print("Hasil Pengurangan:")
        tampilkan(hasil)

    elif pilihan == 3:
        hasil = perkalian(A, B)
        print("Hasil Perkalian:")
        tampilkan(hasil)

    else:
        print("Pilihan tidak valid!")