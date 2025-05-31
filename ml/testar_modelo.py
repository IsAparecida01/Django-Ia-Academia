# ml/testar_modelo.py

import pickle
import numpy as np

# Exemplo de entrada fictícia com os mesmos campos usados no treino
entrada = np.array([[1, 30, 3, 2, 0, 4, 1]])  # Exemplo: [genero, idade, frequencia, estacao, objetivo_alcancado, satisfacao, lesoes]

# Carrega o modelo treinado
with open('modelo_desistencia.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Faz a previsão
previsao = modelo.predict(entrada)

# Mostra o resultado
print("Previsão de desistência:", "Sim" if previsao[0] == 1 else "Não")
