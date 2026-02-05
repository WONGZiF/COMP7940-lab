# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
for x in l:
    print(f"Factors of {x}:")
    for i in range(2, x):
        if x % i == 0:
            print(i)
    print("---------------------")
