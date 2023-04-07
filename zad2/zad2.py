from zad2testy import runtests
"""
Michal Kawa
zlozonosz O(nlogn)
Algorytm przy uzyciy alogrytmu sortowania przez kopcowanie wybiera najwiekszy element z nieposortowanej czesci tablicy
S i okresla jaka bedzie mial wartosc w dniu w ktorym snieg zostanie z niego zebrany. Sortowanie ma na celu znalezienie 
tych pol ktore najkorzytsniej bedzie nam zebrac z wawazu zeby zdobyc jak najweiecej sniegu. Dzien zebrania sniegu z 
 konkretnegoo pola nie ma znaczenia bo dodanie i odejmowanie jest przemeinne.
"""
def snow( S ):
    left = lambda x: 2*x + 1
    right = lambda x: 2*x + 2
    parent = lambda x: (x-1)//2

    def heapify(A, n, i):
        max_id = i
        l = left(i)
        r = right(i)
        if l < n and A[max_id] < A[l]:
            max_id = l
        if r < n and A[max_id] < A[r]:
            max_id = r
        if max_id != i:
            A[i], A[max_id] = A[max_id], A[i]
            heapify(A, n, max_id)

    def build_heap(A, n):
        for i in range(parent(n-1), -1, -1):
            heapify(A, n, i)

    def heap_sort(A):
        n = len(A)
        build_heap(A, n)
        j, zebrane = 0, 0
        for i in range(n - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            if A[i] - j > 0:
                zebrane += A[i] - j
                j += 1
            else:
                return zebrane
            heapify(A, i, 0)

    return heap_sort(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True)
