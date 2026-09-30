# Find the Intersection of Two Arrays:

def intersections(num1,num2):
    set1 = set(num1)
    result = []
    for num in num2:
        if num in  set1:
            result.append(num)
    return result             
num1 = [1,2,3,4]
num2 = [4,3,5,6]
res = intersections(num1,num2)
print(res)            
