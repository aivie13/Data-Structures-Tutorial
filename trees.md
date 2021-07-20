# Trees

## Introduction

Trees are a lot like a multidimensional singly linked list.  Trees have a series of nodes liked to parents and children.  Each node will have a single parent but an arbitrary number of children.  The main difference between trees and linked lists is that lists are linear in nature, while trees are heirarchal.  The topmost node or oldest grandparent is referred to as the root, while the outermost children are often called the leaves.

```
      tree
      ----
       j    <-- root
     /   \
    f      k  
  /   \      \
 a     h      z    <-- leaves
```

 Above is an example of a binary tree. Binary because each node has at most 2 children, but trees can have an arbitrary number of children.  A tree with nodes that have at most **n** children will be referred to as n-ary. 

 The main function of trees is to organize data for quick lookup.  Think of a file system.  You have a root folder and a series of importand folders that each contain successively less important folders and so on. This makes it easy to navigate the tree and find exactly what you're looking for without having to look through your whole filesystem for a specific file.

```
 file system
-----------
     /    <-- root
  /      \
...       home
      /          \
   stuff        school
    /       /      |     \
  ...      cs101  cs112  cs113
```

## Recursion

Trees are best defined in the scope of recursion, which to understand, we must first define recursion.

Recursion is a way to have a program execute multiple times in a row, similar to a loop.  While a standard loop has a known number of iterations and an unknown endpoint, a recursive call has a known endpoint and unknown number of iterations.  Let's look at an example.

```
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 7
print("Fibonacci sequence:")
for i in range(1, nterms):
    print(recur_fibo(i))
```

If the program's input is 1, it will return 1, otherwise it will add 2 instances of the program, one with input n-1, the other with n-2. Let's look at a more graphical representation of **recur_fibo(4)**.

```
recur_fib(4)________________________________
    |                                       |
recur_fib(3)________________       +     recur_fib(2)_______
    |                       |               |               |
recur_fib(2)______  +    recur_fib(1)     recur_fib(1) + recur_fib(0)
    |             |              |          |               |
recur_fib(1) + recur_fib(0)      1          1         +     0 
    |               |
    1        +      0
```
And we see that **recur_fib(4)** turns into 1+0+1+1+0 or 3.  
```
>>> print(recur_fibo(4))
3
```
So to bring it all together, recursion just means calling the function from within the function so that it repeats until an exit prompt is fulfilled. In our case, that was n <= 1.

## Functions
Trees have many similar functions to linked lists, but since we add a dimension to traverse, the perfomance is a bit different.

* **insert(value)** - will insert a value into the tree.  It must traverse subtrees to compare with relative node values to find where the new value should be inserted.  Perfomance of **O(log n)**.

* **remove(value)** - will traverse the tree looking for a specified value and remove it.  The adjacent nodes will then need to be rearranged.  Perfomance of **O(log n)**.

* **contains(value)** - takes a value and searches recursively through the tree to check if the value exists.  Perfomance of **O(log n)**.

* **empty()** - returns true if the tree has no nodes.    Perfomance of **O(1)**.

## Example
Let's implement a data structure and pay special attention to the recursion aspects.  
```
class BST:

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, recursively find the location 
        to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BST.Node(data)
                elif node.left.data != data:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)

            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BST.Node(data)
                elif node.right.data != data:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)
```

Now a very useful function for our tree would be to generate a balanced tree from a set of sorted data.  If we simply looped through the data, we would end up with a 1-dimensional linked list.  We need to find the middle of the list and set that as the root, then recursively call it for each subtree.  



## Problem

Write a program to find the lowest common ancestor given 2 nodes.  Think of this as the smallest enclosing folder for 2 files in a system.

[Solution](treeSolution.py) 