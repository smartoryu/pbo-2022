A = [[1, 2],
    [4, 3]]

B = [[6, 8],
    [4, 2]]

hasil = [[0, 0],
        [0, 0]]

for i in range(len(A)):
    for j in range(len(B)):
        hasil[i][j] = A[i][j] + B[i][j]

for r in hasil:
    print(r)
