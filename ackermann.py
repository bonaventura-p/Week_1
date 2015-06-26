def ackermann(a,b):
	if a==0:
		return b+1
	elif a>0 and b==0:
		return ackermann(a-1,1)
	else:
		return ackermann(a-1,ackermann(a,b-1))

