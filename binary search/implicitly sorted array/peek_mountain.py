def peakIndexInMountainArray(self, arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mi = (lo + hi) / 2
        if arr[mi] < arr[mi + 1]:
            lo = mi + 1
        else:
            hi = mi
    return lo
