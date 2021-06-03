import os
import azure.identity as identity
from azure.keyvault.secrets import SecretClient

def getClient(mode):
    keyVaultURL = os.environ["keyVaultURL"] # KEY VAULT URL
    if (mode == "ManagedIdentity"):
        creds = identity.ManagedIdentityCredential()
        client = SecretClient(vault_url=keyVaultURL, credential=creds)
    if (mode == "LocalCreds"):
        creds = identity.ClientSecretCredential( client_id=os.environ["clientId"],
                                        client_secret=os.environ["clientSecret"],
                                        tenant_id=os.environ["tenantId"])
        client = SecretClient(vault_url=keyVaultURL, credential=creds)
    return client