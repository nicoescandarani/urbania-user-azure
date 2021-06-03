import re
from email_validator import validate_email

def validateEmail(email):
    try:
        validate_email(email)
        esValido = True
    except:
        esValido = False
    return esValido

def validateUserName(user):
    valido = False
    MINCHAR = 4
    MAXCHAR = 20
    if (user != ""):
        if (len(user) >= MINCHAR and len(user) <= MAXCHAR):
            userName = re.sub(r'\w+', '', user.replace("-",""))
            if (userName == ""):
                valido = True
    return valido

def validateInput(*args): # Argumentos: args[0] => user | args[1] => password | args[2] => accion | args[3] => email
    esValido = False
    if (len(args) == 3):
        if (validateUserName(args[0])):
            if (args[1] != "" and args[2] == 'crearusuario' or args[2] == 'borrarusuario'):
                esValido = True
    elif (len(args) == 4):
        if (validateUserName(args[0]) and validateEmail(args[3])):
            if (args[1] != "" and args[2] == 'crearusuario' or args[2] == 'borrarusuario'):
                esValido = True

    return esValido