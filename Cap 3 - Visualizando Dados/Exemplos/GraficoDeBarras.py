from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#Plote as barras com coordenadas x à esquerda [0, 1, 2, 3, 4], alturas[num_oscaras]
plt.bar(range(len(movies)), num_oscars)

plt.title("My favorites Movies")	#adiciona um título
plt.ylabel("Nº of Oscars")	#rotule o eixo y

#Rotule o eixo x com os nomes dos filmes no centro das barras
plt.xticks(range(len(movies)), movies)

plt.show()
