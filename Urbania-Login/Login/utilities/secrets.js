let methods = {
    searchSecretName: async function(client, user){
        let secreto = ""
        for await (let secret of client.listPropertiesOfSecrets()) {
            let secretPartialName = secret.name.slice(0, -12)
            if (user == secretPartialName.toLowerCase()){
                secreto = secret.name
                break
            }
          }
        return secreto
    }
}
//  const specificSecret = await client.getSecret(secretName, { version: latestSecret.properties.version! });

module.exports = methods;