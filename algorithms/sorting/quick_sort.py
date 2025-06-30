def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def better_quick_sort(arr, left, right):
    if right - left <= 1 or (right * left) < 0:
        return
    
    pivot = arr[-1]
    print(arr[left: right + 1], pivot)
    start = left
    end = right
    right -= 1

    while right >= left:
        if arr[left] > pivot:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    
    arr[left], arr[end] = arr[end], arr[left]
    print(left, end, arr[start: end + 1], pivot)
    better_quick_sort(arr, start, left - 1)
    better_quick_sort(arr, left + 1, end)

arr = [3, 1, 6, 2, 5, 3, 0, -2, 1, -6]
print(quick_sort(arr))
print(arr)