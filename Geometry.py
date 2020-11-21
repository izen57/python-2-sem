from tkinter import *
from tkinter import messagebox
from math import sqrt, acos, degrees
y_coordinates = []
x_coordinates = []
#очистка холста
def clear():
	canva.delete("all")
	x_coordinates.clear()
	y_coordinates.clear()
#Добавление точки рисунком
def paint(event):
	x, y = (event.x), (event.y)
	canva.create_oval(x, y, x, y, width = 0, fill = "red")
	x_coordinates.append(x)
	y_coordinates.append(y)
#Ручное добавление точки
def add_point():
	try:
		x = float(X.get())
		y = float(Y.get())
		if x > 660 or x < 0 or y > 300 or y < 0:
			messagebox.showerror('Ошибка', 'Некорректный ввод')
		canva.create_oval(x, y, x, y, width = 0, fill = "red")
		x_coordinates.append(x)
		y_coordinates.append(y)
	except ValueError:
		messagebox.showerror('Ошибка', 'Некорректный ввод')
#Поиск вершин треугольника
def find_triangle():
	n = len(x_coordinates)
	if n <= 2 or (n == 3 and (x_coordinates[0] == x_coordinates[1] == x_coordinates[2] or y_coordinates[0] == y_coordinates[1] == y_coordinates[2])):
		messagebox.showerror('Ошибка', 'Введено недостаточно точек или все точки лежат на одной прямой')
	else:
		#canva.delete("all")
		max_angle = 0
		x1 = y1 = x2 = y2 = x3 = y3 = 0
		for i in range(n - 2):
			for j in range(i + 1, n - 1):
				for k in range(j + 1, n):
					a = sqrt((x_coordinates[i] - x_coordinates[j]) ** 2 + (y_coordinates[i] - y_coordinates[j]) ** 2)
					b = sqrt((x_coordinates[j] - x_coordinates[k]) ** 2 + (y_coordinates[j] - y_coordinates[k]) ** 2)
					c = sqrt((x_coordinates[i] - x_coordinates[k]) ** 2 + (y_coordinates[i] - y_coordinates[k]) ** 2)
					angle1 = degrees(acos((b * b + c * c - a * a) / (2 * b * c)))
					angle2 = degrees(acos((a * a + c * c - b * b) / (2 * a * c)))
					angle3 = 180.0 - angle1 - angle2
					if angle1 >= 175.0 or angle2 >= 175.0 or angle3 >= 175.0:
						continue
					if angle1 > max_angle and angle1 > angle2 and angle1 > angle3:
						max_angle = angle1
						x1 = x_coordinates[i]
						y1 = y_coordinates[i]
						x2 = x_coordinates[j]
						y2 = y_coordinates[j]
						x3 = x_coordinates[k]
						y3 = y_coordinates[k]
					elif angle2 > max_angle and angle2 > angle1 and angle2 > angle3:
						max_angle = angle2
						x1 = x_coordinates[i]
						y1 = y_coordinates[i]
						x2 = x_coordinates[j]
						y2 = y_coordinates[j]
						x3 = x_coordinates[k]
						y3 = y_coordinates[k]
					elif angle3 > max_angle and angle3 > angle2 and angle3 > angle1:
						max_angle = angle3
						x1 = x_coordinates[i]
						y1 = y_coordinates[i]
						x2 = x_coordinates[j]
						y2 = y_coordinates[j]
						x3 = x_coordinates[k]
						y3 = y_coordinates[k]
	canva.create_polygon(x1, y1, x2, y2, x3, y3, fill = 'white', outline = 'blue')
root = Tk()
root.title("Задача с треугольником")
root.geometry('700x600')
text_1 = Label(text = "Поиск треугольника, построенного на точках, в котором самый большой угол.")
text_1.pack(side = TOP)
X = Entry()
X.place(x = 160, y = 100, width = 100, height = 30)
Y = Entry()
Y.place(x = 160, y = 150, width = 100, height = 30)
text_x = Label(text = "x = ")
text_x.place(x = 120, y = 100)
text_y = Label(text = "y = ")
text_y.place(x = 120, y = 150)
point = Button(text = "Добавить точку", command = add_point)
point.place(x = 115, y = 210, width = 150, height = 50)
triangle = Button(text = "Найти и построить треугольник", command = find_triangle)
triangle.place(x = 320, y = 210, width = 300, height = 50)
clear = Button(text = "Очистить холст", command = clear)
clear.place(x = 320, y = 120, width = 300, height = 50)
canva = Canvas(width = 660, height = 300, bg = "white")
canva.place(x = 20, y = 280)
canva.bind("<Button-1>", paint)
mainloop()