# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
	"""docstring for Point"""
	
	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.perimeter = ((x1-x2)**2 + (y1-y2)**2)**0.5 + ((x1-x3)**2 + (y1-y3)**2)**0.5 + ((x2-x3)**2 + (y2-y3)**2)**0.5
		if self.perimeter == 0:
			print('Невозможно построить треугольник')
			exit(1)

	def get_area(self):
		area = math.fabs(((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)))/2
		return area

	def get_perimeter(self):
		return self.perimeter



	
		
x1 = int(input('Введите X1: '))	
y1 = int(input('Введите Y1: '))	
x2 = int(input('Введите X2: '))	
y2 = int(input('Введите Y2: '))	
x3 = int(input('Введите X3: '))	
y3 = int(input('Введите Y3: '))	

triangle = Triangle(x1,y1,x2,y2,x3,y3)



print('Площадь треугольника:')
print(triangle.get_area())
print('периметр треугольника:')
print(triangle.get_perimeter())
