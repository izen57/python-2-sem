from tkinter import ttk
from tkinter import *
import tkinter.messagebox as box
def summary(num1, num2):
	str_num1 = str(num1)
	str_num2 = str(num2)
	result = str()
	prom = str()
	div = 0
	try:
		dot1 = str_num1.index('.')
	except BaseException:
		dot1 = -1
	try:
		dot2 = str_num2.index('.')
	except BaseException:
		dot2 = -1
	if dot1 == -1 and dot2 != -1:
		for i in range(dot2 + 1, len(str_num2)):
			result += str_num2[i]
		result = result[::-1]
	elif dot2 == -1 and dot1 != -1:
		for i in range(dot1 + 1, len(str_num1)):
			result += str_num1[i]
		result = result[::-1]
	elif dot1 != -1 and dot2 != -1:
		start = 0
		if len(str_num1) - dot1 > len(str_num2) - dot2:
			for i in range(dot1 + len(str_num2) - dot2, len(str_num1)):
				prom += str_num1[i]
			result += prom[::-1]
			start = 2
		elif len(str_num2) - dot2 > len(str_num1) - dot1:
			for i in range(dot2 + len(str_num1) - dot1, len(str_num2)):
				prom += str_num2[i]
			result += prom[::-1]
			start = 1
		if start == 1:
			for i in range(len(str_num1) - 1 - dot1, 0, -1):
				mod = (int(str_num1[dot1 + i]) + int(str_num2[dot2 + i]) + div) % 3
				div = (int(str_num1[dot1 + i]) + int(str_num2[dot2 + i]) + div) // 3
				result += str(mod)
			result += '.'
		else:
			for i in range(len(str_num2) - 1 - dot2, 0, -1):
				mod = (int(str_num1[dot1 + i]) + int(str_num2[dot2 + i]) + div) % 3
				div = (int(str_num1[dot1 + i]) + int(str_num2[dot2 + i]) + div) // 3
				result += str(mod)
			result += '.'
	if dot1 > dot2:
		for i in range(dot2 - 1, -1, -1):
			mod = (int(str_num1[dot1 - dot2 + i]) + int(str_num2[i]) + div) % 3
			div = (int(str_num1[dot1 - dot2 + i]) + int(str_num2[i]) + div) // 3
			result += str(mod)
		for i in range(dot1 - dot2 - 1, -1, -1):
			result += str((int(str_num1[i]) + div) % 3)
			div = (int(str_num1[i]) + div) // 3
	elif dot2 > dot1:
		for i in range(dot1 - 1, -1, -1):
			mod = (int(str_num2[dot2 - dot1 + i]) + int(str_num1[i]) + div) % 3
			div = (int(str_num1[i]) + int(str_num2[dot2 - dot1 + i]) + div) // 3
			result += str(mod)
		for i in range(dot2 - dot1 - 1, -1, -1):
			result += str((int(str_num2[i]) + div) % 3)
			div = (int(str_num2[i]) + div) // 3
	else:
		for i in range(dot1 - 1, -1, -1):
			mod = (int(str_num1[i]) + int(str_num2[dot2 - dot1 + i]) + div) % 3
			div = (int(str_num1[i]) + int(str_num2[dot2 - dot1 + i]) + div) // 3
			result += str(mod)
	if div:
		result += str(div)
	result = result[::-1]
	for i in range(len(result) - 1, -1, -1):
		if result[i] == '0':
			result = result[:i]
		else:
			break
	return result
def substraction(num1, num2):
	if num1 < 0:
		return str(-float(summary(-num1, num2)))
	elif num2 < 0:
		return str(-float(summary(num1, -num2)))
	sign = 0
	if num2 > num1:
		num2, num1 = num1, num2
		sign = -1
	str_num1 = str(num1)
	str_num2 = str(num2)
	dot1 = str_num1.index('.')
	dot2 = str_num2.index('.')
	result = str()
	if len(str_num1) - dot1 < len(str_num2) - dot2:
		for i in range(len(str_num1) - dot1, len(str_num2) - dot2):
			str_num1 += '0'
	else:
		for i in range(len(str_num2) - dot2, len(str_num1) - dot1):
			str_num2 += '0'
	str_num1 = str_num1[::-1]
	str_num2 = str_num2[::-1]
	lenmax = len(str_num1) if len(str_num1) < len(str_num2) else len(str_num2)
	div = 0
	i = 0
	for i in range(lenmax):
		if str_num1[i] == '.':
			result += '.'
		elif int(str_num1[i]) - div >= int(str_num2[i]):
			mod = int(str_num1[i]) - int(str_num2[i]) - div
			div = 0
			result += str(mod)
		else:
			mod = 3 + int(str_num1[i]) - int(str_num2[i]) - div
			div = 1
			result += str(mod)
	if i + 1 < len(str_num1):
		for j in range(i + 1, len(str_num1)):
			if int(str_num1[j]) - div >= 0:
				result += str(int(str_num1[j]) - div)
				div = 0
			else:
				result += str(int(str_num1[j]) - div + 3)
				div = 1
	elif i + 1 < len(str_num2):
		for j in range(i + 1, len(str_num2)):
			if int(str_num2[j]) - div >= 0:
				result += str(int(str_num2[j]) - div)
				div = 0
			else:
				result += str(int(str_num2[j]) - div + 3)
				div = 1
	if len(result):
		i = 0
		n = len(result)
		while i < n:
			if result[i] == '0':
				result = result[i + 1:]
				n -=1
			else:
				break
	if len(result):
		for i in range(len(result) - 1, -1, -1):
			if result[i] == '0':
				result = result[:i]
			else:
				break
	if not len(result):
		result = '0'
	if sign == -1:
		result += '-'
	return result[::-1]
