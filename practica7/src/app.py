import time
import mysql.connector
from flask import Flask
import os

app = Flask(__name__)

def connect_db():
    for i in range(10):  # intenta 10 veces
        try:
            conn = mysql.connector.connect(
                host=os.environ.get("DB_HOST", "db"),
                user=os.environ.get("DB_USER", "user"),
                password=os.environ.get("DB_PASSWORD", "userpass"),
                database=os.environ.get("DB_NAME", "holamundo")
            )
            return conn
        except Exception as e:
            print(f"Intento {i+1}: BD no lista todavía ({e})")
            time.sleep(3)
    raise Exception("No se pudo conectar a la BD después de varios intentos")

@app.route("/")
def hello():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Hola Mundo! Conectado a la BD: {result[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
