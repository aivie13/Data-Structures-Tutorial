# Linked Lists

## Introduction

Linked lists are a lot like normal lists.  They hold an arbitrary amount of data and can index through it fairly easily.  Linked lists end up being like a chain.  Every entry knows where the next and previous item is.

## Linked vs Unlinked

The difference ends up being in the linking.  In python, a standard list is a dynamic array that resizes itself as it fills up.  A linked list does not need to be resized.  Every time a new element is added, it gets linked onto the end with data for where the previous item is.  The main drawback of this implementation is that in order to search for a specific value, it is necessary to check every entry in sequential order.

Linked lists can be of the singly or doubly linked variety.  A singly linked list can only be traversed in one direction and must be started from the head, while a doubly linked list has bot a head and a tail as possible starting points and can be traversed in either direction.

The main advantage of a linked list over a dynamic array comes in adding a single item to the end of the list or the beginning of the list.  Dynamic arrays have a soft limit on size, when that limit is reached, hte array is copied into a new array with double the size.  For a linked list, this is a simple **O(1)** operation where the pointers are reassigned.  Arrays cannot add new data to or delete from the front either, again the whole array would need to be copied into a new one.

## Functions

* **insert_head(value)** - takes a value and makes it the new head of the list, linking it to the old head and the old head bacck to it in a doubly linked list.  **O(1)** performance.

* **insert_tail(value)** - takes a value and makes it the new tail, linking the old tail to it ant it back to the old tail in a doubly linked list.  **O(1)** performance.

* **insert(i, value)** - takes a value and a number **i**.  THere are two ways to implement this, either the function inserts after the **i**th node, or after the node whose value is **i**.  Either way, the persformance is **O(n)**.

* **remove_head()** - removes the head of the list and assigns the next value as the new head.  **O(1)** performance.

* **remove_tail()** - removes the tail of the list and assigns the previous value as the new tail.  **O(1)** performance.

* **remove(i)** - Either removes the **i**th entry from the list or searches for a value equal to **i**, then removes it. **O(n)** performance.

* **size()** - returns the size of the list.  **O(1)** performance.

* **empty()** - returns true is the list is empty. **O(1)** performance.

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
		print("The middle element is ", iterMiddle.data)


l = LinkedList()

for i in range(1, 23, 2):
    l.push(i)
    l.printList()
    l.printMiddle()
```

Lets quickly run through each of these functions.

* *push(self, new_data)* is inserting new nodes.  It takes the current node and links it to a new node with a new data value.

* *printList(self)*  will traverse the list, starting at the head. It will print the data value at each node, then a -> representing the link to the next node.

* *printMiddle(self)* is where the real solution to this problem lies.  There are two iterators here, one that jumps by 2's and another that jumps by 1's.  By the time the **iterEnd** reaches the end, **iterMiddle** will have gone half as far and be at the middle, so the function prints the data stored where **iterMiddle** elds up.

As we can see, it's not as simple using a linked list.  You can't just pop out the value at an index, you have to iterate through every entry.
## Problem

Implement a queue for a line using a linked list. PAtrons in the line will have 3 types of memberships: Gold, silver, or none.  Gold members have priority over silver and silver have priority over those without any membership.

[Solution](linkedListSolution.py)