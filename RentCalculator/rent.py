rent = int(input("Enter your flate/hostel rent = "))
food = int(input("Enter the amount of food ordered = "))

electricity_spend = int(input("enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the change per unit = "))
persons = int(input("enter the numbers of persons living in room/flate = "))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill)//persons #no of persons

print("Each person will pay =", output)