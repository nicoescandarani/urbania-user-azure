const secrets  = require('./secrets.js')
const { SecretClient } = require("@azure/keyvault-secrets")
const { DefaultAzureCredential, ClientSecretCredential } = require("@azure/identity")


let methods = { 
    process: async function(user, pass){
        const keyVaultURL = process.env["keyVaultURL"]
        let esValido = false

        try {
            let client = this.getClient("Default")
            let secretFullName = await secrets.searchSecretName(client, user)
            if (secretFullName != ""){
                let secret = await client.getSecret(secretFullName)
                if (pass == secret.value){
                    esValido = true 
                }
            }
        } catch (e) {
            let client = this.getClient("ByClientID")
            let secretFullName = await secrets.searchSecretName(client, user)
            if (secretFullName != ""){
                let secret = await client.getSecret(secretFullName)
                if (pass == secret.value){
                    esValido = true 
                }
            }
        
        }
        return esValido
    },
    getClient: function(method){
        const keyVaultURL = process.env["keyVaultURL"]
        let credential
        let client
        if (method == "Default"){
            credential = new DefaultAzureCredential()
            client = new SecretClient(keyVaultURL, credential)
        } else if (method == "ByClientID"){
            credential = new ClientSecretCredential(process.env["tenantId"], process.env["clientId"], process.env["clientSecret"])
            client = new SecretClient(keyVaultURL, credential)
        }
        return client
    }
}

module.exports = methods;