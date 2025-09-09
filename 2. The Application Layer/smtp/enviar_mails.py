import smtplib
import pandas as pd
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Segundos de espera entre envio de correos diferentes
EMAIL_TIME_DELAY = 3

# Numero de reintentos de envio al mismo correo
MAX_RETRIES = 2
# Segundos de espera entre envio al mismo correo
RETIRES_TIME_DELAY = 5

# Archivo excel de correos, debe tener las columnas "Nombres" y "Email"
# CORREOS_EXCEL = "00_interesados/enviar_interesados.xlsx"
CORREOS_EXCEL = "01_entrevistas/enviar_entrevistas.xlsx"

# Archivo html
# CONTENIDO_HTML = "00_interesados/correo_interesados.html"
CONTENIDO_HTML = "01_entrevistas/correo_entrevistas.html"

# Subject del correo
# CORREO_SUBJECT = "¡Inscríbete a la Maestría en Ciencia de Datos! 🚀"
CORREO_SUBJECT = "Agenda tu entrevista para la Maestría en Inteligencia Artificial"

# ----------------------------------------------------------------------


# ------- Cargar lista de correos desde Excel
df = pd.read_excel(CORREOS_EXCEL)  # Asegúrate de tener columnas "Nombre" y "Email"

# ------- CAMPO NOMBRE
df['Nombre'] = df['Nombre'].astype(str).str.strip().str.title()

# ------- CAMPO CORREO

# Normalizar: eliminar espacios, pasar a minúsculas
df['Email'] = df['Email'].astype(str).str.strip().str.lower()

# Eliminar vacíos o nulos
df = df[df['Email'].notna() & (df['Email'] != '')]

# Validar formato básico de correo (regex simple)
df = df[df['Email'].str.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', na=False)]

# Eliminar correos electrónicos duplicados
df = df.drop_duplicates(subset=['Email'], keep='first')

print(df.head())

# exit()

# ------- Leer el archivo HTML
with open(CONTENIDO_HTML, 'r', encoding='utf-8') as file:
    email_body = file.read()

# ------- Configuración del servidor SMTP (Ejemplo con Gmail)
smtp_server = 'smtp.office365.com'  # Dirección del servidor SMTP de Exchange Online
smtp_port = 587  # Puerto recomendado para conexión segura TLS
email_user = 'maestriainteligenciaartificial@yachaytech.edu.ec'
email_password = 'Ecuador2030*'  # Usa una contraseña de aplicación si tienes 2FA habilitada

# ------- Iniciar la conexión al servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Habilitar seguridad TLS
    server.login(email_user, email_password)
    print("Conexión exitosa al servidor SMTP.")
except Exception as e:
    print(f"Error al conectar con el servidor SMTP: {e}")
    exit()

# ------- Enviar correos
for index, row in df.iterrows():
    try:
        time.sleep(EMAIL_TIME_DELAY)
        
        # # ... antes del envío del correo
        # email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        # if not re.match(email_regex, row['Email']):
        #     print(f"Email inválido: {row['Email']}")
        #     continue
        
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = row['Email']
        msg['Subject'] = CORREO_SUBJECT

        # Manejar el caso donde el nombre está vacío o no está disponible
        nombre = row['Nombre'] if pd.notna(row['Nombre']) else "Estimado/a"

        # Personalizar el cuerpo del correo con el nombre si está disponible
        personalized_body = email_body.replace("{{Nombre}}", nombre)
        msg.attach(MIMEText(personalized_body, 'html'))
        
        # Intentar reintentos
        for attempt in range(MAX_RETRIES):
            try:
                # Enviar el correo
                server.sendmail(email_user, row['Email'], msg.as_string())
                print(f"Correo enviado a {row['Email']}")
                break
            except Exception as e:
                print(f"Intento {attempt+1} fallido: {row['Email']} - {e}")
                time.sleep(RETIRES_TIME_DELAY)
        else:
            print(f"Fallo permanente al enviar a {row['Email']}")

    except Exception as e:
        print(f"Error al enviar correo a {row['Email']}: {e}")
        continue  # Continúa con el siguiente correo en caso de error

# Cerrar conexión
try:
    server.quit()
    print("Conexión cerrada correctamente.")
except Exception as e:
    print(f"Error al cerrar la conexión SMTP: {e}")

print("Proceso de envío finalizado.")