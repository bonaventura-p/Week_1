
#user's name
def name():
    username = raw_input("""User's name?\n""")
    print username


#limit function
def maximum_limit(n, minn, maxn):
    if n < minn: #then you manually define the values for minn and maxn
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


#greetings
def greetings():
	self.username()
    print "Goodbye {}".format(username)


#fizzbuzz output
def fizzbuzz():
	for n in xrange(1,101):
		if n%5==0 and n%3==0:
			print "fizzbuzz"
		elif n%3==0:
			print "fizz"
		elif n%5==0:
			print "buzz"
		else:
			print n