import io
import email
import smtplib
from Usuarios.functions.login import getClient

def sendMail(usuario, password, destinatario):
    try:
        client = getClient("ManagedIdentity")
        miCasilla = client.get_secret("Email-User-account").value
        miPass = client.get_secret("Email-User-Password").value
    except:
        client = getClient("LocalCreds")
        miCasilla = client.get_secret("Email-User-account").value
        miPass = client.get_secret("Email-User-Password").value
    try:
        body = "CONSERVA ESTOS DATOS Y PREPARATE PARA LA AVENTURA\n\nUSUARIO: " + usuario + "\nPASSWORD: " + password
        body = bytes(body, 'latin1')
        msg = email.message_from_bytes(body)
        msg['From'] = miCasilla
        msg['To'] = destinatario
        msg['Subject'] = "Hola "+ usuario + ". Bienvenido a Urbania."
        s = smtplib.SMTP("smtp.live.com",587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(miCasilla, miPass)
        s.sendmail(destinatario, destinatario, msg.as_bytes())
        s.quit()
    except:
        pass
