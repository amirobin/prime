def data_type(data):
	if type(data)is str:
		print len(data);
	if type(data) is bool:
		print str(data);
	if type(data) is int:
		if data<100:
			print str(data)+ 'is less than 100';
		else:
			print str(data)+ 'is more than 100'
	if type(data) is list:
		if len(data)>3:
			print data[2]
		else:
			print 'None'
	elif type(data) is None :
		print 'no value'
data_type([5,8,9,0,5,4])