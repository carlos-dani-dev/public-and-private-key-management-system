from tkinter import *
from tkinter import filedialog
import BusinessRules as br


class Window:
    def __init__(self, toplevel) -> None:
        self.font1 = ('verdana', '10', 'bold')
        self.check_pub = IntVar()
        self.check_priv = IntVar()

        self.search_frame = Frame(toplevel)
        self.search_frame.grid(row=1, column=1, pady=10)

        self.search_button = Button(self.search_frame, text="Search by email", background="green")
        self.search_button.bind("<Button-1>", self.search_key)
        self.search_button['height'] = 2
        self.search_button['width'] = 15
        self.search_button.grid(row=1, column=1, padx=10)
       
       
        self.search_entry_checkbox_frame = Frame(self.search_frame)
        self.search_entry_checkbox_frame.grid(row=1, column=2, padx=10)

        self.search_entry = Entry(self.search_entry_checkbox_frame, width=20, font=self.font1)
        self.search_entry.grid(row=1, column=1, columnspan=2, pady=5)
        self.search_entry_file_password = Entry(self.search_entry_checkbox_frame, width=20, font=self.font1)
        self.search_entry_file_password.grid(row=2, column=1, columnspan=2, pady=5)
        self.search_checkbox_pub = Checkbutton(self.search_entry_checkbox_frame, text="Public Key", variable=self.check_pub)
        self.search_checkbox_pub.grid(row=3, column=1)
        self.search_checkbox_priv = Checkbutton(self.search_entry_checkbox_frame, text="Private Key", variable=self.check_priv)
        self.search_checkbox_priv.grid(row=3, column=2)
################################################


        self.list_frame = Frame(toplevel)
        self.list_frame.grid(row=2, column=1, pady=10)

        self.list_pubkey_button = Button(self.list_frame, text="List public keys", background="blue")
        self.list_pubkey_button.bind("<Button-1>", self.list_pubkeys)
        self.list_pubkey_button['height'] = 1
        self.list_pubkey_button['width'] = 15
        self.list_pubkey_button.grid(row=1, column=1, padx=10)
        self.list_privkey_button = Button(self.list_frame, text="List private keys", background="blue")
        self.list_privkey_button.bind("<Button-1>", self.list_privkeys)
        self.list_privkey_button['height'] = 1
        self.list_privkey_button['width'] = 15
        self.list_privkey_button.grid(row=1, column=2, padx=10)
################################################


        self.generate_frame = Frame(toplevel)
        self.generate_frame.grid(row=3, column=1, pady=10)

        self.generate_button = Button(self.generate_frame, text="Generate key pair", background="yellow")
        self.generate_button.bind("<Button-1>", self.generate_keypair)
        self.generate_button.grid(row=1, column=1, padx=10)
        self.generate_button['height'] = 2
        self.generate_button['width'] = 15


        self.generate_checkbox_frame = Frame(self.generate_frame)
        self.generate_checkbox_frame.grid(row=1, column=2, padx=10)
        self.generate_checkbox_s1 = Checkbutton(self.generate_checkbox_frame, text="1024 bits")
        self.generate_checkbox_s1.grid(row=1, column=1)
        self.generate_checkbox_s2 = Checkbutton(self.generate_checkbox_frame, text="2048 bits")
        self.generate_checkbox_s2.grid(row=2, column=1)
        self.generate_checkbox_s3 = Checkbutton(self.generate_checkbox_frame, text="4096 bits")
        self.generate_checkbox_s3.grid(row=3, column=1)


        self.email_entry = Entry(self.generate_frame, width=20, font=self.font1)
        self.email_entry.grid(row=4, column=1, columnspan=2, pady=5)
        self.rsa_password_entry = Entry(self.generate_frame, width=20, font=self.font1)
        self.rsa_password_entry.grid(row=5, column=1, columnspan=2, pady=5)
