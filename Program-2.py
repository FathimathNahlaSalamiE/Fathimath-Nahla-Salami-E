def odd_numbers(num):
    for i in range(2*num):
        if i % 2 != 0:
            print(i, end=", ")

a=int(input("Enter a number : "))
odd_numbers(a)