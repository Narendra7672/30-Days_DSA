'''Input:
s = "abcabcbb"

Output: 3'''

def substring(s):
    lst = list(s)
    temp = []
    for num in lst:
        if num not in temp:
            temp.append(num)
    return "".join(temp) 
s =  "abcabcbb"
n = substring(s)     
print(len(n))


def substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        current_len = right - left + 1

        if current_len > max_len:
            max_len = current_len

    return max_len


s = "abcabcbb"

print(substring(s))