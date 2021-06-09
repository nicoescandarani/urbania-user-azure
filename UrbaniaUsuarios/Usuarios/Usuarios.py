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
    try:
        inputJson = req.get_json()
        user = inputJson["user"] 
        password = inputJson["password"]
        if (req._HttpRequest__method == 'POST'):
            email = inputJson["email"]
    except:
        return finish("Error. Input invalido", 400) #400 => Bad Request

    # INICIO PRIMER VALIDACION. SE VALIDA QUE SE HAYAN RECIBIDO TODOS LOS ELEMENTOS NECESARIOS EN EL INPUT Y SEAN VALIDOS.
    if (req._HttpRequest__method == 'POST'):
        if (not validateInput(user, password, email)):
            return finish("Los datos ingresados son invalidos.", 400) #400 => Bad Request
        process = processRequest(user, password, email)
    else:
        if (not validateInput(user, password)):
            return finish("Los datos ingresados son invalidos.", 400) #400 => Bad Request
        process = processRequest(user, password)
    # FIN PRIMER VALIDACION.

    if (process): # FINAL EXITOSO
        if (req._HttpRequest__method == 'POST'):
            return finish("Se ha creado con exito el usuario " + user, 201) #201 => Created
        else:
            return finish("Se ha borrado con exito el usuario " + user, 200) #200 => Ok
    else: # FINAL CON ERRORES
        if (req._HttpRequest__method == 'POST'):
            return finish("Error. El usuario " +user+ " ya existe.", 409) #409 => Conflict
        else:
            return finish("Error. Verifique que el nombre de Usuario y Password sean correctos.", 401) #401 => Unauthorized

