# INPUT: parâmetros do algoritmo de geração do par de chaves, apenas
# OUTPUT: arquivo em texto nomeado e com o par de chaves como conteúdo
from Crypto.PublicKey import RSA
import ImportExportKey as iekey


def rsa_keypair_generation(bits_key_length, privatekey_file_password, publickey_filename, privatekey_filename):
    
    key = RSA.generate(bits_key_length)
    privatekey = iekey.export_RSA_privatekey("private/"+privatekey_filename, key, privatekey_file_password)
    publickey = key.publickey()
    iekey.export_RSA_publickey("public/"+publickey_filename, publickey, start_exp_op=False)
    
    return (publickey, privatekey)