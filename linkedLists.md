## Introduction

Linked lists are a lot like normal lists.  They hold an arbitrary amount of data and can index through it fairly easily.  Linked lists end up being like a chain.  Every entry knows where the next and previous item is.

## Linked vs Unlinked

The difference ends up being in the linking.  In python, a standard list is a dynamic array that resizes itself as it fills up.  A linked list does not need to be resized.  Every time a new element is added, it gets linked onto the end with data for where the previous item is.  The main drawback of this implementation is that in order to search for a specific value, it is necessary to check every entry in sequential order.

## Example

![Linked List](assets/Linkedlist.png)

```
class Node:

    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None
                          
  
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertTail(self, value):
        new_tail = LinkedList.Node(value)

        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
```

Above we have a simple linked list class implementation.  To start it is empty, and every new item inserted will become a new tail.  Each item will have member data of its value, the previous item's location, and the next item location.

Let's look at an example problem:

Given a linked list, find the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
If there are even nodes, then there would be two middle nodes, print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4. 

```
class Node:

	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		node = self.head
		while node:
			print(str(node.data) + "->", end="")
			node = node.next
		print("NULL")

	def printMiddle(self):
		iterMiddle = self.head
		iterEnd = self.head

        # one iterator will jump by 1's the other by 2's, when iterEnd reaches the end, iterMiddle will be in the middle

		while iterEnd and iterEnd.next:
			iterMiddle = iterMiddle.next
			iterEnd = iterEnd.next.next
		
		# return middle element
		print("The middle element is ", slow.data)


l = LinkedList()

for i in range(1, 23, 2):
    l.push(i)
    l.printList()
    l.printMiddle()
```