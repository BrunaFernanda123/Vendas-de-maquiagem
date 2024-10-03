import tkinter as tk
from tkinter import messagebox, simpledialog


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} ({self.quantidade} em estoque)"


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return [str(produto) for produto in self.produtos]

    def excluir_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                return f"Produto '{nome}' excluído com sucesso."
        return "Produto não encontrado."

    def alterar_produto(self, nome, novo_nome, novo_preco, nova_quantidade):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.nome = novo_nome
                produto.preco = novo_preco
                produto.quantidade = nova_quantidade
                return f"Produto '{nome}' alterado com sucesso."
        return "Produto não encontrado."


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Vendas de Maquiagem")

        self.estoque = Estoque()

        self.btn_cadastrar = tk.Button(master, text="Cadastrar Produto", command=self.cadastrar_produto)
        self.btn_cadastrar.pack(pady=10)

        self.btn_listar = tk.Button(master, text="Listar Produtos", command=self.listar_produtos)
        self.btn_listar.pack(pady=10)

        self.btn_excluir = tk.Button(master, text="Excluir Produto", command=self.excluir_produto)
        self.btn_excluir.pack(pady=10)

        self.btn_alterar = tk.Button(master, text="Alterar Produto", command=self.alterar_produto)
        self.btn_alterar.pack(pady=10)

    def cadastrar_produto(self):
        nome = simpledialog.askstring("Cadastro", "Nome do produto:")
        preco = simpledialog.askfloat("Cadastro", "Preço do produto:")
        quantidade = simpledialog.askinteger("Cadastro", "Quantidade em estoque:")

        if nome and preco is not None and quantidade is not None:
            produto = Produto(nome, preco, quantidade)
            self.estoque.adicionar_produto(produto)
            messagebox.showinfo("Cadastro", f"Produto '{nome}' cadastrado com sucesso!")

    def listar_produtos(self):
        produtos = self.estoque.listar_produtos()
        if produtos:
            messagebox.showinfo("Produtos", "\n".join(produtos))
        else:
            messagebox.showinfo("Produtos", "Nenhum produto cadastrado.")

    def excluir_produto(self):
        nome = simpledialog.askstring("Exclusão", "Nome do produto a ser excluído:")
        if nome:
            resultado = self.estoque.excluir_produto(nome)
            messagebox.showinfo("Resultado da Exclusão", resultado)

    def alterar_produto(self):
        nome = simpledialog.askstring("Alteração", "Nome do produto a ser alterado:")
        if nome:
            novo_nome = simpledialog.askstring("Alteração", "Novo nome do produto:")
            novo_preco = simpledialog.askfloat("Alteração", "Novo preço do produto:")
            nova_quantidade = simpledialog.askinteger("Alteração", "Nova quantidade em estoque:")
            if novo_nome and novo_preco is not None and nova_quantidade is not None:
                resultado = self.estoque.alterar_produto(nome, novo_nome, novo_preco, nova_quantidade)
                messagebox.showinfo("Resultado da Alteração", resultado)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
