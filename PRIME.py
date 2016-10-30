def is_prime(num):
	for num in range(2,num):
		prime =True;
		for i in range(2,num):
			if num%i==0:
				prime=False;

		
		if prime:
			print (num)

is_prime(20);
