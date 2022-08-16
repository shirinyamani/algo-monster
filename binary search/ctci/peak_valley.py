from os import TMP_MAX
from tempfile import tempdir


def sortValleyPeak(arr):
    for i in range(1, len(arr)):
        biggest = max_index(arr, i-1, i, i+1)
        if biggest != i:
            swap(arr, i, biggest)
            i += 2
        


    def max_index(arr, left, mid, right):   #max(arr[left], max(arr[mid], arr[right]))
        if left == right:   
            return left
        elif left == mid:
            return mid

        elif right == mid:
            return mid

        elif left > mid and right < mid:
            swap(arr, left, mid)

        elif left < mid and right > mid:
            swap(arr, right, mid)
        

    def swap(arr, left, right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        