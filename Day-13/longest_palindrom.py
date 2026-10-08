# Longest Palindromic Substring:
def longest_palindromic_substring(s: str) -> str:
    if not s or len(s) <= 1:
        return s
    start, max_length = 0, 1
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        current_len = max(len1, len2)   
        if current_len > max_length:
            max_length = current_len
            start = i - (current_len - 1) // 2       
    return s[start : start + max_length]
if __name__ == "__main__":
    test_1 = "babad"
    test_2 = "cbbd"
    test_3 = "racecar"
    print(f"Input: '{test_1}' -> Output: '{longest_palindromic_substring(test_1)}'")
    print(f"Input: '{test_2}' -> Output: '{longest_palindromic_substring(test_2)}'")
    print(f"Input: '{test_3}' -> Output: '{longest_palindromic_substring(test_3)}'")
