from matplotlib import pyplot as plt
from collections import Counter #Notar, Counter cria um dicionário 

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

#Agrupe as notas por decil, mas coloque o 100 com o 90
histogram = Counter(min((grade // 10) * 10, 90) for grade in grades) 	#Notar, 10 * 10 não é 100 e // retorna divisão intera
print(histogram)																	#min retorna o valor minimo, se for maior que 90 retorna 90
plt.bar([ x + 5 for x in histogram.keys()],	#Mova as barras para a direita em 5
		histogram.values(),					#Atribuça a ltura correta a cada barra
		10,									#Atribua a largura 10 a cada barra
		edgecolor = (0, 0, 0))				#Escureça as bordas da barra

plt.axis([-5, 105, 0, 5])					#Eixo x de -5 a 105
											#Eixo y de 0 a 5
											
plt.xticks([10 * i for i in range(11)])		#Rótulos do eixo x 0,10...,100
plt.xlabel("Nota")							
plt.ylabel("Nº de Alunos")
plt.title("Distribuição das Notas da 1ª Avaliação")
plt.show()

