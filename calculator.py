while True:
	print('CALCULATOR \n')
	print('OPTIONS:')
	print('To add 2 numbers, enter add')
	print('To subtract 2 numbers, enter subtract')
	print('To divide 2 numbers, enter divide')
	print('To multiply 2 numbers, enter multiply')
	print('To quit the program, enter quit')
	userinput=input('ENTER SELECTION:')

	
	if userinput=='quit':
		break
	


	elif userinput=='add':
		a=float(input('ENTER FIRST NUMBER:'))
		b=float(input('ENTER SECOND NUMBER:'))
		c=a+b
		print('SUM IS', c)
		#break



	elif userinput=='subtract':
		a=float(input('ENTER FIRST NUMBER:'))
		b=float(input('ENTER SECOND NUMBER:'))
		c=a-b
		print('DIFFRENCE IS', c)
		#break



	elif userinput=='multiply':
		a=float(input('ENTER FIRST NUMBER:'))
		b=float(input('ENTER SECOND NUMBER:'))
		c=a*b
		print('PROD IS', c)
		#break



	elif userinput=='divide':
		a=float(input('ENTER FIRST NUMBER:'))
		b=float(input('ENTER SECOND NUMBER:'))
		c=a/b
		print('QUOTIENT IS', c)
		#break



	else:
		print('UNKNOWN INPUT')
		#break


