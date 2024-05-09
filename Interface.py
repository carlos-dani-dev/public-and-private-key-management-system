import tkinter as tk

class JanelaCheckbuttons(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Seleção de Checkbuttons")

        self.frame = tk.Frame(self)
        self.frame.pack()

        # Caixa de texto
        self.textbox = tk.Entry(self.frame)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Checkbuttons
        self.checkbutton_var1 = tk.IntVar()
        self.checkbutton_var2 = tk.IntVar()
        
        self.checkbutton1 = tk.Checkbutton(self.frame, text="Checkbutton 1", variable=self.checkbutton_var1)
        self.checkbutton1.grid(row=1, column=0, padx=5, pady=5)

        self.checkbutton2 = tk.Checkbutton(self.frame, text="Checkbutton 2", variable=self.checkbutton_var2)
        self.checkbutton2.grid(row=1, column=1, padx=5, pady=5)

        # Botão de exportar
        self.exportar_button = tk.Button(self.frame, text="Exportar", command=self.exportar)
        self.exportar_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Botão de verificação
        self.verificar_button = tk.Button(self, text="Verificar Seleção", command=self.verificar_selecao)
        self.verificar_button.pack()

    def verificar_selecao(self):
        if self.checkbutton_var1.get() == 1 and self.checkbutton_var2.get() == 1:
            print("Ambos os Checkbuttons foram selecionados!")
        else:
            print("Pelo menos um dos Checkbuttons não foi selecionado.")

    def exportar(self):
        print("Exportar")

class JanelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Inicial")
        self.abrir_janela_button = tk.Button(self, text="Abrir Janela de Checkbuttons", command=self.abrir_janela_checkbuttons)
        self.abrir_janela_button.pack()

    def abrir_janela_checkbuttons(self):
        janela_checkbuttons = JanelaCheckbuttons(self)
        janela_checkbuttons.grab_set()  # Impede que a janela principal seja acessada enquanto esta estiver aberta

# Criando a janela inicial e executando o loop principal
if __name__ == "__main__":
    janela_inicial = JanelaInicial()
    janela_inicial.mainloop()
