# collatz.py
# Author : Adedoyinsola Fifo
## numbers


num = int(input("Enter a positive integer: "))
while num != 1:
    print(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
print(num)

