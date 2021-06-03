import os
import sys
import azure.functions as func

#These are necessary to import from a parent folder because of venv
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from Usuarios.functions.finish import finish
from Usuarios.functions.manageSecret import processRequest
from Usuarios.functions.validateInput import validateInput

def main(req: func.HttpRequest) -> func.HttpResponse:
    if (req._HttpRequest__method == 'POST'):
        accion = "crearusuario"
    elif (req._HttpRequest__method == 'DELETE'):
        accion = "borrarusuario"

    try:
        inputJson = req.get_json()
        user = inputJson["user"]
        password = inputJson["password"]
        if (accion.lower() == "crearusuario"):
            email = inputJson["email"]
    except:
        return finish("Error. Input invalido", 400)

    # INICIO PRIMER VALIDACION. SE VALIDA QUE SE HAYAN RECIBIDO TODOS LOS ELEMENTOS NECESARIOS EN EL INPUT Y SEAN VALIDOS.
    if ("email" in locals()):
        if (not validateInput(user, password, accion, email)):
            return finish("Los datos ingresados son invalidos.", 400)
        process = processRequest(accion, user, password, email)
    else:
        if (not validateInput(user, password, accion)):
            return finish("Los datos ingresados son invalidos.", 400)
        process = processRequest(accion, user, password)
    # FIN PRIMER VALIDACION.

    if (process): # FINAL EXITOSO
        if (accion == "crearusuario"):
            return finish("Se ha creado con exito el usuario " + user, 201)
        elif (accion == "borrarusuario"):
            return finish("Se ha borrado con exito el usuario " + user, 200)
    else: # FINAL CON ERRORES
        if (accion == "crearusuario"):
            return finish("Error. El usuario " +user+ " ya existe.", 409)
        elif (accion == "borrarusuario"):
            return finish("Error. Verifique que el nombre de Usuario y Password sean correctos.", 401)

