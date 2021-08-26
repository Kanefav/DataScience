import sklearn.svm as sk
from sklearn.metrics import accuracy_score

maquina = sk.LinearSVC()


#Voa #Cava #Nada #Anda
# 0 não, 1 sim

#voadores
exemplo1 = [1, 0, 0, 0]
exemplo2 = [1, 0, 0, 1]
#terrestres
exemplo3 = [0, 0, 1, 1]
exemplo4 = [0, 1, 0, 1]

exemplos = [exemplo1, exemplo2, exemplo3, exemplo4]
# 0 voador, 1 terrestre
respostas = [0, 0, 1, 1]
maquina.fit(exemplos, respostas)

teste1 = [1, 0, 1, 0] #V
teste2 = [1, 0, 1, 1] #V
teste3 = [0, 1, 1, 1] #T
teste4 = [1, 0, 1, 1] #V
testes = [teste1, teste2, teste3, teste4]
tentativa1 = maquina.predict(testes)
print(tentativa1)
print(accuracy_score(respostas, tentativa1)*100, end='%\n')
 