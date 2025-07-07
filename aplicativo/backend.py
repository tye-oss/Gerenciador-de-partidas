import sqlite3
import os
from criacao import criar_tabelas

class Backend:
    def __init__(self):
        base_path = os.path.dirname(__file__)
        self.caminho_banco = os.path.join(base_path, "vem no fut vem", "db", "torneio.db")
        criar_tabelas()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    # Exemplo de função
    def cadastrar_jogador(self, nome, idade, telefone, email, participacoes="", id_time=None):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO jogadores (nome_jogador, idade, telefone, email, participacoes, id_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, idade, telefone, email, participacoes, id_time))
        conexao.commit()
        conexao.close()

    # ⚔️ Registrar uma partida
    def registrar_partida(self, data, id_time1, id_time2, vencedor=None):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO competicoes (data, id_time1, id_time2, vencedor)
            VALUES (?, ?, ?, ?)
        """, (data, id_time1, id_time2, vencedor))
        conexao.commit()
        conexao.close()

    # 🧾 Ver partidas já disputadas
    def listar_partidas_concluidas(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT c.data, t1.nome_time, t2.nome_time, c.vencedor
            FROM competicoes c
            JOIN times t1 ON c.id_time1 = t1.id_time
            JOIN times t2 ON c.id_time2 = t2.id_time
            WHERE c.vencedor IS NOT NULL
        """)
        resultados = cursor.fetchall()
        conexao.close()
        return resultados

    # 📅 Ver partidas futuras (sem vencedor definido ainda)
    def listar_partidas_pendentes(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT c.data, t1.nome_time, t2.nome_time
            FROM competicoes c
            JOIN times t1 ON c.id_time1 = t1.id_time
            JOIN times t2 ON c.id_time2 = t2.id_time
            WHERE c.vencedor IS NULL
        """)
        partidas = cursor.fetchall()
        conexao.close()
        return partidas

    

    