# Tip Calculator
print("Welcome to the Tip Calculator")
bill_amt = float(input("What was the total Bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
bill_split = int(input("How many prople to split the bill? "))

bill_with_tip = tip / 100 * bill_amt + bill_amt
bill_pay = round((bill_with_tip/bill_split),2)

print(f"Each person should pay: {bill_pay}")