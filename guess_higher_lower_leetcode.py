def guessNumber(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            left = mid + 1
        else:
            right = mid - 1
