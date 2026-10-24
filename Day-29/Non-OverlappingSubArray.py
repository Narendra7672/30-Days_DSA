#Maximum Number of Non-Overlapping Substrings:

def maxNumOfSubstrings(s):
    first = {}
    last = {}
    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i
    intervals = []
    for c in set(s):
        l = first[c]
        r = last[c]
        i = l
        valid = True
        while i <= r:
            if first[s[i]] < l:
                valid = False
                break
            r = max(r, last[s[i]])
            i += 1
        if valid:
            intervals.append((l, r))
    intervals.sort(key=lambda x: x[1])
    ans = []
    prev_end = -1
    for l, r in intervals:
        if l > prev_end:
            ans.append(s[l:r + 1])
            prev_end = r
    return ans
s = "adefaddaccc"
print(maxNumOfSubstrings(s))

