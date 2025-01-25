# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
for x in l:
    print(f"The factors of {x} is:")
    for i in range(1, x+1):
        if x % i == 0:
            if i != x:
                print(i, end=', ')
            else:
                print(i, end='\n')