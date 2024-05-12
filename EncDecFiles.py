from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import ImportExportKey as iekey
from Crypto.Random import get_random_bytes


def encrypt_file(plaintext_filepath, associated_email, rsa_privatekey_file_password, pub_or_priv):
    
    if pub_or_priv == "public":
        rsa_key = iekey.import_RSA_publickey("public/"+associated_email+".pem")
        cipher = PKCS1_v1_5.new(rsa_key)
        plaintext = open(plaintext_filepath)
        plaintext = plaintext.read().encode("utf-8")
        ciphertext = cipher.encrypt(plaintext)

    if pub_or_priv == "private":
        rsa_key = iekey.import_RSA_privatekey("private/"+associated_email+".pem", rsa_privatekey_file_password)
        cipher = PKCS1_v1_5.new(rsa_key)
        plaintext = open(plaintext_filepath).read().encode("utf-8")
        ciphertext = cipher.encrypt(plaintext)

    print("ciphertext: "+ str(ciphertext))
    
    # Salvar o criptograma em um arquivo
    name = plaintext_filepath.split(".")[0] + "-ciphertext.txt"
    with open(name, "wb") as file:
        file.write(ciphertext)
    return(ciphertext)


def decrypt_file(ciphertext_byte_filepath, associated_email, rsa_privatekey_file_password, pub_or_priv):
    ciphertext = open(ciphertext_byte_filepath, "rb").read()

    if pub_or_priv == "public":
        rsa_key = iekey.import_RSA_publickey("public/"+associated_email+".pem")
        print("rsa_key: "+str(rsa_key))
        sentinel = get_random_bytes(16)
        cipher = PKCS1_v1_5.new(rsa_key)
        encoded_plaintext = cipher.decrypt(ciphertext, sentinel)

    if pub_or_priv == "private":
        rsa_key = iekey.import_RSA_privatekey("private/"+associated_email+".pem", rsa_privatekey_file_password)
        sentinel = get_random_bytes(16)
        cipher = PKCS1_v1_5.new(rsa_key)
        encoded_plaintext = cipher.decrypt(ciphertext, sentinel)
    
    plaintext = encoded_plaintext.decode("utf-8")
    print("plaintext: "+plaintext)
    # Salvar o texto plano em um arquivo
    with open(ciphertext_byte_filepath+"-plaintext", "w") as file:
        file.write(plaintext)
    return plaintext

