# Initialize a queue

queue_exm = []

# Adding elements to the queue

queue_exm.append('x')

queue_exm.append('y')

queue_exm.append('z')

print("Queue before any operations")

print(queue_exm)

# Removing elements from the queue

print("\nDequeuing items")

print(queue_exm.pop(0))

print(queue_exm.pop(0))

print(queue_exm.pop(0))

print("\nQueue after deque operations")

print(queue_exm)




# Creating the queue class

class Queue:  

  def __init__(self):  

      self.queue = list()  

  def element_add_exm(self,data):  

# Using the insert method  

      if data not in self.queue:  

          self.queue.insert(0,data)  

          return True  

      return False   

  def leng(self):  

      return len(self.queue)   

Queue_add = Queue()  

Queue_add.element_add_exm("Mercedes Benz")  

Queue_add.element_add_exm("BMW")  

Queue_add.element_add_exm("Maserati")  

Queue_add.element_add_exm("Ferrari")

Queue_add.element_add_exm("Lamborghini")

print("Queue's Length: ",Queue_add.leng())  



# Creating the queue class

class Queue:  

  def __init__(self):  

      self.queue = list()  

  def element_add_exm(self,data):  

# Using the insert method  

      if data not in self.queue:  

          self.queue.insert(0,data)  

          return True  

      return False

# Removing elements  

  def element_remove_exm(self):  

      if len(self.queue)>0:  

          return self.queue.pop()  

      return ("Empty Queue")  

queu = Queue()  

queu.element_add_exm("A")  

queu.element_add_exm("B")  

queu.element_add_exm("C")  

queu.element_add_exm("D")  

print(queu)

print(queu.element_remove_exm())  

print(queu.element_remove_exm())



# Queue short

import queue  

queu = queue.Queue()  

queu.put(5)  

queu.put(24)  

queu.put(16)  

queu.put(33)  

queu.put(6)    

# Using bubble sort algorithm for sorting  

i =  queu.qsize()  

for x in range(i):  

    # Removing elements  

    n = queu.get()  

    for j in range(i-1):  

        # Removing elements  

        y = queu.get()  

        if n > y :  

            # putting smaller elements at beginning  

            queu.put(y)  

        else:  

            queu.put(n)  

            n = y

    queu.put(n)  

while (queu.empty() == False):   

    print(queu.queue[0], end = " ")    

    queu.get()





