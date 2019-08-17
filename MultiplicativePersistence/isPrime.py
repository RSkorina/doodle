import math
def isP(num):
	for i in range(3, math.ceil(num**0.5), 2):
		if(num % i == 0): return i
	return False

def factor(num):
	factorOf = isP(num)
	if (factorOf):
		print(factorOf)
		factor(num/factorOf)
	else: 
		print(int(num))
	

		