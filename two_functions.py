#Программа Михаила Коротыча (ИУ7-15Б) для вычисления значений функций и построения по ним их графиков
from math import cos
mxmz = -(1e-10) #Максимум функции
mnmz = 1e-10 #Минимум функции
start = float(input('Введите начальный аргумент: '))
stop = float(input('Введите конечный аргумент: '))
step = float(input('Введите шаг, больший нуля: '))
print('{:36}'.format('_' * 39))
print('{:8.2}'.format('step'), '{:4}'.format(' |'), '{:8.2}'.format('z1'), '{:4}'.format(' |'), '{:8.2}'.format('z2'), '{:4}'.format(' |'))
drstep = step
y = int(start / step)
x = int(stop / step)
#Вывод таблицы
for step in range(y, x):
	step *= drstep
	z1 = start - cos(step)
	z2 = 18 * step ** 4 + 26 * step ** 3 - 2.3 * step * step + 10.1 * step - 7.1
	if z2 > mxmz:
		mxmz = z2
		mxmx = step
	if  z2 < mnmz:
		mnmz = z2
	print('{:8.2}'.format(step), '{:4}'.format(' |'), "{:8.2}".format(z1), '{:4}'.format(' |'), '{:8.2}'.format(z2), '{:4}'.format(' |'))
	print('_' * 39)
print('Максимальные значение аргумента и значения функции: {:.6} и {:.6}'.format(mxmx, mxmz))
zas = int(input('Введите количество засечек: '))
R = round(100 / zas)
o_zas = (mxmz + abs(mnmz)) / zas #Значения
o_zas = round(o_zas, 1)
line_x = round(o_zas, 2) #Количество тире для рисования оси абсцисс
#График отн. ординат:
line_y = int(abs(round(mnmz, 2) * 100))
zsg = ' ' * line_y
if y > 0:
	line_x = int(line_x * 100)
	wsg = ('-' * R + '|') * zas
	print('{:5}'.format(' '), wsg)
	for step in range(y, x):
		step *= drstep
		z2 = 18 * step ** 4 + 26 * step ** 3 - 2.3 * step * step + 10.1 * step - 7.1
		okr_z = int(abs(round(z2, 2)) * 100)
		if z2 < 0:
			oo = line_y - okr_z
			okr_z = (okr_z - 1) * ' '
			oo *= ' '
			dd = int(round(drstep, 2) * 100)
			if step > 0:
				for i in range(0, dd):
					print('{:5}'.format(' '), zsg + '|')
				print('{:5}'.format(step), oo + '*' + okr_z + '-')
		elif z2 > 0:
			okr_z *= ' '
			dd = int(round(drstep, 2) * 100)
			if step > 0:
				for i in range(0, dd):
					print('{:5}'.format(' '), zsg + '|')
				print('{:5.2}'.format(step), zsg + '-' + okr_z + '*')
else:
	step += y
	for step in range(y, x):
		if not step:
			line_x = int(line_x * 100)
			wsg = (('-' * R) + '|') * zas
			print('{:5}'.format(' '), wsg)
		step *= drstep
		z2 = 18 * step ** 4 + 26 * step ** 3 - 2.3 * step * step + 10.1 * step -7.1
		okr_z = int(abs(round(z2, 2)) * 100)
		if z2 < 0:
			oo = line_y - okr_z
			okr_z = (okr_z - 1) * ' '
			oo *= ' '
			dd = int(round(drstep, 2) * 100)
			if step > 0:
				for i in range(0, dd):
					print('{:5}'.format(' '), zsg + '|')
				print('{:5.2}'.format(step), oo + '*'+ okr_z + '-')
		elif z2 > 0:
			okr_z *= ' '
			dd = int(round(drstep, 2) * 100)
			if step > 0:
				for i in range(0, dd):
					print('{:5}'.format(' '), zsg + '|')
				print('{:5.2}'.format(step), zsg + '-' + okr_z + '*')