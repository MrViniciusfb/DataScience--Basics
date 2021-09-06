#28/07/2021

from matplotlib import pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#Rotule cada ponto
for label, friend_count, minute_count in zip(labels, friends, minutes): #Tupla com três valores
	plt.annotate(label,
		xy=(friend_count, minute_count),	#Coloque o rótulo no respectivo ponto
		xytext=(5, -5),						#mas levemente descolado
		textcoords='offset points'
	)
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("Nº of Friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
