def sorting(a):
	b = timeit.default_timer()
	for i in range(1, len(a)):
		j = i - 1
		key = a[i]
		while a[j] > key and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	return timeit.default_timer() - b
def chart():
	fig, ax = plt.subplots()
	x = np.linspace(start.get(), end.get(), 10, dtype = int)
	mas = [np.random.random_integers(-100, 100, el) for el in x]
	ax.plot(x, [sorting(el) for el in mas], 'o')
	ax.grid(which = 'major', color = 'k')
	ax.minorticks_on()
	ax.xaxis.set_minor_locator(tck.MultipleLocator(20))
	ax.yaxis.set_major_locator(tck.MultipleLocator(0.02))
	ax.yaxis.set_minor_locator(tck.MultipleLocator(0.01))
	ax.grid(which = 'minor', color = 'gray', linestyle = ':')
	ax.set_xlabel('Количество элементов массива, шт.')
	ax.set_ylabel('Время, с')
	plt.show()
def table():
	table_window = Tk()
	table_window.title('Таблица')
	head12 = Label(table_window, text = 'Упорядоченный массив')
	head12.grid(column = 1, row = 2)
	head13 = Label(table_window, text = 'Случайный массив')
	head13.grid(column = 1, row = 3)
	head14 = Label(table_window, text = 'Упорядоченный в обратном порядке')
	head14.grid(column = 1, row = 4)
	head21 = Label(table_window, text = N1.get())
	head21.grid(column = 2, row = 1)
	head31 = Label(table_window, text = N2.get())
	head31.grid(column = 3, row = 1)
	head41 = Label(table_window, text = N3.get())
	head41.grid(column = 4, row = 1)
	sort1 = sorted(np.random.random_integers(-100, 100, N1.get()))
	t1 = Label(table_window, text = sorting(sort1))
	t1.grid(column = 2, row = 2)
	sort2 = sorted(np.random.random_integers(-100, 100, N2.get()))
	t2 = Label(table_window, text = sorting(sort2))
	t2.grid(column = 3, row = 2)
	sort3 = sorted(np.random.random_integers(-100, 100, N3.get()))
	t3 = Label(table_window, text = sorting(sort3))
	t3.grid(column = 4, row = 2)
	ran1 = np.random.random_integers(-100, 100, N1.get())
	t4 = Label(table_window, text = sorting(ran1))
	t4.grid(column = 2, row = 3)
	ran2 = np.random.random_integers(-100, 100, N2.get())
	t5 = Label(table_window, text = sorting(ran2))
	t5.grid(column = 3, row = 3)
	ran3 = np.random.random_integers(-100, 100, N3.get())
	t6 = Label(table_window, text = sorting(ran3))
	t6.grid(column = 4, row = 3)
	rev1 = sorted(np.random.random_integers(-100, 100, N1.get()), reverse = True)
	t7 = Label(table_window, text = sorting(rev1))
	t7.grid(column = 2, row = 4)
	rev2 = sorted(np.random.random_integers(-100, 100, N2.get()), reverse = True)
	t8 = Label(table_window, text = sorting(rev2))
	t8.grid(column = 3, row = 4)
	rev3 = sorted(np.random.random_integers(-100, 100, N3.get()), reverse = True)
	t9 = Label(table_window, text = sorting(rev3))
	t9.grid(column = 4, row = 4)
def test_sorting():
	a = no_sort_list.get().split()
	[float(a[i]) for i in range(1, len(a))]
	for i in range(1, len(a)):
		j = i - 1
		key = a[i]
		while a[j] > key and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	sorted_list_entry.insert(0, a)
from tkinter import *
import matplotlib.pyplot as plt, matplotlib.ticker as tck, numpy as np, timeit
main_window = Tk()
main_window.title('Метод простых вставок')
main_window.geometry('700x700')
non_sorted_list_label = Label(text = 'Неотсортированный список', relief = GROOVE)
non_sorted_list_label.place(x = 5, y = 10, height = 20, width = 175)
no_sort_list = StringVar()
non_sorted_list_entry = Entry(textvariable = no_sort_list)
non_sorted_list_entry.place(x = 5, y = 35, height = 20, width = 175)
sorted_list_label = Label(text = 'Отсортированный список', relief = GROOVE)
sorted_list_label.place(x = 270, y = 10, height = 20, width = 175)
sorted_list_entry = Entry()
sorted_list_entry.place(x = 270, y = 35, height = 20, width = 175)
test = Button(text = 'Тест', command = test_sorting)
test.place(x = 200, y = 20, height = 20, width = 50)
N1_label = Label(text = 'N1 =')
N1_label.place(x = 5, y = 60)
N1 = IntVar()
N1_entry = Entry(textvariable = N1)
N1_entry.place(x = 45, y = 60, height = 20, width = 35)
N2_label = Label(text = 'N2 =')
N2_label.place(x = 5, y = 85)
N2 = IntVar()
N2_entry = Entry(textvariable = N2)
N2_entry.place(x = 45, y = 85, height = 20, width = 35)
N3_label = Label(text = 'N3 =')
N3_label.place(x = 5, y = 110)
N3 = IntVar()
N3_entry = Entry(textvariable = N3)
N3_entry.place(x = 45, y = 110, height = 20, width = 35)
table_btn = Button(text = 'Таблица', command = table)
table_btn.place(x = 5, y = 135)
gr = Button(text = 'График', command = chart)
gr.place(x = 130, y = 135)
from_label = Label(text = 'От')
from_label.place(x = 100, y = 60)
start = IntVar()
from_entry = Entry(textvariable = start)
from_entry.place(x = 130, y = 60, height = 20, width = 35)
to_label = Label(text = 'До')
to_label.place(x = 100, y = 85)
end = IntVar()
to_entry = Entry(textvariable = end)
to_entry.place(x = 130, y = 85, height = 20, width = 35)
main_window.mainloop()