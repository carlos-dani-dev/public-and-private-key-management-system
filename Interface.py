import tkinter as tk

class JanelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Inicial")
        self.geometry("350x500")

        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        self.mostrar_pagina_inicial()

    def mostrar_pagina_inicial(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página inicial
        label = tk.Label(self.container, text="Página Inicial")
        label.pack(pady=10)

        # Botão de gerar par de chaves
        gerar_chaves_button = tk.Button(self.container, text="Gerar Par de Chaves", command=self.mostrar_pagina_chaves)
        gerar_chaves_button.pack()

    def mostrar_pagina_chaves(self):
        # Limpar o container
        self.limpar_container()

        # Adicionar widgets da página de gerar chaves
        label = tk.Label(self.container, text="Gerar Par de Chaves")
        label.pack(pady=10)

        # Botão de voltar para a página inicial
        voltar_button = tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial)
        voltar_button.pack()

    def limpar_container(self):
        # Limpar todos os widgets no container
        for widget in self.container.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    janela_inicial = JanelaInicial()
    janela_inicial.mainloop()
