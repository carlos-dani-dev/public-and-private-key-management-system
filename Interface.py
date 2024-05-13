import tkinter as tk
from tkinter import filedialog
import BusinessRules as br

class JanelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Inicial")
        self.geometry("450x600")

        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        self.mostrar_pagina_inicial()

    def mostrar_pagina_inicial(self):
        self.limpar_container()

        label = tk.Label(self.container, text="Página Inicial", font=("Arial", 18))
        label.pack(pady=20)

        gerenciar_chaves = tk.Button(self.container, text="Gerenciar Chaves", command=self.mostrar_pagina_gerenciar_chaves, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
        gerenciar_chaves.pack(pady=10)

        gerar_chaves_button = tk.Button(self.container, text="Gerar Par de Chaves", command=self.mostrar_pagina_gerar_chaves, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        gerar_chaves_button.pack(pady=10)

        enc_dec_button = tk.Button(self.container, text="Encriptar/Decriptar arquivos", command=self.mostrar_pagina_enc_dec, bg="#F44336", fg="white", font=("Arial", 12), width=25)
        enc_dec_button.pack(pady=10)

    def mostrar_pagina_gerar_chaves(self):
        self.limpar_container()

        label = tk.Label(self.container, text="Gerar Par de Chaves", font=("Arial", 18))
        label.pack(pady=20)
        
        email_label = tk.Label(self.container, text="Email:", font=("Arial", 12))
        email_label.pack()
        email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=email_var, bg="lightgray", font=("Arial", 12))
        email_entry.pack()
        senha_label = tk.Label(self.container, text="Senha:", font=("Arial", 12))
        senha_label.pack()
        senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=senha_var, show="*", bg="lightgray", font=("Arial", 12))
        senha_entry.pack()

        tk.Label(self.container, text="Tamanho da chave:", font=("Arial", 12)).pack(pady=10)
        
        radiobuttons_var = tk.StringVar(self.container, "1024")
        radiobutton1024 = tk.Radiobutton(self.container, text="1024 bits", variable=radiobuttons_var,
                                        value="1024", bg="#E0E0E0", font=("Arial", 12))
        radiobutton1024.pack()
        radiobutton2048 = tk.Radiobutton(self.container, text="2048 bits", variable=radiobuttons_var,
                                        value="2048", bg="#E0E0E0", font=("Arial", 12))
        radiobutton2048.pack()
        radiobutton4096 = tk.Radiobutton(self.container, text="4096 bits", variable=radiobuttons_var,
                                        value="4096", bg="#E0E0E0", font=("Arial", 12))
        radiobutton4096.pack()

        gerar_button = tk.Button(self.container, text="Gerar", command=lambda: self.mostrar_info_gerar_chaves(email_var.get(), senha_var.get(), radiobuttons_var.get()), bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        gerar_button.pack(pady=20)
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_pagina_gerenciar_chaves(self):
        self.limpar_container()
        
        label = tk.Label(self.container, text="Gerenciar Chaves", font=("Arial", 18))
        label.pack(pady=20)
        
        buscar_button = tk.Button(self.container, text="Buscar Chave", command=self.mostrar_pagina_buscar_chave, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
        buscar_button.pack(pady=10)
        
        deletar_button = tk.Button(self.container, text="Deletar Chave(s)", command=self.mostrar_pagina_deletar_chaves, bg="#F44336", fg="white", font=("Arial", 12), width=20)
        deletar_button.pack(pady=10)
        
        listar_button = tk.Button(self.container, text="Listar Chaves", command=self.mostrar_pagina_listar_chaves, bg="#FFC107", fg="black", font=("Arial", 12), width=20)
        listar_button.pack(pady=10)
        
        export_import_button = tk.Button(self.container, text="Exportar/Importar Chaves", command=self.mostrar_pagina_exportar_importar_chaves, bg="#8BC34A", fg="black", font=("Arial", 12), width=20)
        export_import_button.pack(pady=10)
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)


    def mostrar_pagina_enc_dec(self):
        self.limpar_container()
        
        label = tk.Label(self.container, text="Encriptar/Decriptar Arquivos", font=("Arial", 18))
        label.pack(pady=20)
        
        email_label = tk.Label(self.container, text="Email:", font=("Arial", 12))
        email_label.pack()
        
        self.email_var = tk.StringVar()
        
        email_entry = tk.Entry(self.container, textvariable=self.email_var, bg="lightgray", font=("Arial", 12))
        email_entry.pack()
        
        senha_label = tk.Label(self.container, text="Senha:", font=("Arial", 12))
        senha_label.pack()
        
        self.senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=self.senha_var, show="*", bg="lightgray", font=("Arial", 12))
        senha_entry.pack()
        
        label = tk.Label(self.container, text="Chave:", font=("Arial", 12))
        label.pack(pady=5)
        
        self.ed_pubpriv_checkbutton_var = tk.IntVar(self.container, 0)
        ed_pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.ed_pubpriv_checkbutton_var,
                                            onvalue=0, offvalue=0, bg="#E0E0E0", font=("Arial", 12))
        ed_pub_checkbutton.pack()
        
        ed_priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.ed_pubpriv_checkbutton_var,
                                            onvalue=1, offvalue=0, bg="#E0E0E0", font=("Arial", 12))
        ed_priv_checkbutton.pack()
        
        self.caminho_arquivo_var = tk.StringVar()
        
        ed_arquivo_label = tk.Label(self.container, text="Escolher Arquivo:", textvariable=self.caminho_arquivo_var, font=("Arial", 12))
        ed_arquivo_label.pack(pady=10)
        
        ed_escolher_arquivo_button = tk.Button(self.container, text="Escolher Arquivo", command=self.buscar_arquivo, font=("Arial", 12))
        ed_escolher_arquivo_button.pack(pady=5)
        
        ed_enc_button = tk.Button(self.container, text="Encriptar", command=self.encriptar_arquivo, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        ed_enc_button.pack()
        
        ed_dec_button = tk.Button(self.container, text="Decriptar", command=self.decriptar_arquivo, bg="#F44336", fg="white", font=("Arial", 12), width=20)
        ed_dec_button.pack()
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_pagina_buscar_chave(self):
        self.limpar_container()
        
        label = tk.Label(self.container, text="Buscar Chave", font=("Arial", 18))
        label.pack(pady=20)
        
        email_label = tk.Label(self.container, text="Email:", font=("Arial", 12))
        email_label.pack()
        
        email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=email_var, bg="lightgray", font=("Arial", 12))
        email_entry.pack()
        
        tk.Label(self.container, text="Chave:", font=("Arial", 12)).pack(pady=5)
        
        self.buscar_pubpriv_checkbutton_var = tk.IntVar(self.container, 0)
        buscar_pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.buscar_pubpriv_checkbutton_var,
                                                onvalue=1, offvalue=0, bg="#E0E0E0", font=("Arial", 12))
        buscar_pub_checkbutton.pack()
        
        buscar_priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.buscar_pubpriv_checkbutton_var,
                                                onvalue=0, offvalue=1, bg="#E0E0E0", font=("Arial", 12))
        buscar_priv_checkbutton.pack()
        
        buscar_chave_button = tk.Button(self.container, text="Buscar", command=lambda: self.mostrar_mensagem_busca_chave(email_var.get(), self.buscar_pubpriv_checkbutton_var.get()), bg="#2196F3", fg="white", font=("Arial", 12), width=20)
        buscar_chave_button.pack(pady=20)
        
        self.buscar_mensagem_label = tk.Label(self.container, text="")
        self.buscar_mensagem_label.pack()
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_mensagem_busca_chave(self, email, value):

        if value == 1:
            mensagem = br.search_publickey(email)
        elif value == 0:
            mensagem = br.search_privatekey(email)

        if mensagem is None:
            mensagem = "Chave não encontrada!"
        else:
            mensagem = "Chave encontrada em " + mensagem

        self.buscar_mensagem_label.config(text=mensagem)

    def mostrar_pagina_deletar_chaves(self):
        self.limpar_container()

        label = tk.Label(self.container, text="Deletar Chave(s)", font=("Arial", 18))
        label.pack(pady=20)

        email_associado_label = tk.Label(self.container, text="Email associado à chave:", font=("Arial", 12))
        email_associado_label.pack()

        email_associado_var = tk.StringVar()
        email_associado_entry = tk.Entry(self.container, textvariable=email_associado_var, bg="lightgray", font=("Arial", 12))
        email_associado_entry.pack()

        deletar_button = tk.Button(self.container, text="Deletar", command=lambda: self.deletar_chave(email_associado_var.get(), self.deletekey_label), bg="#F44336", fg="white", font=("Arial", 12), width=20)
        deletar_button.pack(pady=20)

        self.deletekey_label = tk.StringVar()
        label = tk.Label(self.container, text="", textvariable=self.deletekey_label, font=("Arial", 12))
        label.pack(pady=5)

        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)

    def deletar_chave(self, email, deletekey_label):

        mensagem = br.delete_key(email)
        
        if mensagem == 1:
            self.deletekey_label.set("Chave(s) deletada(s) com sucesso!")
        else:
            self.deletekey_label.set("Falha ao deletar a(s) chave(s)!")

    def mostrar_pagina_listar_chaves(self):
        self.limpar_container()

        label = tk.Label(self.container, text="Listar Chave(s)", font=("Arial", 18))
        label.pack(pady=5)
        
        iniciar_listagem_button = tk.Button(self.container, text="Iniciar Listagem", command=self.iniciar_listagem, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        iniciar_listagem_button.pack(pady=10)
        
        label_chaves_publicas = tk.Label(self.container, text="Chaves Públicas", font=("Arial", 12))
        label_chaves_publicas.pack()
        
        self.lista_chaves_publicas = tk.Listbox(self.container, font=("Arial", 12))
        self.lista_chaves_publicas.pack()
        
        tk.Label(self.container, text="").pack()
        
        label_chaves_privadas = tk.Label(self.container, text="Chaves Privadas", font=("Arial", 12))
        label_chaves_privadas.pack()
        
        self.lista_chaves_privadas = tk.Listbox(self.container, font=("Arial", 12))
        self.lista_chaves_privadas.pack()
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)

    def iniciar_listagem(self):
        
        list_pub = br.list_my_publickeys()
        list_priv = br.list_my_privatekeys()

        self.lista_chaves_publicas.delete(0, tk.END)
        self.lista_chaves_privadas.delete(0, tk.END)

        pub_count = 0
        if list_pub is not None:
            for chave in list_pub:
                pub_count+=1
                self.lista_chaves_publicas.insert(pub_count, chave)

        priv_count = 0
        if list_priv is not None:
            for chave in list_priv:
                priv_count+=1
                self.lista_chaves_privadas.insert(priv_count, chave)


    def mostrar_pagina_exportar_importar_chaves(self):
        self.limpar_container()

        label = tk.Label(self.container, text="Exportar/Importar Chaves", font=("Arial", 18))
        label.pack(pady=5)
        
        email_label = tk.Label(self.container, text="Email:", font=("Arial", 12))
        email_label.pack()
        
        self.email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=self.email_var, bg="lightgray", font=("Arial", 12))
        email_entry.pack()
        
        senha_label = tk.Label(self.container, text="Senha da chave importada:", font=("Arial", 12))
        senha_label.pack()
        
        self.senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=self.senha_var, bg="lightgray", font=("Arial", 12))
        senha_entry.pack()
        
        label = tk.Label(self.container, text="Chave:", font=("Arial", 12))
        label.pack(pady=5)
        
        self.ei_pub_checkbutton_var = tk.IntVar(self.container, 0)
        self.ei_priv_checkbutton_var = tk.IntVar(self.container, 0)
        pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.ei_pub_checkbutton_var,
                                        onvalue=1, offvalue=0, bg="#E0E0E0", font=("Arial", 12))
        pub_checkbutton.pack()
        
        priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.ei_priv_checkbutton_var,
                                        onvalue=1, offvalue=0, bg="#E0E0E0", font=("Arial", 12))
        priv_checkbutton.pack()
        
        self.caminho_pub_arquivo_var = tk.StringVar()
        escolher_arquivo_pub_button = tk.Button(self.container, text="Arquivo da Chave Pública", command=self.buscar_pub_arquivo, font=("Arial", 12))
        escolher_arquivo_pub_button.pack(pady=10)
        
        arquivo_pub_label = tk.Label(self.container, text="----Public key----", textvariable=self.caminho_pub_arquivo_var, font=("Arial", 12))
        arquivo_pub_label.pack()
        
        self.caminho_priv_arquivo_var = tk.StringVar()
        escolher_arquivo_priv_button = tk.Button(self.container, text="Arquivo da Chave Privada", command=self.buscar_priv_arquivo, font=("Arial", 12))
        escolher_arquivo_priv_button.pack(pady=10)
        
        arquivo_priv_label = tk.Label(self.container, text="----Private key----", textvariable=self.caminho_priv_arquivo_var, font=("Arial", 12))
        arquivo_priv_label.pack()
        
        export_button = tk.Button(self.container, text="Exportar", command=self.exportar_chave, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        export_button.pack()
        
        import_button = tk.Button(self.container, text="Importar", command=self.importar_chave, bg="#F44336", fg="white", font=("Arial", 12), width=20)
        import_button.pack()
        
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves, bg="#FF5722", fg="white", font=("Arial", 12))
        voltar_button.pack(side="bottom", pady=10)


    def exportar_chave(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        arquivo_pub = self.caminho_pub_arquivo_var.get()
        arquivo_priv = self.caminho_priv_arquivo_var.get()
        tk.Label(self.container, text="", font=("Arial", 12)).pack()
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 1:
            (pubkey, privkey) = br.import_keypair("public/"+email+".pem", "private/"+email+".pem", senha)
            br.export_keypair(arquivo_pub, arquivo_priv, pubkey, privkey, senha)
            print("Chaves pública e privada exportadas!")
            tk.Label(self.container, text="Chaves pública e privada exportadas!", font=("Arial", 12)).pack()
        if self.ei_priv_checkbutton_var.get() == 1 and self.ei_pub_checkbutton_var.get() == 0:
            print("Impossível exportar unicamente a chave privada!")
            tk.Label(self.container, text="Impossível exportar unicamente a chave privada!", font=("Arial", 12)).pack()
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 0:
            pubkey = br.import_publickey(email)
            br.export_publickey(arquivo_pub, pubkey)
            print("Chave pública exportada!")
            tk.Label(self.container, text="Chave pública exportada!", font=("Arial", 12)).pack()
        if self.ei_pub_checkbutton_var.get() == 0 and self.ei_priv_checkbutton_var.get() == 0:
            #Mostrar na tela mensagem de erro
            tk.Label(self.container, text="É preciso que pelo menos uma opção esteja marcada!", font=("Arial", 12)).pack()
            print("É preciso que pelo menos uma opção esteja marcada!")

    def importar_chave(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        arquivo_pub = self.caminho_pub_arquivo_var.get()
        arquivo_priv = self.caminho_priv_arquivo_var.get()
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 1:
            (pubkey, privkey) = br.import_keypair(arquivo_pub, arquivo_priv, senha)
            br.export_keypair("public/"+email+".pem", "private/"+email+".pem", pubkey, privkey, senha)
            print("Chaves pública e privada importadas!")
        if self.ei_priv_checkbutton_var.get() == 1 and self.ei_pub_checkbutton_var.get() == 0:
            print("Impossível importar unicamente a chave privada!")
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 0:
            pubkey = br.import_publickey(arquivo_pub)
            br.export_publickey("public/"+email+".pem", pubkey)
            print("Chave pública importada!")
        if self.ei_pub_checkbutton_var.get() == 0 and self.ei_priv_checkbutton_var.get() == 0:
            print("É preciso que pelo menos uma opção esteja marcada!")

    def limpar_container(self):
        
        for widget in self.container.winfo_children():
            widget.destroy()

    def buscar_pub_arquivo(self):
        
        arquivo_path = filedialog.askopenfilename()
        
        self.caminho_pub_arquivo_var.set(arquivo_path)

    def buscar_arquivo(self):
        
        arquivo_path = filedialog.askopenfilename()
        
        self.caminho_arquivo_var.set(arquivo_path)

    def buscar_priv_arquivo(self):
        
        arquivo_path = filedialog.askopenfilename()
        
        self.caminho_priv_arquivo_var.set(arquivo_path)

    def mostrar_info_gerar_chaves(self, email, senha, tamanho_chave):
        if senha == "":
            senha = None
        key = br.generate_keypair(int(tamanho_chave), email, senha)
        if(key is not None):
            #Mostrar texto na tela
            tk.Label(self.container, text="Chave gerada com sucesso!", font=("Arial", 14)).pack()
            
            

    def encriptar_arquivo(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        arquivo = self.caminho_arquivo_var.get()
        pub_or_priv = self.ed_pubpriv_checkbutton_var.get()
        
        print("Email: ", email)
        print("Senha: ", senha)
        print("Arquivo: ", arquivo)
        print("Pub or Priv: ", pub_or_priv)
        print(arquivo)
        if pub_or_priv== 0:
            br.encrypt_plain_file(arquivo,email, senha, "public")
        else:
            br.encrypt_plain_file(arquivo,email, senha,  "private")

    def decriptar_arquivo(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        arquivo = self.caminho_arquivo_var.get()
        pub_or_priv = self.ed_pubpriv_checkbutton_var.get()
        if pub_or_priv== 0:
            br.decrypt_file(arquivo,email, senha, "public")
        else:
            br.decrypt_file(arquivo,email, senha,  "private")

if __name__ == "__main__":
    janela_inicial = JanelaInicial()
    janela_inicial.mainloop()
