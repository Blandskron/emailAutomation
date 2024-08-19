import requests

# Lista de clientes
clientes = [
    {"nombre": "Bastian", "email": "bastianlandskronfreelancer@gmail.com"}
]



# Mensaje base
mensaje_base = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Awards 2024 Invitation</title>
</head>
<body>
    <a href="https://techawards2024.cl/home/">
    <img src="https://img.techawards2024.cl/var/albums/Invitacio%CC%81n%20TECH%20AWARDS%202024%20NEW.jpg?m=1724085945" alt="Tech Awards 2024" style="width: 100%; height: auto;">
    </a>
    <a href="https://techawards2024.cl/ics/TechAwards2024.ics" style="background-color: #007BFF; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-size: 16px;">Agrega el evento a tu calendario</a>
    <p>Pronto más información. Si tienes alguna pregunta, no dudes en contactarnos a evento@techawards2024.cl
</p>
</body>
</html>
"""

def enviar_email(cliente):
    mensaje = mensaje_base.format(nombre=cliente["nombre"])
    email_cliente = cliente["email"]
    
    payload = {
        'to': email_cliente,
        'subject': f"Hola {cliente['nombre']} Invitación TECH AWARS 2024",
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