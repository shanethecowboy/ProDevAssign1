# Shane Hendrickson
#CBIS 4210
#Assignment 2
#9/1/2024

# calculate the sum of two numbers
def calculate_sum(num1, num2):
    # sum the two numbers together
    return sum = num1 + num2



# get two inputs from the user and sum them together
def main():
    # get the first number from the user
    num1 = int(input("Enter the first number: "))
    # get the second number from the user
    num2 = int(input("Enter the second number: "))

    # call the calculate_sum function and pass the two numbers as arguments
    sum = calculate_sum(num1, num2)

    # print the sum of the two numbers
    print("The sum of the two numbers is", sum)

# call the main function
main()
