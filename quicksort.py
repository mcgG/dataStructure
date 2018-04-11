from random import randrange

def quicksort(arr, start, end):
    if start < end:
        pos = partition(arr, start, end)
        quicksort(arr, start, pos-1)
        quicksort(arr, pos+1, end)

def partition(arr, start, end):
    randPos = randrange(start, end+1)
    pivot = arr[randPos]
    arr[start], arr[randPos] = arr[randPos], arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    arr[start] = pivot
    return start

# def partition(arr, start, end):
#     pivot = arr[start]
#     while start < end:
#         while start < end and arr[end] >= pivot:
#             end -= 1
#         arr[start] = arr[end]
#         while start < end and arr[start] <= pivot:
#             start += 1
#         arr[end] = arr[start]
#     arr[start] = pivot
#     return start

arr = [2,3,4,1,5,6]
quicksort(arr, 0, len(arr)-1)
print(arr)
