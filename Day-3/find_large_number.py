def large_number(num):
    temp = num[0]
    for i in range(len(num)):
        if num[i] > temp:
            temp = num[i]
    return temp
num = [10, 25, 7, 45, 18] 
n = large_number(num) 
print(n)      



