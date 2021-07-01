# # Binary_search 
def binary_searchiter(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else: 
            return mid
    return -1
arr = [4, 7, 9, 16, 20, 25]
n = 10
r = binary_searchiter(arr, n)
if r != -1:
    print("Element found at index", str(r))
else: 
    print("Element is not present in array")



def charecter_binary(Letters, target):
    start = 0
    end = len(Letters) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = Letters[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle

Letters = ["A", "B", "C", "D", "E", "F"]
found = charecter_binary(Letters, "E")
print("Search letter found at ",found," index")

