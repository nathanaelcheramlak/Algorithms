def counting_sort(nums):
    max_element = max(nums)
    arr = [0] * (max_element + 1)

    for num in nums:
        arr[num] += 1

    idx = 0
    for i, val in enumerate(arr):
        if val != 0:
            for _ in range(val):
                nums[idx] = i
                idx += 1
    
    return nums

def negative_counting_sort(nums):
    max_element = max(nums)
    min_element = min(nums)
    arr = [0] * (max_element + min_element + 1)

    for num in nums:
        n = num + abs(min_element)
        arr[n] += 1
    
    idx = 0
    for i, val in enumerate(nums):
        if val != 0:
            for _ in range(val):
                nums[idx] = min_element + i
                idx += 1
    
    return nums

nums = [4,2,1,3,7,1,-7]
print(negative_counting_sort(nums))