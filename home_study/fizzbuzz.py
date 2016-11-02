def fizzbuzz(num):
	if num%3==0 :
		if num%5==0:
			print 'fizzbuzz'
		else:
			print 'fizz'

	elif num%5==0 :
		print 'buzz'

	else:
		print str(num)
fizzbuzz(8)
