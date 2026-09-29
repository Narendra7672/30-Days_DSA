# Check if Two Arrays Have the Same Elements:
def same_array(num1,num2):
    n = sorted(num1)
    n1 = sorted(num2)
    for i in range(len(n)):
        for j in range(len(n1)):
            if n == n1:
                return True
            else:
                return False
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [2,3,4,1,7,9,10,5,6,8]
res = same_array(num1,num2)
print(res) 
# second approch
def same_array(num1, num2):
    if len(num1) != len(num2):
        return False
    freq = {}
    for num in num1:
        freq[num] = freq.get(num, 0) + 1
    for num in num2:
        if num not in freq:
            return False
        freq[num] -= 1
        if freq[num] < 0:
            return False
    return True  
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [2,3,4,1,7,9,10,5,6,8]
res = same_array(num1,num2)
print(res)          