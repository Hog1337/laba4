from random import choice


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        random_num = choice(a)
        smaller, equal, bigger = [], [], []
        for i in a:
            if i < random_num:
                smaller.append(i)
            elif i > random_num:
                bigger.append(i)
            else:
                equal.append(i)
        return quick_sort(smaller) + equal + quick_sort(bigger)


def hairbrush(a):
    s = len(a)
    while s > 1 or sor:
        if s > 1:
            s = int(s // 2)
        j = 0
        sor = False
        while j + s < len(a):
            if a[j] > a[j + s]:
                a[j], a[j + s] = a[j + s], a[j]
                sor = True
            j += s
    return a


def bucket_sort(a):
    maxi, leni = max(a), len(a),
    size = maxi / leni
    bucket = [[] for _ in range(leni)]
    for i in range(leni):
        ind = int(a[i] / size)
        if ind != leni:
            bucket[ind].append(a[i])
        else:
            bucket[leni - 1].append(a[i])
    for i in range(leni):
        bucket[i] = sorted(bucket[i])
    fin = []
    for i in range(leni):
        fin = fin + bucket[i]
    return fin

def heapi(A, size, r_ind):
    maxi = r_ind
    left = (2 * r_ind) + 1
    right = (2 * r_ind) + 2
    if left < size and A[left] > A[maxi]:
        maxi = left

    if right < size and A[right] > A[maxi]:
        maxi = right

    if maxi != r_ind:
        A[r_ind], A[maxi] = A[maxi], A[r_ind]
        heapi(A, size, maxi)


def heap_sort(A):
    n = len(A)
    for i in range(n, -1, -1):
        heapi(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapi(A, i, 0)
