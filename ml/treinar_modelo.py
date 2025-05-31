import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
import pickle

df = pd.read_csv('dados_clientes.csv')


le_genero = LabelEncoder()
df['genero'] = le_genero.fit_transform(df['genero'])  

le_estacao = LabelEncoder()
df['estacao'] = le_estacao.fit_transform(df['estacao']) 

X = df[['genero', 'idade', 'frequencia', 'estacao', 'objetivo_alcancado', 'satisfacao', 'lesoes']]
y = df['desistiu']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

df = df.dropna(subset=['desistiu'])  

 
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(modelo, 'modelo_desistencia.pkl')
print("Modelo salvo como modelo_desistencia.pkl")

with open('modelo_desistencia.pkl', 'wb') as f:
    pickle.dump(modelo, f)
    