from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("Nº de vezes em que ouvi alguém, dizer 'data science'")

#Se vocÊ fizer isso, matplotlib rotulará o eixo x como 0, 1
#e adicionará um +2.013e3 off no canto
plt.ticklabel_format(useOffset=False)

#O eixo y malandro mostra apenas a parte acima de 500
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Observe esse 'grande' aumento!")

plt.axis([2016.5, 2018.5, 0, 506])
plt.title("Não tão grandem mais!")
plt.show()
