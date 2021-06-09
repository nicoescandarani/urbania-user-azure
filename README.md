# Usuarios
## Api REST del proyecto Urbania

Usuarios es una Api desarrollada en python capaz de interactuar con [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/), creando o borrando secretos.

## Tipos de Request
- POST
- DELETE

## Creacion de usuarios

Consiste en crear un secreto en [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/).
Se realiza mediante un POST request donde la API recibirá los siguientes datos desde un JSON enviado en el body.

- user: Caracteres permitidos 'a-z', 'A-Z', '0-9', y '-'. De 4 a 20 caracteres.
- password
- email

Con estos datos se crea en [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/) un secreto que llevara como nombre el 'user'+${TIMESTAMP} (no debe existir previamente el user). El valor del secreto sera "password".
Por último se envía usando el "email" un mensaje de bienvenida al usuario.

## Eliminacion de usuarios

Consiste en borrar un secreto en [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/).
Se realiza mediante un DELETE request donde la API recibirá los siguientes datos desde un JSON enviado en el body.

- user
- password

Con estos datos se buscara en [Azure Keyvault](https://azure.microsoft.com/es-es/services/key-vault/) un secreto que corresponda al 'user'+${TIMESTAMP} indicado en el body. De ser encontrado se evaluará si el valor de "password" coincide con el valor del secreto previamente almacenado

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

Usuarios requiere [Python](https://www.python.org/) v3.8 to run.

Instala las dependencias antes de iniciar el servidor.

```sh
pip install -r requirements.txt
```
> Nota: En entorno productivo no es necesario este paso.


## Respuestas del servidor
```sh
200: Se ha eliminado correctamente el usuario.
201: Se ha creado correctamente el usuario.
400: No se ingresaron los datos necesarios para el request enviado.
401: Los datos ingresados para borrar el usuario no coinciden con los almacenados en el Keyvault.
409: Ya existe el usuario que intenta crearse.
```

## Ruta
```sh
https://api-urbania.azurewebsites.net/api/usuarios
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


## Respuestas del servidor
```sh
200: Se ha logueado correctamente.
400: No se ingresaron los datos requeridos para realizar el login.
401: Los datos ingresados no coinciden con los almacenados en el Keyvault.
```

## Ruta
```sh
https://api-urbanialogin.azurewebsites.net/api/Login
```

## License

MIT
**Free Software**
