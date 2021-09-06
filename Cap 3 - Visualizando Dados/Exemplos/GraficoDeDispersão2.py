#28/07/2021

from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [ 100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades) #scatter = dispersão
plt.axis("equal")	#Se você não fizer isso o matplotlib pode não deixar o gráfico comparável
plt.title("Axes Aren't Comparable")
plt.xlabel("Test 1 grande")
plt.ylabel("Test 2 grade")
plt.show()

