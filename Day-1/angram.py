'''s = "anagram"
t = "nagaram"

Output: True'''

def anagram(s,t):
    n = sorted(s)
    m = sorted(t)
    if n == m:
        return True
    else:
        return False
s = "anagram"
t = "nagaram"
num = anagram(s,t)
print(num)    

# ****************************************************************************
def anagram_1(s,t):
    lst = list(s)
    lst2 = list(t)
    temp = 0

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    for i in range(len(lst2)):
        for j in range(i+1,len(lst2)):
            if lst2[i] > lst2[j]:
                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp
    if lst == lst2:
            return True
    else:
        return False            
    return "".join(lst), "".join(lst2)
s = "anagram"
t = "nagaram"
num = anagram(s,t)
print(num)

#*********************************************************************************

def anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


s = "anagram"
t = "nagaram"

print(anagram(s, t))
    
           


