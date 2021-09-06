#04/08/2021

from typing import List
from typing import Tuple

Vector = List[float]

#Exemplo de matriz

Matrix = List[List[float]]

A = [[1, 2, 3], #A tem 2 linhas e 3 colunas
	 [4, 5, 6]]
	 
B = [[1, 2],	#B Tem 3 linhas e 2 colunas
	 [3, 4],
	 [5, 6]]

def shape(A: Matrix) -> Tuple[int, int]:
	"""Retorna (nº de linhas de A, nº colunas de A)"""
	
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0	#Número de elementos da primeira linha
	return num_rows, num_cols

#print(shape([[1, 2, 3], [4, 5, 6]]))

def get_rows(A: Matrix, i: int) -> Vector:
	"""Retorna a linha i de A(como um Vector)"""
	return A[i]				#A[i] já está na linha i
	
def get_column(A: Matrix, j: int) -> Vector:
	"""Retorna a coluna j de A(como um Vector)"""
	return [A_i[j]			#elemento j da linha A_i
			for A_i in A]	#para cada linha A_i
			
#Criando matrizes
from typing import Callable

def make_matrix(num_rows: int,
				num_columns: int,
				entry_fn: Callable[[int, int], float]) -> Matrix:
		"""
		Retorna uma matriz com num_rows x num_columns
		cuja entrada (i,j) é entry_fn(i, j)
		"""
		
		return[[entry_fn(i, j)				#Com i, crie uma lista
				for j in range(num_columns)]#	[entry_fn(i, 0)...]
				for i in range(num_rows)]	# crie uma lista para cada i
				
#Criando a matriz identidade
def identity_matrix(n: int) -> Matrix:
	"""Retorna a matriz de identidade n x n"""
	return make_matrix(n,n, lambda i, j: 1 if i == j else 0)
	
print(identity_matrix(10))
