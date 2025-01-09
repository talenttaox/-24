quantity = int(input())  
lst = [int(i) for i in input().split()]  
num = int(input())  
prefix_sum = [0] * (len(lst) + 1)  
for i in range(1, len(prefix_sum)):  
    prefix_sum[i] = prefix_sum[i - 1] + lst[i - 1]   
sorted_lst = sorted(lst)  
sorted_prefix_sum = [0] * (len(sorted_lst) + 1)  
for i in range(1, len(sorted_prefix_sum)):  
    sorted_prefix_sum[i] = sorted_prefix_sum[i - 1] + sorted_lst[i - 1]   
for i in range(num):  
    value = 0  
    question = [int(j) for j in input().split()]  
    if question[0] == 1:    
        left, right = question[1], question[2]  
        value = prefix_sum[right] - prefix_sum[left-1]  
    else:   
        left, right = question[1], question[2]  
        value = sorted_prefix_sum[right] - sorted_prefix_sum[left-1]  
    print(value)