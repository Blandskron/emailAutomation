import requests

# Lista de clientes
clientes = [
    {"nombre": "Claudio", "email": "csantiba@gestum.cl"},
    {"nombre": "Allonne", "email": "allonne.bg@gmail.com"},
    {"nombre": "Patricio", "email": "ppastor@bcn.cl"},
    {"nombre": "Gustavo", "email": "gustavo.gimenez@globant.com"},
    {"nombre": "Claudio", "email": "c.inostroza@ticservices.cl"},
    {"nombre": "Jaime", "email": "jacarril@gmail.com"},
    {"nombre": "Paola", "email": "paolagodoysam@gmail.com"},
    {"nombre": "Manuel", "email": "m.cordovao@gmail.com"},
    {"nombre": "Luis", "email": "lsilvab@saamtowage.com"},
    {"nombre": "Cristóbal", "email": "cristobal@rojasalday.com"},
    {"nombre": "VERONICA", "email": "veronica.figueroa@carabineros.cl"},
    {"nombre": "Maria", "email": "maraya.soc@gmail.com"},
    {"nombre": "PHILIPPE", "email": "philippe.pares@idemia.com"},
    {"nombre": "SEBASTIAN", "email": "sebastian.riveros@idemia.com"},
    {"nombre": "RAFAEL", "email": "rdelcampom@gmail.com"},
    {"nombre": "Rodrigo", "email": "rleon@silva.cl"},
    {"nombre": "Andrés", "email": "andres.letelier@rancagua.cl"},
    {"nombre": "Javier", "email": "jgomez@mbienes.cl"},
    {"nombre": "María Fernanda", "email": "fernanda.cortez@municipalidadpetorca.cl"},
    {"nombre": "Rodrigo", "email": "rodrigo.diaz.o@uchile.cl"},
    {"nombre": "Paz", "email": "paz.henriquez@uchile.cl"},
    {"nombre": "Felipe", "email": "felipe.montegu@globant.com"},
    {"nombre": "Mariano", "email": "mariano.andividria@globant.com"},
    {"nombre": "Paulina", "email": "paulina.cabrera@chilecompra.cl"},
    {"nombre": "Christian", "email": "chinojosav@contraloria.cl"},
    {"nombre": "Daniela", "email": "dgonzalezg@contraloria.cl"},
    {"nombre": "Francisca", "email": "francisca.soto@chilecompra.cl"},
    {"nombre": "Patricio", "email": "patricio.yanez.villarroel@gmail.com"},
    {"nombre": "Jadra", "email": "jadra.fer@gmail.com"},
    {"nombre": "José", "email": "jflores@newtenberg.com"},
    {"nombre": "Marisol", "email": "mdocmac@newtenberg.com"},
    {"nombre": "Gonzalo", "email": "gsalazar@lascondes.cl"},
    {"nombre": "José Miguel", "email": "jm.umana@munirauco.cl"},
    {"nombre": "Jorge", "email": "jramirez@maipu.cl"},
    {"nombre": "Cristhian", "email": "cbravo@sanrosendo.com"},
    {"nombre": "Claudia", "email": "cmartinez@digital.gob.cl"},
    {"nombre": "SOFIA", "email": "SOFIMNZ@GMAIL.COM"},
    {"nombre": "Vania", "email": "vania.rammsy@maipu.cl"},
    {"nombre": "PALOMA", "email": "PALOMA.VALENZUELA@MAIPU.CL"},
    {"nombre": "Andrea", "email": "andrea.zamora@chileatiende.cl"},
    {"nombre": "Fernando", "email": "fernando.humeres@corfo.cl"},
    {"nombre": "Rodolfo", "email": "rodolfo.herrera@corfo.cl"},
    {"nombre": "Norma", "email": "norma.bustos@corfo.cl"},
    {"nombre": "Jesús", "email": "jancaten@previsionsocial.gob.cl"},
    {"nombre": "Florencia", "email": "florenciaa@iadb.org"},
    {"nombre": "Raimundo", "email": "rfbravo@aduana.cl"},
    {"nombre": "Flavio", "email": "poblete481@gmail.com"},
    {"nombre": "Carolina", "email": "carozs@amazon.com"},
    {"nombre": "Christian", "email": "chrgonza@uchile.cl"},
    {"nombre": "Diego", "email": "dmartinez@cenabast.cl"},
    {"nombre": "Federico", "email": "fosta@redhat.com"},
    {"nombre": "Ivonne", "email": "idiaz@educaciondigitalsa.com"},
    {"nombre": "Brayan", "email": "bhonorato@educaciondigitalsa.com"},
    {"nombre": "María Paz", "email": "mgonzalez@i-edglobal.com"},
    {"nombre": "Gilbert", "email": "gleiva@educaciondigitalsa.com"},
    {"nombre": "Jaime", "email": "jpacheco@educaciondigitalsa.com"},
    {"nombre": "María Ignacia", "email": "malfonso@educaciondigitalsa.com"},
    {"nombre": "Braulio", "email": "bneira@digital.gob.cl"},
    {"nombre": "Marcos", "email": "marcos.mondaca.silva@gmail.com"},
    {"nombre": "Constanza", "email": "cpperez2@uc.cl"},
    {"nombre": "Enrique", "email": "enrique.opazo@agenciaeducacion.cl"},
    {"nombre": "Giancarlo", "email": "gsillerico@lab.gob.cl"},
    {"nombre": "George", "email": "gbarria@fosis.gob.cl"},
    {"nombre": "GABRIEL", "email": "grosales@fosis.gob.cl"},
    {"nombre": "Lorena", "email": "ltorres@lab.gob.cl"},
    {"nombre": "Camilo", "email": "camilo.olate@saludohiggins.cl"},
    {"nombre": "Gonzalo", "email": "gonzaloabm@gmail.com"},
    {"nombre": "Raúl", "email": "rfaundez9@gmail.com"},
    {"nombre": "Jorge", "email": "jmontesinos@mbienes.cl"},
    {"nombre": "Juan Pablo", "email": "jmeza@mbienes.cl"},
    {"nombre": "Roberto", "email": "ripuga@uc.cl"},
    {"nombre": "Catalina", "email": "catalina.gonzalez@maipu.cl"},
    {"nombre": "Harry", "email": "holivares@mbienes.cl"},
    {"nombre": "Teresa", "email": "tolaveq@maipu.cl"},
    {"nombre": "Nicolás", "email": "nargomedo@mbienes.cl"},
    {"nombre": "David", "email": "dsalazar@mbienes.cl"},
    {"nombre": "Jose Adrian", "email": "adrian.paredes@umag.cl"},
    {"nombre": "Karina", "email": "kaguilera@mtt.gob.cl"},
    {"nombre": "Jose", "email": "Innovacion@munifrutillar.cl"},
    {"nombre": "Javiera", "email": "transformaciondigital@cauquenes.cl"},
    {"nombre": "Ernesto", "email": "ernesto.quiroga@muninogales.cl"},
    {"nombre": "Victor", "email": "victor.saavedra@muninogales.cl"},
    {"nombre": "antonio angel", "email": "informatica@munisanpedro.cl"},
    {"nombre": "BELÉN", "email": "b.lopez@munisanpedro.cl"},
    {"nombre": "Iván", "email": "iquinones@sercotec.cl"},
    {"nombre": "PATRICIA", "email": "patricia.peps@gmail.com"},
    {"nombre": "Fernando", "email": "fernando.guasch@sesuperior.cl"},
    {"nombre": "Jesus", "email": "jmayorga@minvu.cl"},
    {"nombre": "Máximo", "email": "m.lizana@munimarchigue.cl"},
    {"nombre": "Jorge", "email": "jorge.moreno@sleplosparques.gob.cl"},
    {"nombre": "Roxana", "email": "rvercoutere@fosis.gob.cl"},
    {"nombre": "Francisca", "email": "fmoya@lab.gob.cl"},
    {"nombre": "RAMIRO", "email": "rmendoza@momag.cl"},
    {"nombre": "Luis", "email": "luis.delgado@imo.cl"},
    {"nombre": "Sebastian", "email": "sebastian.alarcon.munoz@gmail.com"},
    {"nombre": "Christian", "email": "informatica@cauquenes.cl"},
    {"nombre": "Ignacio", "email": "ifaglonij@ine.gob.cl"},
    {"nombre": "Antonia", "email": "antodiaz@google.com"},
    {"nombre": "Catalina", "email": "cbustost@tgr.cl"},
    {"nombre": "Francisco", "email": "francisco.donoso@sma.gob.cl"},
    {"nombre": "Daniel", "email": "danielteplizky@registrocivil.gob.cl"}
]



# Mensaje base
mensaje_base = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Un estado digital 2024 Invitation</title>
</head>
<body>
    <a href="https://unestadodigital.cl/home/">
        <img src="https://img.unestadodigital.cl/var/albums/Recordatorio.jpg?m=1728252667" alt="Un estado digital" style="width: 100%; height: auto;">
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