def f(x):
	return np.sin(x) - x / 4
def solution(): #График
	from matplotlib import pyplot as plt
	global start, end, step, eps
	xlist = np.linspace(start.get(), end.get(), 1000, dtype = float)
	ylist1 = [f(x) for x in xlist]
	ylist2 = np.zeros(1000, dtype = float)
	plt.plot(xlist, ylist1)
	plt.plot(xlist, ylist2, color = 'r')
	plt.grid(b = True)
	plt.show()
from tkinter import *
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
#Кнопка
btn = Button(input_window, text = 'Решить', command = solution)
btn.place(relx = 0.4, rely = 0.7)
input_window.mainloop()