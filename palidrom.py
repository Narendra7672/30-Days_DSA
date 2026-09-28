name = 'makam'
lst = list(name)
left = 0
right = len(lst)
while left < right:
    lst[left],lst[right] = lst[right],lst[left]
    left += 1
    right -= 1
lst1 ="".join(lst)

print(lst1)  


def is_palindrome(text):
    
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    
    
    left = 0
    right = len(cleaned) - 1
    
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False  
        left += 1
        right -= 1
        
    return True
print(is_palindrome("Racecar"))  
print(is_palindrome("Hello"))    
print(is_palindrome("A man, a plan, a canal: Panama"))  

    