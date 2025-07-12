def part_c(initial_deposit):
	#########################################################################
	house_cost = 800000
	down_payment = house_cost* .25
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	steps = 0
	lower_guess = 0 # lower bound
	upper_guess = 1 # upper bound
	g=0.5
	
	r = 0
	if initial_deposit * (1 + 1 / 12) ** 36 < down_payment:
	    r = None
	elif initial_deposit < down_payment:
	    while r != g:
	        steps += 1
	        g = (lower_guess + upper_guess ) / 2
	        amount_saved = initial_deposit * (1 + g / 12) ** 36
	
	        if amount_saved < down_payment-100:
	            lower_guess = g
	        elif amount_saved > down_payment+100:
	            upper_guess = g
	        else:
	            r = g
	
	
	print(r)
	print (steps)
	
	return r, steps