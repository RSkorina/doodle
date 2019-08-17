def fizzBuzz(n):
	for i in range(0,n):
		output = ""
		if (i % 3 == 0): output += "fizz"
		if (i % 5 == 0): output += "buzz"
		if (output == ""): print(i)
		else: print(output)
		
fizzBuzz(100)

		