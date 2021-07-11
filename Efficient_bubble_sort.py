# Eifficient Bubble sort

# def bubble_sort(list_item):
#     list_lenght = len(list_item)

#     for i in range(list_lenght):
#         swap = False

#         for j in range(list_lenght-i-1):
#             if list_item[j] > list_item[j+1]:

#                 result = list_item[j]
#                 list_item[j] = list_item[j+1]
#                 list_item[j+1] = result
#                 swap = True
        
#         if swap == False:
#             break

# if __name__ == "__main__":
#     list_item = [12, 45, 2, 36, 54, 30, 50]
#     bubble_sort(list_item)
#     print("Bubble sorted: ", list_item)




def bubble_sort(datalist):
    n = len(datalist)
    for i in range(n-1):
        swapped = False
        
        for j in range(n-i-1):
            
            if  datalist[j] > datalist[j+1]:
                temp = datalist[j]
                datalist[j] = datalist[j+1]
                datalist[j+1] = temp
                
                swapped = True
        
        if not swapped:
            break

if __name__ == '__main__':
    datalist = [3,4,5,9,7]
    bubble_sort(datalist)
    print(datalist)