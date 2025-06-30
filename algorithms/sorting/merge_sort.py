def merge_sort(arr):
    N = len(arr)
    if N <= 1:
        return arr

    left = merge_sort(arr[:N // 2])
    right = merge_sort(arr[N // 2:])

    return merge_array(left, right)


def merge_array(left, right):
    left_idx = right_idx = 0
    merged = list()
    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and (right_idx >= len(right) or left[left_idx] < right[right_idx]):
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    return merged

# Test cases
if __name__ == "__main__":
    test_arrays = [
        [8, 7, 6, 5, 4, 3, 2, 1],
        [],
        [1],
        [5, 2, 9, 1, 5, 6],
        [3, 3, 3],
    ]
    for arr in test_arrays:
        print(f"Original: {arr} -> Sorted: {merge_sort(arr)}")