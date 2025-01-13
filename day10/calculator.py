from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation_dict= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(logo)
    number1=float(input("Enter the first number:\n"))
    print("+")
    print("-")
    print("*")
    print("/")

    previous_calculate = True
    while previous_calculate:

        operation = input("Type your operation:\n")
        number2= float(input("Enter the second number:\n"))

        answer = operation_dict[operation](number1,number2)
        print(f"{number1} {operation} {number2} = {answer}")


        next_step = input(f"Type 'y' to continue calculation from {answer} and 'n' to start new calculation ").lower()

        if next_step=="y":
            number1=answer
        elif next_step=="n":
            previous_calculate=False
            print("\n"*100)
            calculator()

calculator()




