def max_sequence(arr):
    max_so_far = float('-inf')
    max_ending = 0
    for i in range(len(arr)):  # Added parentheses around len(arr)
        max_ending = max_ending + arr[i]
        if max_so_far < max_ending:
            max_so_far = max_ending
        if max_ending < 0:
            max_ending = 0
    return max_so_far

# Test case
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sequence(arr))  # Output: 7
