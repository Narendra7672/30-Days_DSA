# Minimum Remove to Make Valid Parentheses:

def RemoveParentheses(s):
    remove = set()
    stack =[]
    for i,c in enumerate(s):
        if c not in '()':
            continue
        elif c == '(':
            stack.append(i)
        else:
            if not stack:
                remove.add(i)
            else:
                stack.pop()
    remove =  remove.union(set(stack))
    result = []
    for i,c in enumerate(s):
        if i not in remove:
            result.append(c)
    return ''.join(result)
s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
res = RemoveParentheses(s)
print(res)

