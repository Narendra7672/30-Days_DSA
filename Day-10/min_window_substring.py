# Minimum Window Substring:
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    window = {}
    left = 0
    formed = 0
    required = len(need)
    min_len = float("inf")
    min_left = 0
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        if char in need and window[char] == need[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1
    if min_len == float("inf"):
        return ""
    return s[min_left:min_left + min_len]
s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)