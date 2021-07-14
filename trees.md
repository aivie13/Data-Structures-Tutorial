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

