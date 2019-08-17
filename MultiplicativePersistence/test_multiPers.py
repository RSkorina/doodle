#Test multiPerse
import multiPers as mp

def test_multP():
	assert mp.multP(3) == [3], "One digit"
	assert mp.multP(0) == [0], "zero"
	assert mp.multP(23) == [23, 6], "Two Digit"
	assert mp.multP(277777788888899) == [277777788888899, 4996238671872, 438939648, 4478976, 338688, 27648, 2688, 768, 336, 54, 20, 0], "smallets 11 step"
	
	
	
	



if (__name__ == "__main__"):
	test_multP()
	print("Everything passed")