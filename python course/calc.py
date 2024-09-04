def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "can't divide by 0"
    return x/y
#user input -->> to control fuunctions 
operation_dict ={
    "add":add,
    "substract":substract,
    "multiply":multiply,
    "divide":divide
}
def main():
    while True:
        print("options:")
        print("enter 'add' for addition")
        print("enter 'subtract' for substraction")
        print("enter 'multiply' for multiplication")
        print("enter 'divide' for division")
        print("enter 'quit' to end the program")
        user_input = input(":")
        if user_input =="quit":
            break
        elif user_input in operation_dict : 
            num1 = float(input("enter the first number : "))
            num2 = float(input("enter the second number : "))
            operation =operation_dict[user_input]
            result = operation(num1,num2)
            print("result:",result)
        else:
            print("invalid input")

