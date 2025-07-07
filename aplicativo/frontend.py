import tkinter as tk
from tkinter import messagebox
from backend import Backend

class FrontendGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Torneios de eSports")
        self.app = Backend()

        self.menu_principal()

    def limpar_janela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpar_janela()
        tk.Label(self.master, text="Sistema de Torneios", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.master, text="Cadastrar Jogador", width=30, command=self.tela_cadastrar_jogador).pack(pady=5)
        tk.Button(self.master, text="Registrar Partida", width=30, command=self.tela_registrar_partida).pack(pady=5)
        tk.Button(self.master, text="Ver Partidas Realizadas", width=30, command=self.ver_partidas_realizadas).pack(pady=5)
        tk.Button(self.master, text="Ver Partidas Pendentes", width=30, command=self.ver_partidas_pendentes).pack(pady=5)
        tk.Button(self.master, text="Sair", width=30, command=self.master.quit).pack(pady=10)

    def tela_cadastrar_jogador(self):
        self.limpar_janela()
        tk.Label(self.master, text="Cadastro de Jogador", font=("Arial", 14)).pack(pady=10)

        campos = ["Nome", "Idade", "Telefone", "Email", "Participações", "ID do Time (opcional)"]
        entradas = []

        for campo in campos:
            tk.Label(self.master, text=campo).pack()
            entrada = tk.Entry(self.master)
            entrada.pack()
            entradas.append(entrada)

        def salvar_jogador():
            try:
                nome = entradas[0].get()
                idade = int(entradas[1].get())
                telefone = entradas[2].get()
                email = entradas[3].get()
                participacoes = entradas[4].get()
                id_time = entradas[5].get()
                id_time = int(id_time) if id_time.strip() else None

                self.app.cadastrar_jogador(nome, idade, telefone, email, participacoes, id_time)
                messagebox.showinfo("Sucesso", "Jogador cadastrado com sucesso!")
                self.menu_principal()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar jogador: {e}")

        tk.Button(self.master, text="Salvar", command=salvar_jogador).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.menu_principal).pack()

    def tela_registrar_partida(self):
        self.limpar_janela()
        tk.Label(self.master, text="Registro de Partida", font=("Arial", 14)).pack(pady=10)

        campos = ["Data (YYYY-MM-DD)", "ID Time 1", "ID Time 2", "Vencedor (opcional)"]
        entradas = []

        for campo in campos:
            tk.Label(self.master, text=campo).pack()
            entrada = tk.Entry(self.master)
            entrada.pack()
            entradas.append(entrada)

        def salvar_partida():
            try:
                data = entradas[0].get()
                id_time1 = int(entradas[1].get())
                id_time2 = int(entradas[2].get())
                vencedor = entradas[3].get()
                vencedor = vencedor if vencedor.strip() else None

                self.app.registrar_partida(data, id_time1, id_time2, vencedor)
                messagebox.showinfo("Sucesso", "Partida registrada com sucesso!")
                self.menu_principal()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao registrar partida: {e}")

        tk.Button(self.master, text="Salvar", command=salvar_partida).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.menu_principal).pack()

    def ver_partidas_realizadas(self):
        partidas = self.app.listar_partidas_concluidas()
        if not partidas:
            messagebox.showinfo("Informação", "Nenhuma partida concluída.")
            return

        texto = "\n".join([f"{d} - {t1} vs {t2} | Vencedor: {v}" for d, t1, t2, v in partidas])
        messagebox.showinfo("Partidas Concluídas", texto)

    def ver_partidas_pendentes(self):
        partidas = self.app.listar_partidas_pendentes()
        if not partidas:
            messagebox.showinfo("Informação", "Nenhuma partida pendente.")
            return

        texto = "\n".join([f"{d} - {t1} vs {t2}" for d, t1, t2 in partidas])
        messagebox.showinfo("Partidas Pendentes", texto)