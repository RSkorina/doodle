from turtle import *

# things I want to teach
# from turtle import *
# Forward 
# Turn
# position 

color('red', 'purple')
pen(pensize = 100)
begin_fill()
while True:

	forward(200)
	left(90)
	if abs(pos()) < 1:
		break

end_fill()

done()