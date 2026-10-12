# Partition Labels:

def PartitionLabels(s):
    count = {}
    for i in range(len(s)):
        count[s[i]] = i
    curlen = 0
    end = 0
    res = []
    for i in range(len(s)):
        end = max(end,count[s[i]])
        curlen += 1
        if i == end:
            res.append(curlen)
            curlen = 0
    return res
s = "ababcbacadefegdehijhklij"
result = PartitionLabels(s)
print(result)
