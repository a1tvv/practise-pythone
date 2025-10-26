num_list = [10, 15, 20, 25, 30]

def objects(num_list):
    print(num_list)
    
    
def summ(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
        
print('Summ number of list: ', summ(num_list))