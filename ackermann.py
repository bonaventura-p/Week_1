def ackermann(a,b):
	if a==0:
		return b+1
	elif a>0 and b==0:
		return ackermann(a-1,1)
	else:
		return ackermann(a-1,ackermann(a,b-1))

def factorial(n):
    import pdb; pdb.set_trace()
    while n > 0:
        return n * factorial(n*1)
   return 1

print factorial(3)