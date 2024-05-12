import tkinter as tk
from tkinter import filedialog
import BusinessRules as br

class JanelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Inicial")
        self.geometry("400x550")

        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        self.mostrar_pagina_inicial()

    def mostrar_pagina_inicial(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página inicial
        label = tk.Label(self.container, text="Página Inicial")
        label.pack(pady=5)

        # Botão de gerar par de chaves
        gerenciar_chaves = tk.Button(self.container, text="Gerenciar chaves", command=self.mostrar_pagina_gerenciar_chaves)
        gerenciar_chaves.pack(pady=20)

        gerar_chaves_button = tk.Button(self.container, text="Gerar Par de Chaves", command=self.mostrar_pagina_gerar_chaves)
        gerar_chaves_button.pack(pady=20)

        enc_dec_button = tk.Button(self.container, text="Encriptar/Decriptar arquivos", command=self.mostrar_pagina_enc_dec)
        enc_dec_button.pack(pady=20)

    def mostrar_pagina_gerar_chaves(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de gerar chaves
        label = tk.Label(self.container, text="Gerar Par de Chaves")
        label.pack(pady=5)

        # Label e entrada para o email
        email_label = tk.Label(self.container, text="Email:")
        email_label.pack()

        email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=email_var, background="gray")
        email_entry.pack()

        # Label e entrada para a senha
        senha_label = tk.Label(self.container, text="Senha:")
        senha_label.pack()

        senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=senha_var, background="gray")
        senha_entry.pack()

        # Adicionando espaçamento
        tk.Label(self.container, text="Tamanho da chave:").pack(pady=5)

        # Radiobuttons
        radiobuttons_var = tk.StringVar(self.container, "1024")
        radiobutton1024 = tk.Radiobutton(self.container, text="1024 bits", variable=radiobuttons_var,
                                         value="1024", background="light blue")
        radiobutton1024.pack()
        radiobutton2048 = tk.Radiobutton(self.container, text="2048 bits", variable=radiobuttons_var,
                                         value="2048", background="light blue")
        radiobutton2048.pack()
        radiobutton4096 = tk.Radiobutton(self.container, text="4096 bits", variable=radiobuttons_var,
                                         value="4096", background="light blue")
        radiobutton4096.pack()

        # Botão de gerar
        gerar_button = tk.Button(self.container, text="Gerar", command=lambda: self.mostrar_info_gerar_chaves(email_var.get(), senha_var.get(), radiobuttons_var.get()))
        gerar_button.pack(pady=20)

        # Botão de voltar para a página inicial
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial)
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_pagina_gerenciar_chaves(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de gerenciar chaves
        label = tk.Label(self.container, text="Gerenciar Chaves")
        label.pack(pady=5)

        # Botões de ação
        buscar_button = tk.Button(self.container, text="Buscar Chave", command=self.mostrar_pagina_buscar_chave)
        buscar_button.pack(pady=10)

        deletar_button = tk.Button(self.container, text="Deletar Chave(s)", command=self.mostrar_pagina_deletar_chaves)
        deletar_button.pack(pady=10)

        listar_button = tk.Button(self.container, text="Listar Chaves", command=self.mostrar_pagina_listar_chaves)
        listar_button.pack(pady=10)

        export_import_button = tk.Button(self.container, text="Exportar/Importar Chaves", command=self.mostrar_pagina_exportar_importar_chaves)
        export_import_button.pack(pady=10)

        # Botão de voltar para a página inicial
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial)
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_pagina_enc_dec(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de encriptar/decriptar
        label = tk.Label(self.container, text="Encriptar/Decriptar Arquivos")
        label.pack(pady=5)

        # Label e entrada para o email
        email_label = tk.Label(self.container, text="Email:")
        email_label.pack()

        self.email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=self.email_var, background="gray")
        email_entry.pack()

        # Label e entrada para a senha
        senha_label = tk.Label(self.container, text="Senha:")
        senha_label.pack()

        self.senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=self.senha_var, background="gray")
        senha_entry.pack()

        label = tk.Label(self.container, text="Chave:")
        label.pack(pady=5)

        self.ed_pubpriv_checkbutton_var = tk.IntVar(self.container, 0)
        ed_pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.ed_pubpriv_checkbutton_var,
                                            onvalue=0, offvalue=0, background="light blue")
        ed_pub_checkbutton.pack()
        ed_priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.ed_pubpriv_checkbutton_var,
                                             onvalue=1, offvalue=0, background="light blue")
        ed_priv_checkbutton.pack()

        self.caminho_arquivo_var = tk.StringVar()  # StringVar para armazenar o caminho do arquivo

        # Label para escolher o arquivo
        ed_arquivo_label = tk.Label(self.container, text="Escolher Arquivo:", textvariable = self.caminho_arquivo_var)
        ed_arquivo_label.pack(pady=10)

        # Botão para escolher o arquivo
        ed_escolher_arquivo_button = tk.Button(self.container, text="Escolher Arquivo", command=self.buscar_arquivo)
        ed_escolher_arquivo_button.pack(pady=5)

        
        ed_enc_button = tk.Button(self.container, text="Encriptar", command=self.encriptar_arquivo)
        ed_enc_button.pack()

        ed_dec_button = tk.Button(self.container, text="Decriptar", command=self.decriptar_arquivo)
        ed_dec_button.pack()

        # Botão de voltar para a página inicial
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial)
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_pagina_buscar_chave(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de buscar chave
        label = tk.Label(self.container, text="Buscar Chave")
        label.pack(pady=5)

        # Label e entrada para o email
        email_label = tk.Label(self.container, text="Email:")
        email_label.pack()

        email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=email_var, background="gray")
        email_entry.pack()

        # Adicionando espaçamento
        tk.Label(self.container, text="Chave:").pack(pady=5)

        # Checkbuttons
        self.buscar_pubpriv_checkbutton_var = tk.IntVar(self.container, 0)
        buscar_pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.buscar_pubpriv_checkbutton_var,
                                                onvalue=1, offvalue=0, background="light blue")
        buscar_pub_checkbutton.pack()
        buscar_priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.buscar_pubpriv_checkbutton_var,
                                                 onvalue=0, offvalue=1, background="light blue")
        buscar_priv_checkbutton.pack()

        # Botão de buscar
        buscar_chave_button = tk.Button(self.container, text="Buscar",
                                        command=lambda: self.mostrar_mensagem_busca_chave(email_var.get(), self.buscar_pubpriv_checkbutton_var.get()))
        buscar_chave_button.pack(pady=20)

        # Rótulo para exibir mensagem
        self.buscar_mensagem_label = tk.Label(self.container, text="")
        self.buscar_mensagem_label.pack()  # Packing the label initially empty

        # Botão de voltar para a página de gerenciar chaves
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves)
        voltar_button.pack(side="bottom", pady=10)

    def mostrar_mensagem_busca_chave(self, email, value):
        # Função para mostrar a mensagem após buscar a chave
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
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de deletar chaves
        label = tk.Label(self.container, text="Deletar Chave(s)")
        label.pack(pady=5)

        # Campo de entrada de texto para o email associado à chave
        email_associado_label = tk.Label(self.container, text="Email associado à chave:")
        email_associado_label.pack()

        email_associado_var = tk.StringVar()
        email_associado_entry = tk.Entry(self.container, textvariable=email_associado_var, background="gray")
        email_associado_entry.pack()

        # Botão de deletar
        deletar_button = tk.Button(self.container, text="Deletar",
                                   command=lambda: self.deletar_chave(email_associado_var.get(), self.deletekey_label))
        deletar_button.pack(pady=20)

        # Adicionar widgets da página de deletar chaves
        self.deletekey_label = tk.StringVar()
        label = tk.Label(self.container, text="", textvariable=self.deletekey_label)
        label.pack(pady=5)

        # Botão de voltar para a página de gerenciar chaves
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves)
        voltar_button.pack(side="bottom", pady=10)

    def deletar_chave(self, email, deletekey_label):
        # Função para deletar a chave associada ao email
        mensagem = br.delete_key(email)
        # Exibir uma mensagem informando se a chave foi deletada com sucesso ou não
        if mensagem == 1:
            self.deletekey_label.set("Chave(s) deletada(s) com sucesso!")
        else:
            self.deletekey_label.set("Falha ao deletar a(s) chave(s)!")

    def mostrar_pagina_listar_chaves(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de listar chaves
        label = tk.Label(self.container, text="Listar Chave(s)")
        label.pack(pady=5)

        # Adicionar widgets da página de listar chaves
        iniciar_listagem_button = tk.Button(self.container, text="Iniciar Listagem", command=self.iniciar_listagem)
        iniciar_listagem_button.pack(pady=10)

        # Label para chaves públicas
        label_chaves_publicas = tk.Label(self.container, text="Chaves Públicas")
        label_chaves_publicas.pack()

        # Campo de listagem para chaves públicas
        self.lista_chaves_publicas = tk.Listbox(self.container)
        #Adicionar elementos à listagem
        self.lista_chaves_publicas.pack()

        # Adicionar espaço entre os campos
        tk.Label(self.container, text="").pack()

        # Label para chaves privadas
        label_chaves_privadas = tk.Label(self.container, text="Chaves Privadas")
        label_chaves_privadas.pack()

        # Campo de listagem para chaves privadas
        self.lista_chaves_privadas = tk.Listbox(self.container)
        self.lista_chaves_privadas.pack()

        # Botão de voltar para a página de gerenciar chaves
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves)
        voltar_button.pack(side="bottom", pady=10)

    def iniciar_listagem(self):
        # Função para iniciar a listagem
        # Aqui você pode chamar uma função para obter as chaves
        list_pub = br.list_my_publickeys()  # Supondo que você tenha uma função que retorne a lista de chaves
        list_priv = br.list_my_privatekeys()

        # Limpar os campos de listagem
        self.lista_chaves_publicas.delete(0, tk.END)
        self.lista_chaves_privadas.delete(0, tk.END)

        # Adicionar as chaves públicas à listagem
        pub_count = 0
        if list_pub is not None:
            for chave in list_pub:
                pub_count+=1
                self.lista_chaves_publicas.insert(pub_count, chave)

        # Adicionar as chaves privadas à listagem
        priv_count = 0
        if list_priv is not None:
            for chave in list_priv:
                priv_count+=1
                self.lista_chaves_privadas.insert(priv_count, chave)


    def mostrar_pagina_exportar_importar_chaves(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de exportar/importar chaves
        label = tk.Label(self.container, text="Exportar/Importar Chaves")
        label.pack(pady=5)

        # Label e entrada para o email
        email_label = tk.Label(self.container, text="Email:")
        email_label.pack()

        self.email_var = tk.StringVar()
        email_entry = tk.Entry(self.container, textvariable=self.email_var, background="gray")
        email_entry.pack()

        # Label e entrada para a senha
        senha_label = tk.Label(self.container, text="Senha da chave importada:")
        senha_label.pack()

        self.senha_var = tk.StringVar()
        senha_entry = tk.Entry(self.container, textvariable=self.senha_var, background="gray")
        senha_entry.pack()

        label = tk.Label(self.container, text="Chave:")
        label.pack(pady=5)

        self.ei_pub_checkbutton_var = tk.IntVar(self.container, 0)
        self.ei_priv_checkbutton_var = tk.IntVar(self.container, 0)
        pub_checkbutton = tk.Checkbutton(self.container, text="Pública", variable=self.ei_pub_checkbutton_var,
                                         onvalue=1, offvalue=0, background="light blue")
        pub_checkbutton.pack()
        priv_checkbutton = tk.Checkbutton(self.container, text="Privada", variable=self.ei_priv_checkbutton_var,
                                          onvalue=1, offvalue=0, background="light blue")
        priv_checkbutton.pack()

        self.caminho_pub_arquivo_var = tk.StringVar()  # StringVar para armazenar o caminho do arquivo

        # Botão para escolher o arquivo
        escolher_arquivo_pub_button = tk.Button(self.container, text="Arquivo da Chave Pública", command=self.buscar_pub_arquivo)
        escolher_arquivo_pub_button.pack(pady=10)

        # Label para escolher o arquivo
        arquivo_pub_label = tk.Label(self.container, text="----Public key----", textvariable=self.caminho_pub_arquivo_var)
        arquivo_pub_label.pack()


        self.caminho_priv_arquivo_var = tk.StringVar()  # StringVar para armazenar o caminho do arquivo

        # Botão para escolher o arquivo
        escolher_arquivo_priv_button = tk.Button(self.container, text="Arquivo da Chave Privada", command=self.buscar_priv_arquivo)
        escolher_arquivo_priv_button.pack(pady=10)

        # Label para escolher o arquivo
        arquivo_priv_label = tk.Label(self.container, text="----Private key----", textvariable=self.caminho_priv_arquivo_var)
        arquivo_priv_label.pack()

        export_button = tk.Button(self.container, text="Exportar", command=self.exportar_chave)
        export_button.pack()

        import_button = tk.Button(self.container, text="Importar", command=self.importar_chave)
        import_button.pack()

        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_gerenciar_chaves)
        voltar_button.pack(side="bottom", pady=10)

    def exportar_chave(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        arquivo_pub = self.caminho_pub_arquivo_var.get()
        arquivo_priv = self.caminho_priv_arquivo_var.get()
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 1:
            (pubkey, privkey) = br.import_keypair("public/"+email+".pem", "private/"+email+".pem", senha)
            br.export_keypair(arquivo_pub, arquivo_priv, pubkey, privkey, senha)
            print("Chaves pública e privada exportadas!")
        if self.ei_priv_checkbutton_var.get() == 1 and self.ei_pub_checkbutton_var.get() == 0:
            print("Impossível exportar unicamente a chave privada!")
        if self.ei_pub_checkbutton_var.get() == 1 and self.ei_priv_checkbutton_var.get() == 0:
            pubkey = br.import_publickey(email)
            br.export_publickey(arquivo_pub, pubkey)
            print("Chave pública exportada!")
        if self.ei_pub_checkbutton_var.get() == 0 and self.ei_priv_checkbutton_var.get() == 0:
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
        # Limpar todos os widgets no container
        for widget in self.container.winfo_children():
            widget.destroy()

    def buscar_pub_arquivo(self):
        # Função para buscar o arquivo
        arquivo_path = filedialog.askopenfilename()
        # Atualiza o valor do StringVar com o caminho do arquivo selecionado
        self.caminho_pub_arquivo_var.set(arquivo_path)

    def buscar_arquivo(self):
        # Função para buscar o arquivo
        arquivo_path = filedialog.askopenfilename()
        # Atualiza o valor do StringVar com o caminho do arquivo selecionado
        self.caminho_arquivo_var.set(arquivo_path)

    def buscar_priv_arquivo(self):
        # Função para buscar o arquivo
        arquivo_path = filedialog.askopenfilename()
        # Atualiza o valor do StringVar com o caminho do arquivo selecionado
        self.caminho_priv_arquivo_var.set(arquivo_path)

    def mostrar_info_gerar_chaves(self, email, senha, tamanho_chave):
        if senha == "":
            senha = None
        br.generate_keypair(int(tamanho_chave), email, senha)

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
