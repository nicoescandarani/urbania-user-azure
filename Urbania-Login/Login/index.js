//Login
const processReq  = require('./utilities/processReq.js')

module.exports = async function (context, req) {
    const user = req.body.user.toLowerCase()
    const pass = req.body.pass

    if (user && pass){
        let proceso = await processReq.process(user, pass)      
       if (proceso){
            respuesta = {status: 200, body: {result: "Success"}}
        } else {
            respuesta = {status: 401, body: {result: "Usuario o contraseña incorrectos."}}
        }
    } else {
        respuesta = {status: 400, body: {result: "No se ingresaron los datos requeridos."}}
    }
    context.res = respuesta    
    context.done();
    
}