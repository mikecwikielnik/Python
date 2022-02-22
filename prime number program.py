from sympy import *

# below is the prime number function

primes = []
for i in range(1,10):
    if isprime(i):
        primes.append(i)

print(primes)





# below is just taking i in range and dividing them by 2 and printing all even numbers LOL


for value in range(1,100):
    if value % 2 == 0:
        print(f"{value} is a prime number and Bank of China should take Mike C. as a data analyst. He can do anything!")
        

# this second way appends an empty set so you can print the values set any time you want 

values=[]
for value in range(5,15):
    if value % 2 == 0:    # remember mod is a remainder that isn't zero. 5/2 does not leave a nice clean integer. 
        values.append(value)
        #break
    else:
         print(value)


print(values)





