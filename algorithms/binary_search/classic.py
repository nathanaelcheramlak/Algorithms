def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print('left', left)
    print('right', right)
    return left - 1

def left_binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    print('left', left)
    print('right', right)
    return left - 1


nums = [1, 1, 2, 3, 3, 4, 5,6, 6,6, 9, 10, 12, 13, 14]
print(binary_search(nums, 6))

print(', '.join(str(x) for x in nums))