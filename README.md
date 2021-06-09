## Instalación Local

Usuarios requiere [Python](https://www.python.org/) v3.8 to run.

Instala las dependencias antes de iniciar el servidor.

```sh
pip install -r requirements.txt
```
> Nota: En entorno productivo no es necesario este paso.

## Ruta
```sh
https://api-urbania.azurewebsites.net/api/usuarios
```

## Respuestas del servidor
```sh
200: Se ha eliminado correctamente el usuario.
201: Se ha creado correctamente el usuario.
400: No se ingresaron los datos necesarios para el request enviado.
401: Los datos ingresados para borrar el usuario no coinciden con los almacenados en el Keyvault.
409: Ya existe el usuario que intenta crearse.
```


---------------

# Login
## Api REST del proyecto Urbania

Login es una Api desarrollada en NodeJS capaz de interactuar con [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/), consultando los secretos allí almacenados.

## Tipos de Request
- POST


## Logueo

Consiste en buscar un secreto en [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/) usando los siguientes datos:

- user
- password

Se utiliza el "user" como parámetro para la búsqueda. De encontrarse el secreto correspondiente a ese usuario, se verifica que el valor que almacena ese secreto se corresponda al enviado en "password". 

## Autorización
Tipo OAuth2.
Para recibir el Barer y poder hacer el request a API Usuarios, debe enviarse un POST request a la siguiente ruta:
```sh
https://login.microsoftonline.com/${TENANT_ID}/oauth2/token
```
El body debe contener los siguientes datos:

```sh
grant_type: client_credentials
client_id: ${CLIENT_ID}
client_secret: ${CLIENT_SECRET}
resource: https://api-urbania.azurewebsites.net
```

## Instalación Local

Login requiere [NodeJs](https://www.python.org/) v.(Node 14, 12, & 10)

Instala las dependencias antes de iniciar el servidor.

```sh
npm install
```
> Nota: En entorno productivo no es necesario este paso.


## Ruta
```sh
https://api-urbanialogin.azurewebsites.net/api/Login
```


## Respuestas del servidor
```sh
200: Se ha logueado correctamente.
400: No se ingresaron los datos requeridos para realizar el login.
401: Los datos ingresados no coinciden con los almacenados en el Keyvault.
```

## License

MIT
**Free Software**
