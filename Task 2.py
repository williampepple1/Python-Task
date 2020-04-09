# New employee details
import random
import string

user_dict= {}
switch = True

def options():
	password = input(" kindly type your preferred password ")
	if len(password) < 7:
		print("your password must be longer than 7 characters, kindly create another password")
		options()
	elif len(password) >= 7:
			print(password)
			print("your first name is " + first_name)
			print("your last name is " + last_name)
			print("your email is" + email)



while switch:
	
	info = []
	letters = string.ascii_letters
	first_name  = input("What is your First name?  ")
	last_name  = input("What is Last name?  ")
	email = input("What is your email address?  ")

	print("your password is " + str(first_name[0:2])  + str(last_name[-2:]) + 
''.join(random.choice(letters) for i in range (5)))
 
	question = input("Are you satisfied with it? if yes, type yes, if not type no  ")

	if question== "yes":
		print("your first name is " + first_name)
		print("your last name is " + last_name)
		print("your email is" + email)
	

	elif question =="no":
		options()
		
			
	user = {'First Name': first_name , 'Last Name ': last_name, 'Email': email}

	info.append(user)
	
	question = input("Want to add another user, type yes if you want to and No if you dont ?: ")
	if question == 'yes':
		pass
		
	elif question == "no":
		switch = False
	
	user_dict[user["First Name"]] = info

print(user_dict)