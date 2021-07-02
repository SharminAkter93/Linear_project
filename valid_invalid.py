
# # operations are valid or not
# def check(a, n):
 
#     # count number of push operations
#     ones = 0;
 
#     # traverse in the array
#     for i in range (0, n):
 
#         # push operation
#         if (a[i]):
#             ones = ones + 1;
 
#         # pop operation
#         else:
#             ones = ones - 1;
 
#         # if at any moment pop() operations
#         # exceeds the number of push operations
#         if (ones < 0):
#             return False;
 
#     return True;
 
# a = [ 1, 1, 0, 0, 1 ];
# n = len(a);
# if (check(a, n)):
#     print("Valid");
# else:
#     print("Invalid");


# class Stack:
# 	     def __init__(self):
# 	         self.items = []
	
# 	     def isEmpty(self):
# 	         return self.items == []
	
# 	     def push(self, item):
# 	         self.items.insert(0,item)
	
# 	     def pop(self):
# 	         return self.items.pop(0)
	
# 	     def peek(self):
# 	         return self.items[0]
	
# 	     def size(self):
# 	         return len(self.items)
	
# s = Stack()
# s.push('hello')
# s.push('true')
# print(s.pop())
 

 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop()) 
# will cause an IndexError
# as the stack is now empty