import pandas as pd
import requests
import time
import os

# 🔑 API Key desde Railway (variable de entorno)
API_KEY = os.getenv("API_KEY", "TU_API_KEY_AQUI")

# 📂 Nombre fijo del archivo Excel
EXCEL_FILE = "mensajes.xlsx"

# Leer Excel
df = pd.read_excel(EXCEL_FILE)

# Eliminar duplicados basados en el número
df = df.drop_duplicates(subset=["numero"])

# Configuración de la API
url = "https://wasenderapi.com/api/send-message"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Enviar mensajes
for index, row in df.iterrows():
    numero = str(row["numero"])
    mensaje = str(row["mensaje"])

    payload = {"to": numero, "text": mensaje}
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"✅ Enviado a {numero}: {response.text}")
    except Exception as e:
        print(f"❌ Error con {numero}: {e}")

    # ⏳ Espera de 60 segundos por restricción del plan gratuito
    time.sleep(60)
