num = 5
factorial=1

if num < 0:
    printf("Factorial does not exist fornegative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,6):
        factorial=factorial*i

print("factorial of 5 is :",factorial)
