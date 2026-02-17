word = input().strip()
n = len(word)

if n % 2 == 1:
    mid = n // 2
    for offset in range(mid + 1):
        left = mid - offset
        right = mid + offset
        if left == right:
            print(' ' * left + word[left])
        else:
            print(' ' * left + word[left] + ' ' * (right - left - 1) + word[right])
else:
    left_center = n // 2 - 1
    right_center = n // 2
    for offset in range(left_center + 1):
        l = left_center - offset
        r = right_center + offset
        if l == left_center and r == right_center:
            print(' ' * l + word[l] + word[r])
        else:
            print(' ' * l + word[l] + ' ' * (r - l - 1) + word[r])