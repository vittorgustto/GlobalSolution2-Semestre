from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [30, 60], [35, 55], [40, 50], [38, 52], [32, 65],
    [42, 45], [28, 70], [37, 50], [39, 48], [31, 68]
])
y = np.array([0, 1, 2, 2, 0, 2, 0, 1, 2, 0])

model = DecisionTreeClassifier()
model.fit(X, y)

nova_leitura = np.array([[39, 47]])
risco = model.predict(nova_leitura)[0]

status = ["Temperatura segura", "Risco moderado", "ALERTA DE CALOR!"]
print("Resultado:", status[risco])
