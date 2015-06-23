
### conditionals quiz
#1
salary= 10000

if salary >= 1000:
    donation= float(0.1) * salary
    print "You can donate" + " " + str(donation) + " " + "this year"
else:
   print "No donation this year"

#2

true_username= "karl"
true_psw= 6666

typed_username= "karl"
typed_psw= 6666

if true_username == typed_username:
	condition1= True  
else:
	condition1= False

if true_psw == typed_psw:
	condition2= True
else:
	condition2= False


if condition1 == True and condition2 == True:
    print "Authentication confirmed"
elif condition1 == True or condition2 == False:
	print "Password not confirmed"
elif condition1== False and condition2 ==True:
	print "Username not confirmed"
else:
    print "Authentication not confirmed"



#######

### list quiz

#1
x=[1,2,[3,5,6]]
x[2][2]

#2
list_of_words=['I','love','ice','cream']
" ".join(list_of_words)

x=[1,2,3,4]
y=[4,5,6,7]
x+y # add y to the right of x in a new list

len(x) # gives the length


