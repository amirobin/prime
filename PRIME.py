#def is_prime(num):
	#if num < 2 :
	#	return False
	#elif num == 2 or num == 3:
	#	return True
	#elif num % 2==0:
	#	return False
    #	for x in range(3,num):
    #		if num % x == 0:
    #			return False
   	#	else:
   	#		return True
#print is_prime(35)

def is_prime(num):
	for num in range(2,num):
		prime =True;
		for i in range(2,num):
			if num%i==0:
				prime=False;

		
		if prime:
			print (num)

is_prime(20);
