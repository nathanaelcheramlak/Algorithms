# N is the bucket size
def bucket_sort(arr, N):
    buckets = [[] for _ in range(N + 1)]
    _min = min(arr)
    _max = max(arr)
    _range = _max - _min

    for num in arr:
        fitted = ((num - _min) / _range)
        buckets[int(fitted * N)].append(num)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    print(sorted_arr)


bucket_sort([1, 4, 2, 61, 21, 90, 32, 12], 5)

