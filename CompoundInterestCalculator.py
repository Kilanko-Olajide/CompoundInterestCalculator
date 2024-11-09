principal = 0
rate = 0
time = 0

while principal <= 0: 
    principal = input("Enter the pricinpal: ")
    principal = float(principal)
    if principal < 0:
        print("You cannot have a pricipal less than 0.")
while rate <= 0:
    rate = input("Enter the rate: ")
    rate = float(rate)
    if rate < 0:
        print("You cannot have a rate less than 0.")
while time <= 0:
    time = input("Enter the time: ")
    time = float(time)
    if time < 0:
        print("You cannot have a time less than 0.")

total = principal * pow((1 + rate/100), time)
print(f"The total is ${total:.2f}")
