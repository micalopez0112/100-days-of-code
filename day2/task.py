print("Hello"[-4])

print("123" + "456")

print(123 + 456)

print(123_456)

print(123.456)


print(True)
print(False)

print(type(123))
print(type(123.456))
print(type("123"))
print(type(True))

# print("Number of letters in your name:" + str(len(input("Enter your name: "))))

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
