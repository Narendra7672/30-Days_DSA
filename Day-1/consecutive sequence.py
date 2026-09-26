num = [100,1,200,4,2,3]
new_set = set(num)
#print(new_set)
max_len = 0
best_start = 0
for n in new_set:
    if(n-1) not in new_set:
        current_num = n
        current_len = 1

        while (current_num + 1) in new_set:
            current_num += 1
            current_len += 1
        if current_len > max_len:
            max_len = current_len
            best_start = n
longest_sequence = list(range(best_start,best_start + max_len))
print(len(longest_sequence))                