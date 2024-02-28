def fibonacci_series(num):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(num - 2):
        third = first + second
        print(third)
        first, second = second, third

num = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series(num)
