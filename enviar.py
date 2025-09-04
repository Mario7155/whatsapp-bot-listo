import pandas as pd
import requests
import os
import time

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("No se encontró API_KEY")

# 🔹 URL pública del Excel
EXCEL_URL = "https://drive.google.com/uc?export=download&id=mensajes.xlsx"
df = pd.read_excel(EXCEL_URL)

# ⚡ Evitar duplicados
df = df.drop_duplicates(subset=["numero"])

url = "https://wasenderapi.com/api/send-message"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

enviados = set()
for _, row in df.iterrows():
    numero = str(row["numero"])
    mensaje = str(row["mensaje"])
    if numero in enviados:
        continue
    payload = {"to": numero, "text": mensaje}
    response = requests.post(url, json=payload, headers=headers)
    print(f"✅ Enviado a {numero}: {response.text}")
    enviados.add(numero)
    time.sleep(60)
