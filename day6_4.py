def score(dice):
    score = 0

    # Count occurrences of each number
    counts = [0] * 7  # Index 0 is not used

    for num in dice:
        counts[num] += 1

    # Calculate score based on counts
    for num in range(1, 7):
        if counts[num] >= 3:
            if num == 1:
                score += 1000
            else:
                score += num * 100

            counts[num] -= 3

    # Add remaining ones and fives
    score += counts[1] * 100
    score += counts[5] * 50

    return score


# Test cases
print(score([5, 1, 3, 4, 1]))  # Output: 250
print(score([1, 1, 1, 3, 1]))  # Output: 1100
print(score([2, 4, 4, 5, 4]))  # Output: 450
