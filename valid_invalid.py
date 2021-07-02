
# operations are valid or not
def check(a, n):
 
    # count number of push operations
    ones = 0;
 
    # traverse in the array
    for i in range (0, n):
 
        # push operation
        if (a[i]):
            ones = ones + 1;
 
        # pop operation
        else:
            ones = ones - 1;
 
        # if at any moment pop() operations
        # exceeds the number of push operations
        if (ones < 0):
            return False;
 
    return True;
 
a = [ 1, 1, 0, 0, 1 ];
n = len(a);
if (check(a, n)):
    print("Valid");
else:
    print("Invalid");

