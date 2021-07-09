import sklearn.svm as sk
from sklearn.metrics import accuracy_score
# tem pelo? 
# perna longa?
# late?
# 0, 1 : nao, sim
cachorro1 = [1, 1, 1]
cachorro2 = [1, 0, 1]

gato1 = [1, 0, 0] 
gato2 = [1, 1, 0]

treino_x = [cachorro1,  cachorro2, gato1, gato2]
treino_y = [0, 0, 1, 1] # 0 - cachorro : 1 - gato

modelo = sk.LinearSVC()
modelo.fit(treino_x, treino_y)
animal_misterioso = [0, 1, 0]
tentativa = modelo.predict([animal_misterioso])
if tentativa == 0:
    print('Cachorro')
if tentativa == 1:
    print('Gato')

misterio1 = [1, 0, 1]
misterio2 = [0, 1, 1]
misterio3 = [0, 0, 0]

teste = [misterio1, misterio2, misterio3]
resposta = [0, 0, 1]

tentativa2 = modelo.predict(teste)
print(tentativa2)
print(accuracy_score(resposta, tentativa2)*100)
#exemplo simples, não é normal a presição ficar em mais de 90% pra maioria dos casos