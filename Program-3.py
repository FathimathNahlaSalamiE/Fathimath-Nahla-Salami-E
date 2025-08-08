def my_function(num):
    if num  % 2 != 0:
        for i in range(2*num):
            if i % 2 != 0:
                print(i,end=", ")
    else:
        return my_function(num-1)

a = int(input("Enter a number : "))
my_function(a)