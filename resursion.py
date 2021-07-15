# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 7
# print("Fibonacci sequence:")
# for i in range(1, nterms):
#     print(recur_fibo(i))
print(recur_fibo(4))

