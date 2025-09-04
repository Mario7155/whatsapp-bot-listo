import os
import pandas as pd
import requests
import time

# 🔹 API_KEY desde variables de entorno (Railway) o en local
API_KEY = ""os.getenv("API_KEY") or "TU_API_KEY_AQUI"""

API_URL = "https://wasenderapi.com/api/send-message"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# 🔹 Leer Excel local (si luego lo pasas a URL, se cambia aquí)
df = pd.read_excel("mensajes.xlsx")

# ✅ Eliminar duplicados basados en la columna "numero"
df = df.drop_duplicates(subset=["numero"])

# 🔹 Validar que existan las columnas correctas
if "numero" not in df.columns or "mensaje" not in df.columns:
    print("❌ El Excel debe tener las columnas: numero, mensaje")
    exit()

# 🔹 Enviar mensajes
for index, row in df.iterrows():
    numero = str(row["numero"])
    mensaje = str(row["mensaje"])
    payload = {"to": numero, "text": mensaje}

    response = requests.post(API_URL, json=payload, headers=headers)
    print(f"Enviado a {numero}: {response.text}")

    # ⏳ Espera de 60 segundos por restricción del plan gratis
    time.sleep(60)
