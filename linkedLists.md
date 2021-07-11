## Introduction

Linked lists are a lot like normal lists.  They hold an arbitrary amount of data and can index through it fairly easily.  Linked lists end up being like a chain.  Every entry knows where the next and previous item is.

## Linked vs Unlinked

The difference ends up being in the linking.  In python, a standard list is a dynamic array that resizes itself as it fills up.  A linked list does not need to be resized.  Every time a new element is added, it gets linked onto the end with data for where the previous item is.  The main drawback of this implementation is that in order to search for a specific value, it is necessary to check every entry in sequential order.

## Example

![Linked List](assets/Linkedlist.png)

```
class Node:

    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
                          # next as null
  
class LinkedList:

    def __init__(self):
        self.head = None
```