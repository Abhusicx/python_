print("Welcome to the tip calculator!")
total_bill=input("what is the bill?")
bill_percentage=input("what is the tip percentage of total bill?")
tip=float(total_bill)*(float(bill_percentage)/100)
net=float(total_bill) + (float(tip))
print(f"total bill {net}")
person=int(input("total number of person : "))
per_person_bill=net/person
print(f"per person bill {per_person_bill}" )