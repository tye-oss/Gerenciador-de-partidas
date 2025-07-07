"""
Sistema de Gerenciamento de Torneios de eSports 🎮
---------------------------------------------------
Este sistema permite:
- Cadastrar jogadores
- Registrar partidas entre times
- Consultar partidas realizadas e partidas futuras

Estrutura:
- backend.py: regras e acesso ao banco de dados
- criacao.py: cria o banco e as tabelas necessárias
- frontend.py: interface gráfica usando Tkinter
- main.py: ponto de entrada da aplicação

Banco:
- Utiliza SQLite (arquivo torneio.db)
- Banco salvo na pasta 'vem no fut vem/db/'

Tabelas:
- categorias_jogo: categorias de jogos
- times: times participantes
- time_categoria: relação N:N entre times e categorias
- jogadores: dados dos jogadores (ligados a times)
- competicoes: registros das partidas (data, times, vencedor)
- jogadores_partida: jogadores que participaram das competições
"""