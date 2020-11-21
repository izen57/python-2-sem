import iuliia
with open('data.txt', 'r', errors = 'ignore') as cyr:
	for line in cyr:
		flag = 0
		for i in line:
			if i.isdigit():
				flag = 1
				break
		if flag:
			continue
		with open('latdata.txt', 'a', encoding = 'utf8') as lat:
			lat.write(iuliia.translate(line, iuliia.WIKIPEDIA))