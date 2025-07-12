def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	return months