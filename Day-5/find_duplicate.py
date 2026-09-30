# Find Duplicate Elements:
'''
def find_duplicates(num):
    seen = set()
    duplicates = set()
    for num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
    return duplicates
num = [1,2,3,4,5,6,7,1,2,3,4]
res = find_duplicates(num)
print(res)   '''

def find_duplicates(nums):
    seen = []
    duplicates = []
    for num in nums:
        if num not in seen:
            seen.append(num)
        else:
            duplicates.append(num)
    return duplicates
nums = [1,2,3,4,5,6,7,1,2,3,4]
res = find_duplicates(nums)
print(res) 
# its return set :
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates
nums = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
print(find_duplicates(nums))
            
