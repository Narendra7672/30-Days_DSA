# Find the Median of Two Sorted Arrays:

def MedianOfTwoArray(num1,num2):
    median = num1 + num2
    median.sort()
    n = len(median)
    mid = n // 2
    if n % 2 == 1:
        return float(median[mid])
    else:
        return (median[mid - 1] + median[mid]) / 2.0

num1 = [1,3]
num2 = [2]
res=MedianOfTwoArray(num1,num2) 
print(res) 
num1 = [1, 2]
num2 = [3, 4]  
res=MedianOfTwoArray(num1,num2) 
print(res)