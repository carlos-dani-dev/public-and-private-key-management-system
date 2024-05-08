import KeyGeneration as kgen
import ImportExportKey as iekey
import EncDecFiles as edfiles
import os


# OBS: NÃO É POSSÍVEL ESCREVER 2 CHAVES COM O MESMO EMAIL ASSOCIADO, A ANTERIOR É SEMPRE SOBRESCRITA

def generate_keypair(bits_length, associated_email, privatekey_file_password):
    kgen.rsa_keypair_generation(bits_length, privatekey_file_password, associated_email, associated_email)


def import_keypair(associated_email, privatekey_filepath, publickey_filepath, import_file_password, start_export_op = True):
    imported_private_key = iekey.import_RSA_privatekey(privatekey_filepath, import_file_password)
    imported_publickey = iekey.import_RSA_publickey(publickey_filepath)
    if start_export_op:
        print("Importação concluída => Iniciando exportação")
        export_file_password = input("RSA private key export file password: ")
        iekey.export_RSA_privatekey("private/"+associated_email, imported_private_key, export_file_password)
        iekey.export_RSA_publickey("public/"+associated_email, imported_publickey)
    print(import_publickey, imported_private_key)
    return (imported_publickey, imported_private_key)


def import_publickey(associated_email, publickey_filepath, star_export_op = True):
    imported_publickey = iekey.import_RSA_publickey(publickey_filepath)
    if star_export_op:
        print("Importação concluída => Iniciando exportação")
        iekey.export_RSA_publickey(associated_email, imported_publickey)
    print(imported_publickey)
    return imported_publickey


def export_keypair(my_publickey, my_privatekey):
    associated_email = input("Associated email: ")
    import_file_password = input("RSA private key import file password: ")
    iekey.export_RSA_publickey("public/"+associated_email, my_publickey)
    iekey.export_RSA_privatekey("private/"+associated_email, my_privatekey, import_file_password)


def export_publickey(exportpath, my_publickey):
    iekey.export_RSA_publickey(exportpath, my_publickey)


def list_my_publickeys():
    print(os.listdir("public/"))
                    

def list_my_privatekeys():
    print(os.listdir("private"))


def search_publickey(associated_email):
    files_list = os.listdir("public/")
    for file_name in files_list:
        if file_name == associated_email+".pem":
            publickey = iekey.import_RSA_publickey("public/"+associated_email+".pem") # apenas retorna a chave públic, mas não grava novamente na pasta "private/"
            print(publickey)
            return publickey
    return None


def search_privatekey(associated_email, import_file_password):
    files_list = os.listdir("public/")
    for file_name in files_list:
        if file_name == associated_email+".pem":
            privatekey = iekey.import_RSA_privatekey("private/"+associated_email+".pem", import_file_password)
            print(privatekey)
            return privatekey
    return None


# o encriptador gera o criptograma em bytes
# meu programa deve receber o criptograma em bytes?
def encrypt_plain_file(filepath, associated_email, rsa_privatekey_file_password, pub_or_priv):
    return edfiles.encrypt_file(filepath, associated_email, rsa_privatekey_file_password, pub_or_priv)

def decrypt_file(ciphertext_byte_filepath, associated_email, rsa_privatekey_file_password, pub_or_priv):
    edfiles.decrypt_file(ciphertext_byte_filepath, associated_email, rsa_privatekey_file_password, pub_or_priv)
