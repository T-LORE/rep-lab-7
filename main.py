import numpy as np
# Commit 3: 1 line
def getMatrix():
	matrix = []
    # Commit 1: 1 line # Commit 5: 1 line
    # Commit 1: 2 line
    # Commit 3: 2 line
	try:
		''' Размеры матрицы '''
		rows = int(input("Введите число строк в матрице: "))
		cols = int(input("Введите число столбцов в матрице: "))
		if(rows <= 0 or cols <= 0):
			raise ValueError("Неверные размеры матрицы.")

		''' Значения матрицы '''
		print("Введите элементы матрицы по одному, разделяя их пробелом")
		for i in range(rows):
			while True:
				row = input(f"Строка {i + 1}: ").split(" ")
				if len(row) != cols:
						raise ValueError("Неверное количество элементов. Пожалуйста, повторите ввод.")
				row = [int(x) for x in row]
				matrix.append(row)
				break

	except ValueError as exception:
			print(f"Ошибка: {exception}")
    # Commit 5: 2 line
	return matrix
    # Commit 1: 3 line
def getRiskMatrix(matrix):
	riskMatrix = []

	for j in range(len(matrix[0])):  # Перебираем столбцы матрицы
			beta = max(matrix[i][j] for i in range(len(matrix)))  # Максимальное значение в столбце
			# if beta >= 0:  # Если это выигрыш
			risk_col = [beta - matrix[i][j] for i in range(len(matrix))]
			# else:  # Если это потеря
			# 		beta = min(matrix[i][j] for i in range(len(matrix)))  # Минимальное значение в столбце
			# 		risk_col = [matrix[i][j] - beta for i in range(len(matrix))]
			riskMatrix.append(risk_col)
   
	# Commit 5: 3 line
	return np.transpose(riskMatrix)
    # Commit 3: 3 line
def waldCriterion(matrix, matrixType):
	if(matrixType == 1):
		maxValues = np.max(matrix, axis=0)
		waldValue = np.min(maxValues)
  
	if(matrixType == 2):
		minValues = np.min(matrix, axis=0)
		waldValue = np.max(minValues)
    # Commit 2: 1 line
	return waldValue

def savageCriterion(riskMatrix):
	maxValues = np.max(riskMatrix, axis=1)
	savageValue = np.min(maxValues)
    # Commit 2: 2 line
    # Commit 2: 3 line
	return savageValue
    # Commit 6: 1 line
def hurwitczCriterion(matrix, matrixType, prob):
	if(matrixType == 1):
		hurwitczValue = np.max(prob*np.min(matrix, axis=1) + (1-prob)*np.max(matrix, axis=1))
    # Commit 6: 2 line
	if(matrixType == 2):
		hurwitczValue = np.min(prob*np.max(matrix, axis=1) + (1-prob)*np.min(matrix, axis=1))
    # Commit 6: 3 line
	return hurwitczValue

''' Получить данные от пользователя '''
''' Тип матрицы '''
# Commit 4: 1 line
print("Что у вас за матрица?")
matrixType = int(input("1 - матрица выигрышей\n2 - матрица потерь (затрат)\n"))

''' Сама матрица '''
matrix = np.array(getMatrix())
# Commit 4: 2 line
''' Степень пессимизма для критерия Гурвица '''
prob = float(input("Введите степень пессимизма для критерия Гурвица: "))
if(prob < 0 or prob > 1): 
  raise ValueError("Степень пессимизма должна находиться в диапазоне (0;1)")
# Commit 4: 3 line
''' Вычисления '''
''' Матрица рисков '''
riskMatrix = getRiskMatrix(matrix)
print(f"\n\nРезультаты вычислений:\nМатрица рисков:\n{riskMatrix}")

''' Критерий Вальда '''
waldValue = waldCriterion(matrix, matrixType)
print(f"\nКритерий Вальда: {waldValue}")

''' Критерий Сэвиджа '''
savageValue = savageCriterion(riskMatrix)
print(f"\nКритерий Сэвиджа: {savageValue}")

''' Критерий Гурвица '''
hurwitczValue = hurwitczCriterion(matrix, matrixType, prob)
print(f"\nКритерий Гурвица: {hurwitczValue}")
