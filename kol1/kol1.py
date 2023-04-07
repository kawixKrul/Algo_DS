from kol1testy import runtests

"""
algorytm bierze pierwszy przedzial z T i sortuje go za pomoca quicksorta zeby znalezc k-ty alement ktory doda do sumy
Znajduje go poprzez wykonienie petli w ktorej w kazdej iteracji:
 kazdej iteracji petli przesuwa posortowany przedzial, usuwajac element ktory do niego juz nie nalezy i 
wstawiajac kolejny element do posrtowanego przedzialu zachowujac jego porzadek, 
zlozonosc: O(np + p*log(p))

"""

def ksum(T, k, p):

    def partition(A,p,r):
        pivot = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] > pivot:
                i += 1
                A[i],A[j] = A[j], A[i]
        A[r],A[i+1] = A[i+1], A[r]
        return i+1

    def quicksort(A,p,r):
        if p < r:
            q = partition(A,p,r)
            quicksort(A,p,q-1)
            quicksort(A,q+1,r)


    def insert(A,x):
        try:
            i = 0
            while A[i] > x:
                i += 1
            A.insert(i,x)
        except: A.append(x)

    n = len(T)
    i = 0
    sum = 0
    slice = T[i:i+p]
    quicksort(slice,0,len(slice)-1)
    while i < n-p:
        sum += slice[k-1]
        slice.remove(T[i])
        insert(slice,T[i+p])
        i += 1
    sum += slice[k-1]
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)
