def insertion(A):
    l = len(A)
    for i in range(l):
        for j in range(i, 0, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]


def seleection(A):
    l = len(A)
    for i in range(l):
        min_idx = i
        for j in range(i+1, l):
            if A[j] < A[min_idx]:
                min_idx = j
        A[min_idx], A[i] = A[i], A[min_idx]


tab = [1,4,5,3,9,4,7,2,6,8,3,2,5,7]
tab2 = [x for x in tab]
insertion(tab)
seleection(tab2)
print(tab)
print(tab2)
