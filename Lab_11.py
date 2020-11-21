#Программа Михаила Коротыча (ИУ7-25Б) для уточнения корней
def f(x): #Функция
	return x * x - 4
def df(x): #Первая производная
	return 2 * x
def d2f(x): #Вторая производная
	return 2
def gr(): #График
	import matplotlib.pyplot as plt
	x1 = np.linspace(start.get(), end.get(), 10 ** 6, dtype = float)
	y1 = [f(el) for el in x1]
	x2, y2 = [], []
	for el in x1:
		if np.fabs(d2f(el)) <= 1e-3:
			x2.append(el)
			y2.append(f(el))
	plt.plot(x1, y1, x1, np.zeros(10 ** 6, dtype = float), 'r', x2, y2, 'gs')
	plt.legend('f(x)', 'Ось абсцисс', 'Точки перегиба')
	plt.grid(b = True)
	plt.show()
def method(start, end, eps):
	x1 = start
	x2 = end - 0.00001
	i = 1
	# Проверка на наличие корня
	if f(x1) * f(x2) > 0.0:
		return -1, 0, 0
	# Проверка границ интервала
	if not f(x1):
		return 0, x1, i
	while np.fabs(x2 - x1) > eps:
		if not df(x2) or not f(x2) - f(x1):
			return -3, 0, i
		x1 -= (x2 - x1) * f(x1) / (f(x2) - f(x1))
		x2 -= f(x2) / df(x2)
		i += 1
		if x2 > end or x2 < start:
			return -2, 0, i
	return 0, (x1 + x2) / 2, i
def table():
	i = 1
	a = start.get()
	b = end.get()
	h = step.get()
	x1 = a
	x2 = a + h
	head = "         №                       Интервал                                  Корень          Значение ф-ции    Кол-во итераций Ошибка\n"
	err = 0
	k = float("-inf")
	# основной цикл
	while x1 < b:
		if err != -1:
			head += "\n"
		err, k, iters = method(x1, x2, eps.get())
		if err <= -2:
			head += "           {:^7}[{:^28.2g};{:^25.2g}]              -                                                                                            {:<7}\n".format(i, x1, x2, -err)
			i += 1
		elif err != -1:
			head += "           {:^7}[{:^28.2g};{:^25.2g}]{:^30.5f}{:<35.0e}       {:<7}\n".format(i, x1, x2, k, f(k), iters, -err)
			i += 1
		x1 = x2
		x2 += h
		if x2 > b:
			x2 = b
	head += "\nОшибка 2: Выход за пределы интервала при нахождении касательной;\nОшибка 3: Деление на ноль."
	return head
def chart():
	output_window = Tk()
	output_window.title('Таблица корней')
	label = Label(master = output_window, text = table(), justify = LEFT)
	label.place(relx = 0.1, rely = 0.1)
	output_window.mainloop()
from tkinter import *
from tkinter import messagebox
import numpy as np
input_window = Tk()
input_window.title('Ввод')
input_window.geometry('300x170')
start = DoubleVar()
end = DoubleVar()
step = DoubleVar()
eps = DoubleVar()
#Поле ввода начала отрезка
start_entry = Entry(input_window, textvariable = start)
start_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
#Поле ввода конца отрезка
end_entry = Entry(input_window, textvariable = end)
end_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
#Поле ввода шага
step_entry = Entry(input_window, textvariable = step)
step_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
#Поле ввода точности
eps_entry = Entry(input_window, textvariable = eps)
eps_entry.grid(row = 3, column = 1, padx = 5, pady = 5)
#Текстовая метка начала отрезка
start_label = Label(input_window, text = 'Введите начало отрезка:')
start_label.grid(row = 0, column = 0, sticky = 'w')
#Текстовая метка конца отрезка
end_label = Label(input_window, text = 'Введите конец отрезка:')
end_label.grid(row = 1, column = 0, sticky = 'w')
#Текстовая метка шага
step_label = Label(input_window, text = 'Введите шаг:')
step_label.grid(row = 2, column = 0, sticky = 'w')
#Текстовая метка точности
eps_label = Label(input_window, text = 'Введите точность:')
eps_label.grid(row = 3, column = 0, sticky = 'w')
#Кнопки
btn1 = Button(input_window, text = 'Вывести таблицу', command = chart)
btn2 = Button(input_window, text = 'Вывести график', command = gr)
btn1.place(relx = 0.5, rely = 0.7)
btn2.place(relx = 0.1, rely = 0.7)
input_window.mainloop()