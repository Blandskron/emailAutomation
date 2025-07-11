import requests

# Lista de clientes
clientes = [
    {"nombre": "Brian", "email": "example@example.cl"}
]



# Mensaje base
mensaje_base = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital 2024 Invitation</title>
</head>
<body>
    <a href="https://web.cl/home/">
        <img src="https://img.web.cl/var/albums/Recordatorio.jpg?m=1728252667" alt="Digital" style="width: 100%; height: auto;">
    </a>
</body>
</html>
"""

def enviar_email(cliente):
    mensaje = mensaje_base.format(nombre=cliente["nombre"])
    email_cliente = cliente["email"]
    
    payload = {
        'to': email_cliente,
        'subject': f"Hola {cliente['nombre']} Te esperamos este miércoles",
        'message': mensaje
    }
    
    response = requests.post('http://localhost:3000/send-email', json=payload)
    
    if response.status_code == 200:
        print(f"Correo enviado a {cliente['nombre']} ({cliente['email']})")
    else:
        print(f"Error al enviar correo a {cliente['nombre']} ({cliente['email']}): {response.text}")

# Enviar correos a todos los clientes
for cliente in clientes:
    enviar_email(cliente)