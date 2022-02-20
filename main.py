from math import sqrt

print("Solve ax^2 + bx + c = 0 (find zeroes of equation)")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("jo")
if a==0:
	if b==0:
		if c==0:
			print("x el R")
		else:
			print("x = {}")
	else:
		print("x = " + str(-(c/b)))
else:
	d = b * b - 4 * a * c
	if d == 0:
		print("x = " + str(-b/(2*a)))
	elif d < 0:
		print("x = {}")
	else:
		print("x1 = " + str((-b + sqrt(d)) / (2*a)))
		print("x2 = " + str((-b - sqrt(d)) / (2*a)))
	