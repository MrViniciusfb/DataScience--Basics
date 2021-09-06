#28/07/2021

from matplotlib import pyplot as plt

variance = [1, 2, 4 , 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x,y in zip(variance, bias_squared)]	#Zip retorna uma lista de tuplas neste caso [(1, 246), (2, 128)]
xs = [i for i, _ in enumerate(variance)]						#Recebe um lista e enumera ela

#Podemos fazer múltiplas chamas para plt.plot
#para mostrar múltiplas séries no mesmo gráfico
plt.plot(xs, variance,	'g-', label='variance')		#Linha verde sólida
plt.plot(xs, bias_squared,	'r-.', label='bias^2')	#Linha vermalha de ponto tracejada
plt.plot(xs, total_error, 'b:', label='total error')#Linha pontilhada azul

#Como atribuímos rótulos a cada série,
#podemos criar uma legenda de graça(loc=9 means 'top center')
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The bias-Variance Tradeoff")
plt.show()