################################################


        self.export_import_frame = Frame(toplevel)
        self.export_import_frame.grid(row=4, column=1, pady=10)

        self.export_button = Button(self.export_import_frame, text="Export key", background="red")
        self.export_button.bind("<Button-1>", self.export_key)
        self.export_button['height'] = 1
        self.export_button['width'] = 15
        self.export_button.grid(row=1, column=1, padx=10)

        self.import_button = Button(self.export_import_frame, text="Import key", background="red")
        # self.import_button.bind("<Button-1>", self.import_key)
        self.import_button['height'] = 1
        self.import_button['width'] = 15
        self.import_button.grid(row=1, column=2, padx=10)

        self.export_import_checkbutton_pubkey = Checkbutton(self.export_import_frame, text="Public key")
        self.export_import_checkbutton_pubkey.grid(row=2, column=1)
        self.export_import_checkbutton_privkey = Checkbutton(self.export_import_frame, text="Private key")
        self.export_import_checkbutton_privkey.grid(row=2, column=2)

        self.pubkey_associatedemail_entry = Entry(self.generate_frame, width=20, font=self.font1)
        self.pubkey_associatedemail_entry.grid(row=6, column=1, columnspan=2, pady=5)
        self.privkey_associatedemail_entry = Entry(self.generate_frame, width=20, font=self.font1)
        self.privkey_associatedemail_entry.grid(row=6, column=1, columnspan=2, pady=5)
        self.privkey_password_entry = Entry(self.generate_frame, width=20, font=self.font1)
        self.privkey_password_entry.grid(row=6, column=1, columnspan=2, pady=5)
        ################################################


        self.encrypt_decrypt_frame = Frame(toplevel)
        self.encrypt_decrypt_frame.grid(row=5, column=1, pady=10)

        self.encrypt_button = Button(self.encrypt_decrypt_frame, text="Encrypt", background="black")
        self.encrypt_button['height'] = 1
        self.encrypt_button['width'] = 15
        self.encrypt_button.grid(row=1, column=1, padx=10)

        self.decrypt_button = Button(self.encrypt_decrypt_frame, text="Decrypt", background="black")
        self.decrypt_button['height'] = 1
        self.decrypt_button['width'] = 15
        self.decrypt_button.grid(row=1, column=2, padx=10)

        self.encrypt_decrypt_checkbutton_pubkey = Checkbutton(self.encrypt_decrypt_frame, text="Public key")
        self.encrypt_decrypt_checkbutton_pubkey.grid(row=2, column=1)
        self.encrypt_decrypt_checkbutton_privkey = Checkbutton(self.encrypt_decrypt_frame, text="Private key")
        self.encrypt_decrypt_checkbutton_privkey.grid(row=2, column=2)

        self.button_explore = Button(self.encrypt_decrypt_frame, 
                                text = "Browse Files",
                                command = self.browseFiles).grid(row=4, column=1, columnspan=2, padx=10) 
        #######################################


        self.button_exit = Button(toplevel,
                            text = "Exit",
                            command = exit).grid(row=6, column=1, columnspan=2, padx=10)



    def search_key(self, event):
        if self.check_pub.get() == 1 and self.check_priv.get() == 1:
            print("Seleciona apenas uma opção de chave")
        elif self.check_pub.get() == 0 and self.check_priv.get() == 0:
            print("Selecione alguma opção de chave")
        elif self.check_pub.get() == 1 and self.check_priv.get() == 0:
            print("Procurando chave pública")
            br.search_publickey(self.search_entry.get())
        elif self.check_pub.get() == 0 and self.check_priv.get() == 1:
            print("Procurando chave privada")
            br.search_privatekey(self.search_entry.get(), self.search_entry_file_password.get())

    def generate_keypair(self, event):
        bits_length = 2048
        if self.generate_checkbox_s1 == 1 and self.generate_checkbox_s2 == 0 and self.generate_checkbox_s3 == 0:
            bits_length = 1024
        elif self.generate_checkbox_s1 == 0 and self.generate_checkbox_s2 == 1 and self.generate_checkbox_s3 == 0:
            bits_length = 2048
        elif self.generate_checkbox_s1 == 0 and self.generate_checkbox_s2 == 0 and self.generate_checkbox_s3 == 1:
            bits_length = 4096

        br.generate_keypair(bits_length, self.email_entry.get(), self.rsa_password_entry.get())

    def browsefile_export_key(self, event):
        self.export_key(self.browsefile_export_key(event))
    
    def browsefile_import_key(self, event):
        self.import_key(self.browsefile_export_key(event))
    
    def export_key(self, event, exportpath):
        pubkey_associated_email = self.pubkey_associatedemail_entry.get()
        privkey_associated_email = self.privkey_associatedemail_entry.get()
        import_file_password = self.privkey_password_entry.get()
        if self.export_import_checkbutton_pubkey == 1 and self.export_import_checkbutton_privkey == 1:
            (pub, priv) = br.import_keypair("", "public/"+pubkey_associated_email, "private/"+privkey_associated_email, import_file_password, False)
            br.export_keypair(pub, priv)
        elif self.export_import_checkbutton_pubkey == 1 and self.export_import_checkbutton_privkey == 0:
            pub = br.import_publickey("", "public/"+pubkey_associated_email, False)
            br.export_publickey(exportpath, pub)
        
    def import_key(self, event):
        pubkey_associated_email = self.pubkey_associatedemail_entry.get()
        privkey_associated_email = self.privkey_associatedemail_entry.get()
        import_file_password = self.privkey_password_entry.get()
        if self.export_import_checkbutton_pubkey == 1 and self.export_import_checkbutton_privkey == 1:
            (pub, priv) = br.import_keypair("", "public/"+pubkey_associated_email, "private/"+privkey_associated_email, import_file_password, False)
        elif self.export_import_checkbutton_pubkey == 1 and self.export_import_checkbutton_privkey == 0:
            pub = br.import_publickey("", "public/"+pubkey_associated_email, False)

    def list_pubkeys(seflf, event):
        br.list_my_publickeys()

    def list_privkeys(seflf, event):
        br.list_my_privatekeys()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.txt*"),
                                                        ("all files",
                                                            "*.*")))
        
        print(filename)
        return filename


root = Tk()
Window(root)
root.mainloop()
