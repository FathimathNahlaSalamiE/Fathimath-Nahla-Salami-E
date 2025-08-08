class CalculatorProgram:
    def calculator_operations(self,a,b,type_of_operation):
        if type_of_operation == "+":
            print(a,"+",b,"=",a+b)
        elif type_of_operation == "-":
            print(a,"-",b,"=",a-b)
        elif type_of_operation == "*":
            print(a,"*",b,"=",a*b)
        elif type_of_operation == "/":
            try:
                print(a,"+",b,"=",a/b)
            except ZeroDivisionError:
                print("Enter a number other than zero!")
        else:
            print("Enter valid operation!")

first_num = float(input("Enter first number : "))
second_num = float(input("Enter second number : "))
operation_type = input("Enter the operation : ")

obj = CalculatorProgram()
obj.calculator_operations(first_num,second_num,operation_type)