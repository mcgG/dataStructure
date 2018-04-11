def heapsort(arr):
    rs = []
    heapify(arr)
    while arr:
        rs.append(arr.pop(0))
        heapify(arr)
    return rs


def heapify(arr):
    for i in range(len(arr)//2, -1, -1):
        sink(arr, i)

def sink(arr, i):
    if 2 * i + 1 < len(arr):
        k = 2*i+2 if 2*i+2 < len(arr) and arr[2*i+2] < arr[2*i+1] else 2*i+1
        if arr[i] > arr[k]:
            arr[i], arr[k] = arr[k], arr[i]
            sink(arr, k)

# def minHeapify(arr, i):
#     minimum = i
#     if 2 * i + 1 < len(arr) and arr[2*i+1] < arr[minimum]:
#         minimum = 2 * i + 1
#     if 2 * i + 2 < len(arr) and arr[2*i+2] < arr[minimum]:
#         minimum = 2 * i + 2
#     if minimum != i:
#         arr[i], arr[minimum] = arr[minimum], arr[i]
#         minHeapify(arr, minimum)


a = [3,2,4,5,1,7]
print (heapsort(a))
