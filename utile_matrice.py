# Realizat de/Produced by Casiu George Valentin
def citire(tip):
    m=int(input("m="))
    n=int(input("n="))
    M=[list([0 for j in range(n)]) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if tip=="int":
                M[i][j]=int(input("M["+str(i)+","+str(j)+"]="))
            elif tip=="float":
                M[i][j]=float(input("M["+str(i)+","+str(j)+"]="))
            else:
                M[i][j]=input("M["+str(i)+","+str(j)+"]=")
    return(m,n,M)

def citire_f(fisier,tip):
    with open(fisier, "r") as f:
        m=int(f.readline())
        n=int(f.readline())
        M=[list([0 for j in range(n)]) for i in range(m)]
        for i in range(m):
            linie=f.readline() #sau se poate folosi/or you can use directli: linie=f.readline().replace("\n"," ").split()
            linie=linie.replace("\n"," ")
            linie=linie.split()
            if tip=="int":
                 M[i]=[int(el) for el in linie]
            elif tip=="float":
                M[i]=[float(el) for el in linie]
            else:
                M[i]=linie
    return(n,m,M)

def afisare(M):
    nr=0
    nr=max([len(str((el))) for i in M for el in i if nr<len(str((el)))])#gaseste lungimea maxima a elementelor
    for i in M:
        for el in i:
            print(el,end=" "*(nr+1-len(str(el))))#afiseaza elementul cu spatii dupa el
        print()

def scrie_f(fisier,M):
    with open(fisier,"w") as f:
        f.write(str(len(M))+"\n")
        f.write(str(len(M[0]))+"\n")
        for linie in M:
            for el in linie:
                f.write(str(el)+" ")
            print("\n")
