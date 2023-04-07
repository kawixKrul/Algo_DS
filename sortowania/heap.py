left = lambda x: 2 * x + 1
right = lambda x: 2 * x + 2
parent = lambda x: (x - 1) // 2


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
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    build_heap(A, n)
    for i in range(n - 1, 0, -1):
        print(A)
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

tab = [1,4,5,3,9,4,7,2,6,8,3,2,5,7]
heap_sort(tab)
print(tab)
