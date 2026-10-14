"""Librería: Requests
Consume una API pública (JSONPlaceholder): consulta y envío de datos."""
import requests

URL = "https://jsonplaceholder.typicode.com"


def main():
    try:
        # GET: obtener un usuario
        r = requests.get(f"{URL}/users/1", timeout=10)
        r.raise_for_status()
        usuario = r.json()
        print("Código de estado:", r.status_code)
        print("Nombre:", usuario["name"], "| Correo:", usuario["email"])

        # GET con parámetros: publicaciones del usuario 1
        r = requests.get(f"{URL}/posts", params={"userId": 1}, timeout=10)
        print("Publicaciones del usuario 1:", len(r.json()))

        # POST: crear una publicación (simulada por la API)
        nuevo = {"title": "Hola", "body": "Prueba con requests", "userId": 1}
        r = requests.post(f"{URL}/posts", json=nuevo, timeout=10)
        print("POST →", r.status_code, r.json())
    except requests.exceptions.RequestException as error:
        print("Error de conexión:", error)


if __name__ == "__main__":
    main()
