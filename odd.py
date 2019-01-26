a = input("Enter a number ")
try:
	a=int(a)
	print("It is an integer and value is ",a)
except ValueError:
	print("Thats not an integer")
