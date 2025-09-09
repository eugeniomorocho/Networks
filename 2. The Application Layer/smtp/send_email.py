# send_email_outlook_html.py
import smtplib
from email.message import EmailMessage

# Configuración del correo
msg = EmailMessage()
msg['Subject'] = 'Correo HTML desde Outlook'
msg['From'] = 'tu_correo@outlook.com'      # tu cuenta de Outlook
msg['To'] = 'destino@example.com'          # correo del destinatario

# Contenido en texto plano
text = "Hola, este correo está diseñado en HTML!"

# Contenido en HTML
html = """
<html>
  <body>
    <h1 style="color: #4CAF50;">¡Hola!</h1>
    <p>Este es un correo <b>diseñado en HTML</b> desde Python usando <i>Outlook SMTP</i>.</p>
    <p>Puedes incluir enlaces: <a href="https://www.example.com">Visitar ejemplo</a></p>
    <hr>
    <p style="font-size: small;">Enviado desde Python con Outlook SMTP</p>
  </body>
</html>
"""

# Adjuntar ambas versiones (texto y HTML)
msg.set_content(text)
msg.add_alternative(html, subtype='html')

# Configuración del servidor SMTP de Outlook
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_user = 'sf4e@outlook.com'
smtp_password = 'TU_APP_PASSWORD'

# Enviar correo
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # activar TLS
    server.login(smtp_user, smtp_password)
    server.send_message(msg)

print("Correo HTML enviado exitosamente!")