def analyse_insert(input_window, calc):
	example = input_window.get()
	num1 = num2 = 0.0
	str_num1 = str()
	sign = 0
	error = 0
	for i in range(len(example)):
		if (example[i] >= '3' or example[i] < '0') and example[i] != '-' and example[i] != '+' and example[i] != '=' and example[i] != '.':
			error = 1
			break
		elif example[i] != '-' and example[i] != '+' and example[i] != '=':
			str_num1 += example[i]
		elif example[i] == '-':
			if sign == -1 and i - 1 >= 0:
				if example[i - 1] == '-':
					error = 3
					break
			try:
				if len(str_num1):
					num1 = float(str_num1)
				if sign == -1 and len(str_num1):
					num2 = float(substraction(num2, num1))
					str_num1 = str()
				elif len(str_num1):
					num2 = float(summary(num1, num2))
					str_num1 = str()
				sign = -1
			except BaseException:
				error = 2
				break
		elif example[i] == '+':
			if sign == 1 and i - 1 >= 0:
				if example[i - 1] == '+':
					error = 3
					break
			try:
				num1 = float(str_num1)
				if sign == -1:
					num2 = float(substraction(num2, num1))
					str_num1 = str()
				else:
					num2 = float(summary(num1, num2))
					str_num1 = str()
				sign = 1
			except BaseException:
				error = 2
				break
		elif example[i] == '=' and i == len(example) - 1:
			try:
				num1 = float(str_num1)
				if sign == -1:
					num2 = float(substraction(num2, num1))
					str_num1 = str()
				elif num2 < 0:
					num2 = float(substraction(num1, -num2))
				else:
					num2 = float(summary(num1, num2))
					str_num1 = str()
			except BaseException:
				error = 2
				break
		else:
			error = 3
			break
	if error == 1:
		box.showerror("Error", "Должны вводиться вещественные троичные числа (из цифр 0, 1 или 2).")
		return 0
	elif error == 2:
		box.showerror("Error", "Введен посторонний символ (помимо цифр допустимо вводить знаки '-', '+', '=', '.').")
		return 0
	elif error == 3:
		box.showerror("Error", "Введено два символа '-', '+' или '=' подряд или после знака равенства присутствуют посторонние символы")
		return 0
	else:
		result_output['text'] = str(num2)
def clean_f():
	#clean.config(state = NORMAL)
	input_window.delete(0, last = END)
	result_output['text'] = ''
def one_f():
	#one.config(state = NORMAL)
	input_window.insert('end', '1')
def two_f():
	#two.config(state = NORMAL)
	input_window.insert('end', '2')
def zero_f():
	#zero.config(state = NORMAL)
	input_window.insert('end', '0')
def plus_f():
	#plus.config(state = NORMAL)
	input_window.insert('end', '+')
def minus_f():
	# minus.config(state = NORMAL)
	input_window.insert('end', '-')
def dot_f():
	#dot.config(state = NORMAL)
	input_window.insert('end', '.')
def start_f():
	#start.config(state = NORMAL)
	input_window.insert('end', '=')
	if not analyse_insert(input_window, calc):
		return 0
def info():
	box.showinfo("Сведения о программе", "Приложение-калькулятор: сложение и вычитание в троичной системе счисления. Позволяет осуществлять ввод как с клавиатуры, так и с программного интерфейса. Автор: Михаил Коротыч, ИУ7-25Б.")
Main = Tk()
Main.title("Калькулятор троичной системы счисления.")
Main.geometry("245x185")
calc = Frame(Main)
calc.grid()
calc_1 = Frame(Main)
calc_1.grid()
calc_2 = Frame(Main)
calc_2.grid()
calc_3 = Frame(Main)
calc_3.grid()
result_output = Label(calc, text = '')
input_window = Entry(calc, width = 40)
input_window.pack(side = TOP)
result_output.pack(side = TOP)
main_menu = Menu(Main)
Main.config(menu = main_menu)
input_action = Menu(main_menu, tearoff = 0)
input_action.add_command(label = 'Сложение', command = plus_f)
input_action.add_command(label = 'Вычитание', command = minus_f)
main_menu.add_cascade(label = 'Добавить действие', menu = input_action)
main_menu.add_command(label = 'Вычислить', command = start_f)
main_menu.add_command(label = 'Очистить', command = clean_f)
main_menu.add_command(label = 'Сведения', command = info)
one = Button(calc_1, text = '1', background = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = one_f)
two = Button(calc_2, text = '2 ', background = '#c9c0bb', height = 2, width = 9, activebackground = '#80daeb', command = two_f)
two.pack(side = LEFT)
zero = Button(calc_1, text = '0', background = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = zero_f)
zero.pack(side = LEFT)
one.pack(side = LEFT)
plus = Button(calc_3, text = '+', bg = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = plus_f)
plus.pack(side = LEFT)
minus = Button(calc_3, text = '-', bg = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = minus_f)
minus.pack(side = LEFT)
start = Button(calc_3, text = '=', bg = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = start_f)
start.pack(side = BOTTOM)
dot = Button(calc_2, text = '.', bg = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = dot_f)
dot.pack(side = LEFT)
clean = Button(calc_1, text = 'C', bg = '#c9c0bb', height = 2, width = 4, activebackground = '#80daeb', command = clean_f)
clean.pack(side = LEFT)
Main.mainloop()