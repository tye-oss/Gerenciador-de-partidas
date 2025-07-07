import sqlite3
import os

def criar_tabelas():
    base_path = os.path.dirname(__file__)
    pasta_banco = os.path.join(base_path, "db")
    os.makedirs(pasta_banco, exist_ok=True)  # ✅ Cria a pasta se não existir

    caminho_banco = os.path.join(pasta_banco, "torneio.db")
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    # Criação das tabelas (mantidas conforme seu original)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias_jogo (
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_categoria TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS times (
            id_time INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_time TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS time_categoria (
            id_time INTEGER,
            id_categoria INTEGER,
            PRIMARY KEY (id_time, id_categoria),
            FOREIGN KEY (id_time) REFERENCES times(id_time),
            FOREIGN KEY (id_categoria) REFERENCES categorias_jogo(id_categoria)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id_jogador INTEGER PRIMARY KEY AUTOINCREMENT,
            id_time INTEGER,
            nome_jogador TEXT NOT NULL,
            participacoes TEXT,
            idade INTEGER NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            FOREIGN KEY (id_time) REFERENCES times(id_time)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competicoes (
            id_competicao INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            id_time1 INTEGER,
            id_time2 INTEGER,
            vencedor TEXT,
            FOREIGN KEY (id_time1) REFERENCES times(id_time),
            FOREIGN KEY (id_time2) REFERENCES times(id_time)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores_partida (
            id_participacao INTEGER PRIMARY KEY AUTOINCREMENT,
            id_competicao INTEGER,
            id_jogador INTEGER,
            FOREIGN KEY (id_competicao) REFERENCES competicoes(id_competicao),
            FOREIGN KEY (id_jogador) REFERENCES jogadores(id_jogador)
        )
    """)

    conexao.commit()
    conexao.close()
