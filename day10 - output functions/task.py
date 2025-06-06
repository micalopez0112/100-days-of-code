number = input("What is the number?:")
print("+\n-\n*\n/")
operator = input("What is the operator?:")
number2 = input("What is the second number?:")

print(f"{number} {operator} {number2} = {eval(f'{number} {operator} {number2}')}")