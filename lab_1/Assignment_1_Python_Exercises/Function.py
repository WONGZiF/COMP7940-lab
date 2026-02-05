# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    for i in range(2, x):
        if x % i == 0:
            print(i)
    
# Call the function with 52633
print_factor(52633)