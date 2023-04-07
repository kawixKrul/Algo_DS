from zad3testy import runtests

def strong_string(T):
    def quicksort(T,p,r):
        if p >= r:
            return
        q = partition(T,p,r)
        quicksort(T,p,q-1)
        quicksort(T,q+1,r)

    def partition(T,p,r):
        pivot = T[r-1]
        i = p-1
        for j in range(p,r-1):
            if T[j]<pivot:
                i += 1
                T[i],T[j] = T[j],T[i]
        T[i+1],T[r-1] = T[r-1],T[i+1]
        return i+1

    result = 1
    napis = ''
    k = 0
    for x in T:
        k = max(len(x), k)
    buckets = [[] for _ in range(k+1)]
    for x in T:
        buckets[len(x)].append(x)
    for x in buckets:
        if len(x):
            quicksort(x,0,len(x)-1)
    for i in range(k+1):
        curr = 1
        if len(buckets[i]):
            for j in range(len(buckets[i])):
                if buckets[i][j] == buckets[i][j-1]:
                    curr += 1
                    if curr > result:
                        result = curr
                        napis = buckets[i][j-1]
                else:
                    curr = 1
        if len(napis) != 1:
                for j in range(len(buckets[i])-1, -1, -1):
                    rev = napis[::-1]
                    if buckets[i][j] == rev:
                        result += 1
    print(napis)
    return result

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
