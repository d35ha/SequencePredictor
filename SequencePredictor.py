while True:
	data = raw_input("Enter space separated list:").split(" ")
	new_data = []
	for item in data:
		if not item == "":
			try:
				new_data.append(int(item))
			except:
				new_data.append(item)
	data = new_data
	gets = []
	removes = []
	ch = ""
	br_ = False
	for item in data:
		if ",?" in str(item):
			if "." in str(item):
				item_ = int(item.split(",")[0].split(".")[0]) + int(item.split(",")[0].split(".")[1]) * ((10 ** len(str(item.split(",")[0].split(".")[1]))) ** (-1))
				gets.append(item_)
			else:
				gets.append(int(item.split(",")[0]))
			removes.append(item)
	for item in removes:
		data.remove(item)
	value = data
	index = range(len(value))
	for i in range(len(index)):
		index[i] = index[i] + 1
	for i in range(len(data)):
		if "," in str(value[i]):
			if ch == True:
				br_ = True
				break
			ch = False
			try:
				index[i] = int(value[i].split(",")[0])
			except:
				index[i] = value[i].split(",")[0]
			try:
				value[i] = int(value[i].split(",")[1])
			except:
				value[i] = value[i].split(",")[1]
		else:
			if ch == False:
				br_ = True
				break
			ch = True
	if br_:
		print("Only one system is allowed [points (x,y) or numbers with pre-defined indecies starting from 1]")
		continue
	br = None
	test = []
	for index_ in index:
		if index_ in test:
			br = index_
			break
		test.append(index_)
	if br != None:
		print("You have entered two or more y-values for the same x-value \"{}\"".format(br))
		continue
	for i in range(len(index)):
		if "." in str(index[i]):
			index[i] = int(index[i].split(".")[0]) + int(index[i].split(".")[1]) * ((10 ** len(str(index[i].split(".")[1]))) ** (-1))
	for i in range(len(value)):
		if "." in str(value[i]):
			value[i] = int(value[i].split(".")[0]) + int(value[i].split(".")[1]) * ((10 ** len(str(value[i].split(".")[1]))) ** (-1))
	if len(gets) == 0:
		gets.append(index[-1] + 1)
	print("\n")
	for get in gets:
		res = 0
		for i in range(len(index)):
			value_ = value[i]
			index_ = index[i]
			mul = 1
			for ii in range(len(index)):
				if ii != i:
					mul = mul * ((get - index[ii]) * ((index_ - index[ii]) ** (-1)))
			mul = mul * value_
			res += mul
		print("Predicted value of index {0} is {1}".format(get,res))
	print("\n")
