def buat_matriks(data):
    return data

def tampilkan_matriks(m):
    for baris in m:
        print(baris)

def penjumlahan_matriks(m1, m2):
    hasil = []
    for i in range(len(m1)):
        baris = []
        for j in range(len(m1[0])):
            baris.append(m1[i][j] + m2[i][j])
        hasil.append(baris)
    return hasil

def pengurangan_matriks(m1, m2):
    hasil = []

    for i in range(len(m1)):
        baris = []
        for j in range(len(m1[0])):
            baris.append(m1[i][j] - m2[i][j])
        hasil.append(baris)
    return hasil

def transpose_matriks(m):
    hasil = []
    for j in range(len(m[0])):
        baris = []
        for i in range(len(m)):
            baris.append(m[i][j])
        hasil.append(baris)
    return hasil

def perkalian_matriks(m1, m2):
    if len(m1[0]) != len(m2):
        return "Perkalian tidak dapat dilakukan"
    hasil = []
    for i in range(len(m1)):
        baris = []
        for j in range(len(m2[0])):
            total = 0
            for k in range(len(m2)):
                total += m1[i][k] * m2[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil