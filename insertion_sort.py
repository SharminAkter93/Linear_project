
# Descending Order form insection_sort


def insection_sort(data):
    n = len(data)

    for i in range(1, n):
        item = data[i]

        j = i-1
        while j>=0 and data[j] < item:
            data[j+1] = data[j]
            j = j - 1

        data[j+1] = item

if __name__ == "__main__":
    data = [20, 55, 70, 44, 10, 25, 5]
    insection_sort(data) 
    print(data)





# Ascending Order form insection_sort


def insection_sort(data_item):
    n = len(data_item)

    for i in range(1, n):
        item = data_item[i]

        j = i-1
        while j>=0 and data_item[j] > item:
            data_item[j+1] = data_item[j]
            j = j-1 
        
        data_item[j+1] = item

if __name__ == "__main__":
    data_item = [22, 75, 80, 40, 11, 25, 5]
    insection_sort(data_item)
    print(data_item)

