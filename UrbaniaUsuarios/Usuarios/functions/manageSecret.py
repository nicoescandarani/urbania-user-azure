from datetime import datetime
from Usuarios.functions.email import sendMail
from Usuarios.functions.login import getClient

def createSecret(client, usuario, password):
    now = str(datetime.now().strftime('%Y%m%d%H%M'))
    secretName = str(usuario)+now
    secretValue = client.set_secret(secretName, password)
    return secretValue

def searchSecret(client, secretPartialName):
    secretName = ""
    vaultSecrets = client.list_properties_of_secrets()
    for i in vaultSecrets:
        if (i.name[:-12] == secretPartialName):
            secretName = i.name
            break
    return secretName

def processRequest(*args): # Argumentos: args[0] => accion | args[1] => user | args[2] => password | args[3] => email
    process = False
    try:
        client = getClient("ManagedIdentity")
        vaultSecret = searchSecret(client, args[1])
    except:
        client = getClient("LocalCreds")
        vaultSecret = searchSecret(client, args[1])

    if (vaultSecret != ""): # Si se encontró un secreto con ese nombre de Usuario entra.
        if (args[0] == "borrarusuario"):
            secreto = client.get_secret(vaultSecret)
            if (args[2].lower() == secreto.value.lower()):
                client.begin_delete_secret(vaultSecret).result() # Borra el usuario.
                process = True
    else:
        if (args[0] == "crearusuario"):
            sendMail(args[1], args[2], args[3])
            createSecret(client, args[1], args[2]) # Crea un secreto en caso que no se encuentre uno con igual nombre de usuario.
           
            process = True
    return process
