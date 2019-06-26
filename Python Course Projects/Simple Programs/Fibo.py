#Program that deals with the Fibonacci sequence to the nth number

def fibo(n):
	a = 1
	b = 1

	for x in range(n):
		a,b = b,a+b
		yield a








if __name__ == "__main__":

	n = int(input("Please enter a number to see the Fibonacci Sequence of that number: "))
	print(list(fibo(n)))

