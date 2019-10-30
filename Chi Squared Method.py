import math

def main():
	# data = [X, Measured Y, Best Fit Y, Measured Y Uncertainty]
	data = [[5.12033e-7, 7.71104e-4, 7.87376e-4, 5.73e-5], 
	[5.71429e-7, 8.37411e-4, 8.78712e-4, 5.95e-5], 
	[5.43478e-7, 8.23391e-4, 8.35731e-4, 5.19e-5],
	[4.90436e-7, 8.23951e-4, 7.54166e-4, 4.85e-5]]
	degreesOfFreedom = 3
	chiSquared(data, degreesOfFreedom)

	return 0

def chiSquared(data, degreesOfFreedom):
	accum = 0
	for i in range(0, len(data), 1):
		accum += (data[i][1] - data[i][2])**2 / data[i][3]**2

	print("  Chi squared:",round(accum,5))
	print("  Reduced chi squared:",round(accum/degreesOfFreedom,5),"\n")

	return accum

main()