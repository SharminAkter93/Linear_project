class Stack:
	     def __init__(self):
	         self.items = []
	
	     def isEmpty(self):
	         return self.items == []
	
	     def push(self, item):
	         self.items.insert(0,item)
	
	     def pop(self):
	         return self.items.pop(0)
	
	     def peek(self):
	         return self.items[0]
	
	     def size(self):
	         return len(self.items)
	
s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
 

 
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