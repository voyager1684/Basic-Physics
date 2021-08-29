problem = input("Enter the operation (Put a space between each element): \n")          
num1 = float(problem[0:problem.find(" ")])
operator = str(problem[problem.find(" ") + 1 : problem.find(" ") + 2])
num2 = float(problem[problem.find(" ") + 3:])

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
