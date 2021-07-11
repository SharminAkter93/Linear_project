# Implementation Bubble sort

def bubble_sort(data_list):
    data_length = len(data_list)

    for i in range(data_length):
        for j in range(data_length-i-1):
            if data_list[j] > data_list[j+1]:
                # swap
                result = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = result


if __name__ == "__main__":
    data_list = [12, 45, 2, 36, 54, 30, 50]
    bubble_sort(data_list)
    print("Bubble sort is: ", data_list)