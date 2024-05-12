from Crypto.PublicKey import RSA
import os


# adicionar associated_email para tratamento interno
def import_RSA_privatekey(key_filepath: str, file_password):
    if not os.path.exists(key_filepath):
        print(key_filepath+" not founded")
        return None
    
    with open(key_filepath, "rb") as f:
        data = f.read()
        my_privatekey = RSA.import_key(data, file_password)

    return my_privatekey


# adicionar associated_email para tratamento interno
def import_RSA_publickey(key_filepath: str):
    if not os.path.exists(key_filepath):
        print(key_filepath+" not founded")
        return None

    with open(key_filepath, "rb") as f:
        data = f.read()
        my_publickey = RSA.import_key(data)
    
    return my_publickey


# naturalmente o formato de arquivo .PEM já encripta a chave privada, mas é obsoleto. Por isso
# adiciona-se mais proteção
def export_RSA_privatekey(exportpath, my_privatekey, file_password: str):
    if not os.path.exists("private/"):
        os.makedirs("private/")
    
    with open(exportpath+".pem", "wb") as f:
        #file_password tem que ser binário?
        if file_password is None:
            data = my_privatekey.export_key(passphrase=file_password,
                                    pkcs=1, # padrão de codificação da chave privada no arquivo
                                    protection=None, # esquema
                                    # de encriptação da chave privada com a passphrase (recomendado) 
                                    prot_params=None) # parâmetros de
                                    # derivação da chave de encriptação da chave privada a
                                    # partir da passphrase (recomendado)
        else:    
            data = my_privatekey.export_key(passphrase=file_password,
                                        pkcs=8, # padrão de codificação da chave privada no arquivo
                                        protection='PBKDF2WithHMAC-SHA512AndAES256-CBC', # esquema
                                        # de encriptação da chave privada com a passphrase (recomendado) 
                                        prot_params={'iteration_count':131072}) # parâmetros de
                                        # derivação da chave de encriptação da chave privada a
                                        # partir da passphrase (recomendado)
        f.write(data)

    return my_privatekey


def export_RSA_publickey(exportpath, my_publickey, start_exp_op):
    if not os.path.exists("public/"):
        os.makedirs("public/")

    if not start_exp_op: exportpath+=".pem"
    with open(exportpath, "wb") as f:
        data = my_publickey.public_key().export_key()
        f.write(data)