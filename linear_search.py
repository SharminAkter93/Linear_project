
def search (list1,key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("key element is found")
            break
    else:
            print("key element is not found")
list1 = [34,23,5,6,7,1,23,8] 
print(list1)
key = int(input("enter the key element:"))   
search (list1,key)    