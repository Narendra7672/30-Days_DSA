def count_frequency(elements):  
    frequency_map = {}       
    for item in elements:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
            
    return frequency_map
   
my_list = [10, 20, 10, 5, 20, 10, 5, 99]  
print(f"Original List: {my_list}")
result = count_frequency(my_list)
for element, count in result.items():
    print(f" {element}:  {count} ")
