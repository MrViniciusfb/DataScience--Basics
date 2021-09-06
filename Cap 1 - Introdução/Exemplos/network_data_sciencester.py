#18/07/2021 , fisrt lesson

#Lista de usuários
users = [
	{"id": 0, "name": "Hero"},
	{"id": 1, "name": "Dunn"},
	{"id": 2, "name": "Sue"},
	{"id": 3, "name": "Chi"},
	{"id": 4, "name": "Thor"},
	{"id": 5, "name": "Clive"},
	{"id": 6, "name": "Hicks"},
	{"id": 7, "name": "Devin"},
	{"id": 8, "name": "Kate"},
	{"id": 9, "name": "Kelin"}
]

#Lista de amizades
friendship_pairs = [(0, 1),(0, 2),(1, 2),(1, 3),(2, 3),(3, 4),
					(4, 5),(5, 6),(5, 7),(6, 8),(7, 8),(8, 9)]
					
#Modo mais eficiente
	#Inicializa o dict com uma lista vazia para cada id de usuário:
friendships = {user["id"]: [] for user in users}

#Em seguida,execute um loop pelos pares de amigos para preenchê-la:
for i,j in friendship_pairs:
	friendships[i].append(j) #Adiciona j como amigo do usuário i
	friendships[j].append(i) #Adiciona i como amigo do usuário j

def number_of_friends(user):
	"""Quantos amigos tem o _user_?"""
	user_id = user["id"]
	friend_ids = friendships[user_id]
	return len(friend_ids)

total_connections = sum(number_of_friends(user)
					for user in users)			#24

num_users = len(users)							#Tamanho da lista de usuário
avg_connections = total_connections / num_users	#24 / 10 = 2.4

#Crie uma lista (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
					for user in users]

num_friends_by_id.sort(									#Classifique a lista
		key=lambda id_and_friends: id_and_friends[1],	#por num_friends
		reverse=True)									#do maior para o menor

print(num_friends_by_id)

def foaf_ids_bad(user):
	'''foaf significa "friend of a friend"'''
	return[foaf_id
			for friend_id in friendships[user["id"]]
			for foaf_id in friendships[friend_id]]


from collections import Counter						#Não é carregado padrão

def friends_of_friends(user):
	user_id = user["id"]
	return Counter(
			foaf_id
			for friend_id in friendships[user_id]	#Para cada amigo meu
			for foaf_id in friendships[friend_id]	#encontre os amigos deles
			if foaf_id != user_id					#que não sejam eu
			and foaf_id not in friendships[user_id]	#e não sejam meus amigos
)
print(friends_of_friends(users[3]))					#Counter({0: 2, 5: 1})

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
#Funciona mas precisa rodar toda vez para descobrir os interesses
def data_scientists_who_like(target_interest):
	'''Encontre os ids dos usuários com o mesmo interesse'''
	return[user_id
			for user_id,user_interest in interests
			if user_interest == target_interest]
	
from collections import defaultdict

#As chaves são interessantes,os valores são listas de user_ids com o interesse em questão
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

for user_id, interest in interests:
	user_ids_by_interest[user_id].append(interest)

#Dar uma olhada abaixo
def most_common_interest_with(user):
	return Counter(
		interested_user_id
		for interest in interests_by_user_id[user['id']]
		for interested_user_id in user_ids_by_interest[interest]
		if interested_user_id !=['id']
	)
