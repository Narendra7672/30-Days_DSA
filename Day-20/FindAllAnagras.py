from collections import Counter
def findAnagrams(s, p):
    ns, np = len(s), len(p)
    if ns < np:
        return []
    p_count = Counter(p)
    s_count = Counter()
    result = []
    for i in range(ns):
        s_count[s[i]] += 1
        if i >= np:
            if s_count[s[i - np]] == 1:
                del s_count[s[i - np]]
            else:
                s_count[s[i - np]] -= 1

        if s_count == p_count:
            result.append(i - np + 1)
    return result
print(findAnagrams("cbaebabacd", "abc"))