# Selection_sort_01

def selection_sort(data_list):
    length = len(data_list)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if data_list[j] < data_list[min_index]:
                min_index = j
        
        if min_index !=i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp


if __name__ == '__main__':
    data_list = [100, 400, 300, 500, 200]
    selection_sort(data_list)
    print('Sorted list: ',data_list)
 

#  Secection_sort_02

def selection_sort(data_list):
    length = len(data_list)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if data_list[j] < data_list[min_index]:
                min_index = j
        
        if min_index != i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

if __name__ == '__main__':
    data_list = [2, 5, 1, 7, 4, 9]
    selection_sort(data_list)
    print('Sorted List: ', data_list)

# Selection_sort_03

def selection_sort(data_list):
    length = len(data_list)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1,length):
            if data_list[j] < data_list[min_index]:
                min_index = j
            
        if min_index != i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp







if __name__ == '__main__':
    data_list = [10,15,20,30,25]
    selection_sort(data_list)
    print('Sorted list:',data_list)    
