# DIVIDE AND CONQUER

words = ["bats", "battle", "batch"]
def find_prefix(left, right, words):
    if left == right:
        return words[left]

    mid = (left + right + 1) // 2
    left_words = find_prefix(left, mid - 1, words)
    right_words = find_prefix(mid, right, words)

    common = []
    for i in range(min(len(left_words), len(right_words))):
        if left_words[i] == right_words[i]:
            common.append(left_words[i])
        else:
            break
    
    return common
    
print(find_prefix(0, len(words) - 1, words))