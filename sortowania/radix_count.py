def counting_sort(A, place):
    l = len(A)
    C = [0 for _ in range(len(A))]
    B = [0 for _ in range(10)]
    for i in range(l):
        idx = A[i] // place
        B[idx % 10] += 1
    for i in range(1,len(B)):
        B[i] += B[i-1]
    for i in range(l):
        idx = A[i]//place
        B[idx%10] -= 1
        C[B[idx%10]] = A[i]
    for i in range(l):
        A[i] = C[i]

def radix(A):
    max_el = max(A)
    place = 1
    while max_el//place > 0:
        counting_sort(A,place)
        place *= 10

def bucket_sort(A):
    max_el = max(A)
    buckets = [[] for _ in range(len(str(max_el)))]
    for i in A:
        buckets[len(str(i))-1].append(i)
    for bucket in buckets:
        radix(bucket)
    output = [x for b in buckets for x in b]
    return output

tab = [144,5,6,412,5234,33,9455,4,47,22,623,82,313,223,523,7123]
radix(tab)
print(bucket_sort(tab))

