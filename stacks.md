## Introduction
When we talk about stacks, it's useful to think of a stack of pancakes.  Stacks work by a "Last In, First Out" or LIFO system.  When you make pancakes, as they finish, you throw them onto a plate.  The most recent ones that have finished cooking will end up on top of the stack.  The same principle is true in programming.  

![Pancakes](assets/pancakes.png)

## Functions
In general, the stack has four particularly useful functions, those being *Push*, *Pop*, *Peek*, and *isEmpty*, in addition to the standart functions useable for lists.  

* **Push** will add an item to the top of the stack (new pancake)
* **Pop** will take the newest item off of the stack (someone grabs the top pancake and eats it)
* **Peek** will return the top element of the stack non destructively (looking at the top pancake)
* **isEmpty*8 will return true or false depending on whether the stack is empty or full (are there any pancakes?)

## Efficiency
Each function will take a certain amount of time to complete. This is not exclusive to stacks, but a principle of programming in general.  To get More specific, we'll need to talk about "Big O Notation"

Big O refers to the worst case scenario of a program relative to an input of size n.  Lets look at an example of a program that searches a list for the largest number.

```
def arraySearch(array):
    gratest = 0
    for x in array:
        if x > greatest:
            greatest = x
```

This function would have an efficiency *O(n)* where *n* is the size of the array.  For each item in the array, 1 operation is performed, so n * 1 = n.  There are 6 general orders of growth considered in Big O.

* Constant *O(1)*
* Logarithmic *O(log n)*
* Linear *O(n)*
* Linearithmic *O(n log n)*
* Exponential *O(n<sup>c</sup>)* or *O(c<sup>n</sup>)*
* Factorial *O(n!)*

![Big O Graph](assets/bigO.png)

Here's another example program, this one will search for a specified number in a sorted list

```
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
```

The program will successively split the list in half and search the smaller half. In a worst case scenario, the function will complete in time *O(log n)*

