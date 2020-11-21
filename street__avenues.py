# Михаил Коротыч (ИУ7-15Б). Проектно-технологическая практика.
# coding: utf-8
# In[59]:
import copy
def step_forward(x):
	y = copy.copy(x)
	n = x['house_num']
	s = 2 * (n % 2) - 1
	hn = (n + 2 * s) % 100
	pn = x['perp_num'] + s * len([a for a in [1, 98] if a == hn])
	if pn in range(49):
		y['house_num'] = hn
		y['perp_num'] = pn
		return y
	return None
def step_back(x):
	y = copy.copy(x)
	n = x['house_num']
	s = 2 * (n % 2) - 1
	y['house_num'] = n - s
	return y
def turn(x, dr):
	if x['house_num'] not in [0, 99]:
		return None
	y = copy.copy(x)
	s = x['house_num'] % 2
	pn = x['line_num'] - dr
	ln = x['perp_num'] + s
	if pn < 49:
		y['house_num'] = (-3 * dr + 1) % 100
		y['perp_num'] = pn
		y['line_num'] = ln
		y['line_type'] = 1 - x['line_type']
		return y
	return None
def dst_between(x, y, mr):
	n = -1
	lst_passed = []
	lst_current = [x]
	while y not in lst_current:
		n += 1
		lst_next = []
		for z in lst_current:
			lst_z = [step_forward(z), turn(z, 0), turn(z, 1)]
			lst_z = [a for a in lst_z if a and a not in mr and a not in lst_current + lst_passed]
			if not len(lst_z):
				lst_z = [step_back(z)]
			lst_next = lst_next + [a for a in lst_z if a not in lst_next]
		lst_passed = lst_passed + lst_current
		lst_current = copy.copy(lst_next)
	return n
def lst_to_dct(lst):
	x = {}
	x['line_type'] = lst[0][0] == 'A'
	x['line_num'] = int(lst[0][1:])
	x['perp_num'] = int(lst[1][:2])
	x['house_num'] = int(lst[1][2:])
	return x
# In[60]:
f = open('D:\street, avenues\input.txt', 'r')
f1 = open('D:\street, avenues\output.txt', 'w')
mr = []
while True:
	l = f.readline()
	if l[0] == '#':
		break
	lst = l.split()
	x_start = lst_to_dct(lst[:2])
	x_fin = lst_to_dct([lst[0], lst[2]])
	line_num = x_start['line_num']
	line_type = x_start['line_type']
	perp_start = x_start['perp_num']
	perp_fin = x_fin['perp_num']
	perp_betw = [p for p in range(50) if p >= x_start['perp_num'] and p <= x_fin['perp_num']]
	for p in perp_betw:
		for house_num in range(100):
			mr.append({'line_type': line_type, 'perp_num': p, 'line_num': line_num, 'house_num': house_num})
		if p == perp_start:
			for house_num in range(x_start['house_num']):
				mr.remove({'line_type': line_type, 'perp_num': p, 'line_num': line_num, 'house_num': house_num})
		if p == perp_fin:
			for house_num in range(x_fin['house_num'] + 2, 100):
				mr.remove({'line_type': line_type, 'perp_num': p, 'line_num': line_num, 'house_num': house_num})
while True:
	l = f.readline()
	if l[0] == '#':
		break
	lst = l.split()
	x = lst_to_dct(lst[:2])
	y = lst_to_dct(lst[2:])
	f1.write(str(dst_between(x, y, mr)) + '\n')
f1.close()
# In[ ]: