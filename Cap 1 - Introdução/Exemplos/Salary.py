#21/07/2021

from collections import defaultdict

salaries_and_tenures = [(83000,8.7),(88000,8.1),
						(48000,0.7),(76000,6),
						(69000,6.5),(76000,7.5),
						(60000,2.5),(83000,10),
						(48000,1.9),(63000,4.2)]
						
#As chaves são anos, os valore são listas de salários por anos de experiência
salary_by_tenures = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	salary_by_tenures[tenure].append(salary)

#As chaves são anos, cada valor é o salário médio associado ao número de anos de experiencia
average_salary_by_tenure = {			#Não é muito útil pq não temos pessoas
	tenure:sum(salaries)/len(salaries)	#com a mesma experiência
	for tenure, salaries in salary_by_tenures.items()
}
#Função para atribuir a experiencia
def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else:
		return "more than five"
		
#AS chaves são buckets de anos de experiÊncia, os valores são as listas de 
#salários associados ao bucket em questão.
salary_by_tenures_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenures_bucket[bucket].append(salary)

#As chaves são buckets de anos de experiência, os valores são a média salarial
#do bucket em questão
average_salary_by_bucket = {
	tenure_bucket: sum(salaries)/len(salaries)
	for tenure_bucket, salaries in salary_by_tenures_bucket.items()
}

print(average_salary_by_bucket)

def predict_paid_or_unpaid(years_experience):
	if years_experience < 3.0:
		return "paid"
	elif years_experience < 8.5:
		return "unpaid"
	else:
		return "paid"

