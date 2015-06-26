def add(a,b):
	c= a+b
	print "The answer is:{0}+{1}={2}".format(a,b,c)

def substract(a,b):
	c=a-b
	print "The answer is: {0}-{1}={2}".format(a,b,c)

def divide(a,b):
	c=a/b
	print "The answer is:{0}/{1}={2}".format(a,b,c)

def multiply(a,b):
	c=a*b
	print "The answer is: {0}*{1}={2}".format(a,b,c)

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
        
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#Function to capture and execute the user's choice
def choice():
    operation = int(raw_input("""Select operation: \n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Factorial \n 6. Fibonacci \n Enter choice (1/2/3/4/5/6):"""))

    if operation == 1:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        add(float(a), float(b))

    elif operation== 2:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        subtract(float(a), float(b))

    elif operation == 3:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        multiply(float(a), float(b))

    elif operation== 4:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        divide(float(a), float(b))

    elif operation==5:
        a=raw_input("Enter the number:\n")
        print "The answer is %s" % factorial(int(a))

    elif operation==6:
        a=raw_input("Enter the number:\n")
        print "The answer is %s" % fibonacci(int(a))

    else:
        print "Please select a valid operation"
        choice()

if __name__ == '__main__':
    choice()  