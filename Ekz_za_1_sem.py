def sort(a, m):
	summ = 0
	for i in range(len(a)):
		summ += a[i][m]
	return summ
len_str = int(input(('Введите кол-во строк матрицы:')))
len_stb = int(input(('Введите кол-во столбцов матрицы:')))
arr = [0] * len_str
for i in range(len_str):
	arr[i] = [0] * len_stb
	for j in range(len_stb):
		arr[i][j] = float(input('Введите элемент матрицы:'))
for i in range(len_str):
	print(arr[i])
for i in range(len_stb - 1):
	if sort(arr, i) > sort(arr, i + 1):
		for j in range(len_str):
			arr[j][i], arr[j][i + 1] = arr[j][i + 1], arr[j][i]
for i in range(len_str):
	print(arr[i])