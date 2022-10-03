A = [[2, 3],
    [6, 9]]

B = [[3, 1],
    [7, 5]]

hasil = [[0, 0],
        [0, 0]]

for i in range(len(A)):
    for j in range(len(B)):
        hasil[i][j] = A[i][j] - B[i][j]

for r in hasil:
    print(r)
