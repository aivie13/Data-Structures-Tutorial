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

Going back to the stack, the great thing about them is that all of the built in functions have efficiency *O(1)*.  The main drawback, however, is that its very inefficient to get to anyhting burried deeper into the stack.  They have a selective use case of anything that benefits from a FIFO (first in, first out) model.

## Implementation

Below we will implement the stack structure using python lists.

```
class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0
```

To test the the code we will run the following:

```
stack = Stack()

## checking is_empty method -> true
print(stack.is_empty())

## pushing the elements
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

## again checking is_empty method -> false
print(stack.is_empty())

## printing the topmost element of the stack -> 5
print(stack.peek())

## popping the topmost element -> 5
stack.pop()

## checking the topmost element using peek method -> 4
print(stack.peek())

## popping all the elements
stack.pop()
stack.pop() 
stack.pop() 
stack.pop() 

## checking the is_empty method for the last time -> true
print(stack.is_empty())
```
Which returns
```
True
False
5
4
True
```

