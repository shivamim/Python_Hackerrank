#TASK 
'''Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20'''

#SOLUTION 
def calculate_income_tax(income):
    if income <= 10000:
        # No tax for the first $10,000
        tax = 0
    elif income <= 20000:
        # 10% tax for the next $10,000
        tax = 0.1 * (income - 10000)
    else:
        # 10% tax for the first $10,000 and 20% tax for the remaining
        tax = 0.1 * 10000 + 0.2 * (income - 20000)

    return tax

print(calculate_income_tax(60000))
