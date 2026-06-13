import radita068

A = radita068.buat_matriks([[25, 2, 4], [5, 26, 9], [3, 7, 13]])
B = radita068.buat_matriks([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

print("Matriks A")
radita068.tampilkan_matriks(A)

print("\nMatriks B")
radita068.tampilkan_matriks(B)

hasil = radita068.penjumlahan_matriks(A, B)
print("\nHasil Penjumlahan")
radita068.tampilkan_matriks(hasil)

hasil = radita068.pengurangan_matriks(A, B)
print("\nHasil Pengurangan")
radita068.tampilkan_matriks(hasil)

AT = radita068.transpose_matriks(A)
print("\nTranspose Matriks A")
radita068.tampilkan_matriks(AT)

hasil = radita068.perkalian_matriks(A, B)
print("\nHasil Perkalian")
radita068.tampilkan_matriks(hasil)