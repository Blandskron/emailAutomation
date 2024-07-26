# Email Automation with Node.js and Python

Este proyecto permite enviar correos electrónicos automáticamente utilizando un servidor SMTP configurado en cPanel. La automatización se realiza a través de un servidor Node.js y un script Python.

## Requisitos

- Node.js
- npm (Node Package Manager)
- Python 3.x

## Configuración

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local.

```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Instalar dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias para Node.js.

```bash
npm install
```

### 3. Configurar las credenciales de SMTP

Asegúrate de que `server.js` esté configurado con las credenciales correctas para tu servidor SMTP de cPanel.

```javascript
const transporter = nodemailer.createTransport({
    host: 's320.v2nets.com', // Host del servidor SMTP de cPanel
    port: 465, // Puerto SMTP (465 para SSL)
    secure: true, // true para SSL
    auth: {
        user: 'evento@techawards2024.cl',
        pass: 'i>6P;7)7xlN2'
    }
});
```

### 4. Ejecutar el servidor

Inicia el servidor Node.js.

```bash
node server.js
```

### 5. Configurar y ejecutar el script Python

Crea un archivo `envio.py` con el siguiente contenido:

```python
import requests

# Lista de clientes
clientes = [
    {"nombre": "Tiare", "email": "tiare@example.com"},
    {"nombre": "Benjamin", "email": "benjamin@example.com"},
    {"nombre": "Sebastian", "email": "sebastian@example.com"},
]

# Mensaje base
mensaje_base = """
    <html>
    <body>
        <h1>🌟 Hola {nombre}, ¡te invitamos a nuestro exclusivo webinar! 🌟</h1>
        <p>📅 <b>Fecha:</b> 02/08/2024</p>
        <p>🕒 <b>Hora:</b> 20:00</p>
        <p>🔗 <b>Enlace de registro:</b> <a href="http://techawards2024.cl/">http://techawards2024.cl/</a></p>
        <p>¡No te lo pierdas! Será una gran oportunidad para aprender y conectar. 🎓🚀</p>
    </body>
    </html>
"""

def enviar_email(cliente):
    mensaje = mensaje_base.format(nombre=cliente["nombre"])
    email_cliente = cliente["email"]
    
    payload = {
        'to': email_cliente,
        'subject': "Invitación a Webinar Exclusivo",
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
```

Ejecuta el script para enviar los correos electrónicos.

```bash
python envio.py
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.