## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:
"""Your goal is to find the number of months it takes to save up for a down payment. The cost of your down payment is calculated by multiplying the
total cost of your dream house by the down payment percentage."""
##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter the yearly salary: "))
portion_saved = float(input("Enter the portion of salary saved: "))
cost_of_dream_home = float(input("Enter the cost of dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
#############
cost_of_dp = cost_of_dream_home * portion_down_payment

while amount_saved < cost_of_dp:
    amount_saved += amount_saved * (r/12) + (yearly_salary/12)*portion_saved
    months += 1

print("Number of months:", months)