#Multiplicative persistence

def multP(num):
	multPersSteps = [num]
	while(len(str(num)) > 1):
		total = 1
		for i in range(len(str(num))):
			total *= int(str(num)[i])
		multPersSteps.append(total)
		num = total
	return (multPersSteps)
			
		
		
		