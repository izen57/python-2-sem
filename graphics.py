import math
# Функция
def f(x: float):
	return math.sin(x)
# Производная
def df(x: float):
	return math.cos(x)
# Нахождения корня на интервале
def method(a, b, eps):
	x1 = a
	x2 = b
	i = 1
	# Проверка на наличие корня
	if f(x1) * f(x2) > 0:
		return -1, 0, 0
	# Проверка границ интервала
	if not f(x1):
		return 0, x1, i
	while abs(x2 - x1) > eps:
		if not df(x2) or not (f(x2) - f(x1)):
			return -3, 0, i
		x1 -= (x2 - x1) * f(x1) / (f(x2) - f(x1))
		x2 -= f(x2) / df(x2)
		i += 1
		if x2 > b or x2 < a:
			return -2, 0, i
	return 0, (x1 + x2) / 2, i
# Ввод данных
a = None
while a is None:
	try:
		a = float(input("Введите точку начала интервала: ").strip())
	except:
		print(end = "Некорректный ввод. ")
b = None
while b is None:
	try:
		b = float(input("Введите конечную точку интервала: ").strip())
	except:
		print(end = "Некорректный ввод. ")
	else:
		if b < a:
			b = None
			print("Конечная точка интервала должна быть больше начальной. ")
h = None
while h is None:
	try:
		h = float(input("Введите шаг разбиений: ").strip())
	except:
		print(end = "Некорректный ввод. ")
	else:
		if h > b - a:
			h = None
			print("Введённый шаг больше длины интервала.")
		elif h < 0:
			h = None
			print("Введённый шаг должен быть больше нуля.")
eps = None
while eps is None:
	try:
		eps = float(input("Введите точность: ").strip())
	except:
		print(end ="Некорректный ввод. ")
	else:
		if eps > h:
			eps = None
			print("Введённая точность больше шага разбиений.")
		elif eps < 0:
			eps = None
			print("Введённая точность должна быть больше нуля.")
i = 1
x1 = a
x2 = a + h
print("┌──────┬─────────────────────┬───────────┬──────────────┬───────────────┬──────┐")
print("│# инт.│      Интервал       │   Корень  │Значение ф-ции│Кол-во итераций│Ошибка│")
err = 0
k= float("-inf")
# основной цикл
while x1 < b:
	if err != -1:
		print("├──────┼─────────────────────┼───────────┼──────────────┼───────────────┼──────┤")
	err, k, iters = method(x1, x2, eps)
	if err <= -2:
		print("│{:6}│[{:9.2g};{:9.2g}]│           │              │              0│{:6}│".format(i, x1, x2, err))
	elif err != -1:
		print("│{:6}│[{:9.2g};{:9.2g}]│{:11g}│{:14.0e}│{:15}│      │".format(i, x1, x2, k, f(k), iters, err))
	# итерируем
	i += 1
	x1 = x2
	x2 += h
	if x2 > b:
		x2 = b
print("└──────┴─────────────────────┴───────────┴──────────────┴───────────────┴──────┘")
print("Ошибка -2 : Выход за пределы интервала при нахождении касательной")
print("Ошибка -3 : Деление на ноль")