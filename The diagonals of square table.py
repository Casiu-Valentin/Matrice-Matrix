# Realizat de/Produced by Casiu George Valentin
"""
A table with n lines and columns, integer is read.
Such a table, in witch the number of lines is equal with number of columns is called the square table.
Is required:
a1) the sum of elements located on the main diagonal
a2) the sum of elements located above the main diagonal
a3) the sum of element located below the main diagonal
b1) the sum of elements located on the secondary diagonal
b2) the sum of elements located above the secondary diagonal
b3) the sum of element located below the secondary diagonal
/Se citeşte un tablou cu n linii şi n coloane, numere întregi.
Un astfel de tablou, în care numǎrul liniilor coincide cu numǎrul coloanelor, se numeşte tablou pǎtratic.
Se cere:
a1) suma elementelor aflate pe diagonala principalǎ;
a2) suma elementelor aflate deasupra diagonalei principale;
a3) suma elementelor aflate sub diagonala principalǎ.
b1) suma elementelor aflate pe diagonala secundarǎ;
b2) suma elementelor aflate deasupra diagonalei secundare;
b3) suma elementelor aflate sub diagonala secundarǎ.
"""

def citirenat(text):# natural number reading/citire numar natural
    n=''
    while not(n.isdecimal()): # if n is not decimal/daca n nu e zecimal
        n = input(text)
        n = n.strip(' +')# remove spaces and '+' from the beginning and end of number/elimina spatiile libere si '+' de la inceputul si sfarsitul numarului
    return int(n)

def citiremat(tip):
    n=m=citirenat("Enter the number of lines and columns/Introduceti numarul de linii si coloane:")
    M=[list([0 for j in range(m)]) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if tip=="int":
                M[i][j]=int(input("M["+str(i)+","+str(j)+"]="))
            elif tip=="float":
                M[i][j]=float(input("M["+str(i)+","+str(j)+"]="))
            else:
                M[i][j]=input("M["+str(i)+","+str(j)+"]=")
    return(n,M)

# Programul principal/The main program
n,M=citiremat("int")

s=0
for i in range(n):
    s+=M[i][i]
print("a1) The sum is/Suma este:",s)

s=0

for i in range(n):
    for j in range(i+1,n):
        s+=M[i][j]
print("a2) The sum is/Suma este:",s)

s=0
for i in range(n):
    for j in range(i):
        s+=M[i][j]
print("a3) The sum is/Suma este:",s)

s=0
for i in range(n):
    s+=M[n-1-i][i]
print("b1) The sum is/Suma este:",s)

s=0
for i in range(n-1):
    for j in range(n-1-i):
        s+=M[i][j]
print("a3) The sum is/Suma este:",s)

s=0
for i in range(1,n):
    for j in range(n-i,n):
        s+=M[i][j]
print("a3) The sum is/Suma este:",s)
