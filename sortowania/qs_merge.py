def partition(A,p,r):
    pivot = A[r-1]
    i = p-1
    for j in range(p, r-1):
        if A[j] < pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r-1] = A[r-1], A[i+1]
    return i+1


def qs(A,p,r):
    if p < r:
        q = partition(A,p,r)
        qs(A,p,q-1)
        qs(A,q+1,r)


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge_s(A):
    if len(A) > 1:
        mid = len(A)//2
        l = A[:mid]
        r = A[mid:]

        merge_s(l)
        merge_s(r)
        i,j,k = 0,0,0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                A[k] = l[i]
                i += 1
            else:
                A[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            A[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            A[k] = r[j]
            j += 1
            k += 1


tab = [1,4,5,3,9,4,7,2,6,8,3,2,5,7]
tab2 = [x for x in tab]
tab3 = [x for x in tab]
qs(tab, 0, len(tab))
mergeSort(tab2)
merge_s(tab3)


print(tab3)
print(tab)
print(tab2)
