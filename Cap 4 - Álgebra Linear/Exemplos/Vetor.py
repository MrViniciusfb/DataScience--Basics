from typing import List

Vector = List[float]
height_weight_age = [70, #Polegadas
					170, #Libras
					70 ] #anos
grades = [95,	#Teste 1
		  80,	#Teste 2
		  75,	#Teste 3
		  62]	#Teste 4
		  
def add(v: Vector, w: Vector) -> Vector:
	"""Soma os elementos correspondentes"""
	assert len(v) == len(w), "vectors must be the same lenght"
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
	"""Subtrai os elementos correspondentes"""
	assert len(v) == len(w), "vectors must be the same lenght"
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
	"""Soma todos os elementos correspondentes"""
	#Verifica se os vetores não estão vazios
	assert vectors, "no vectors provided!"
	
	#Verifique se os vetores são do mesmo tamanho
	num_elements = len(vectors[0])
	assert all(len(v) == num_elements for v in vectors), "different sizes!"
	
	#o elemento de nº i do resultado é a soma de todo vector[i]
	return[sum(vector[i] for vector in vectors)
			for i in range(num_elements)]
		
def scalar_multiply(c: float, v: Vector) -> Vector:
	"""Multiplica cada elemento por c"""
	return[c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector: #Mean = média
	"""Computa a média dos elementos"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))
	
#Dot product = produto escalar

def dot(v: Vector, w: Vector) -> float:
	"""Computa o produto vetorial"""
	assert len(v) == len(w), "vectors must be same lenght"
	
	return sum(v_i*w_i for v_i,w_i in zip(v, w))
	
def sum_of_squares(v: Vector) -> float:
	""""Retorna a soma dos quadrados"""
	return dot(v, v)

import math

def squared_distance(v: Vector, w: Vector) -> float:
	"""Computa o quadrado a diferença entre dois vetores"""
	return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
	"""Computa a distancia entre dois vetores"""
	return math.sqrt(squared_distance(v, w))

	
	
