# Write a function that prints all factors of the given parameter x
def print_factor(x):
# your code here
    if x == 'q':
        exit()
    for i in range(1, int(x) + 1):
        if int(x) % i == 0:
            print(i)

while True:
    x = input("Please input a number (input 'q' to quit): ")
    print_factor(x)