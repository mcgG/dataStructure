def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    rs = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            rs.append(a[i])
            i += 1
        else:
            rs.append(b[j])
            j += 1
    rs += a[i:] if i < len(a) else b[j:]
    return rs

a = [1,2,4,5,3,2,1,3]
print(mergesort(a))
