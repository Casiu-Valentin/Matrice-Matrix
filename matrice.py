# Realizat de/Produced by Casiu George Valentin
import utile_matrice as um

n,m,M=um.citire_f("matrice.in","int")
print(M)
print("Matricea initiala este:")
um.afisare(M)

"""
#interschimbarea liniilor/intrechange of lines
x=int(input("Introduceti x="))
y=int(input("Introduceti y="))
for j in range(n):
    M[x-1][j],M[y-1][j]=M[y-1][j],M[x-1][j]
um.afisare(M)
um.scrie_f("matrice.out",M)
"""

"""
#interschimbarea coloanelor/interchange of columns
x=int(input("Introduceti x="))
y=int(input("Introduceti y="))
for i in range(m):
    M[i][x-1],M[i][y-1]=M[i][y-1],M[i][x-1]
um.afisare(M)
um.scrie_f("matrice.out",M)
"""

"""
#citirea unei matrice patratice in spirala/reading a quadratic matrix in a spiral
print("Citirea in spirala este:")
for k in range(n//2+1):
    for i in range(k,n-k) : print(M[k][i],end=" ")
    for i in range(k+1,n-k) : print(M[i][n-k-1],end=" ")
    for i in range(n-k-2,k-1,-1) : print(M[n-k-1][i],end=" ")
    for i in range(n-k-2,k,-1) : print(M[i][k],end=" ")
"""
