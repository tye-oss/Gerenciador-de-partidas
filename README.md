# 🕹️ Sistema de Gerenciamento de Torneios de eSports

Este é um sistema desktop simples para gerenciamento de torneios de eSports, desenvolvido em Python com interface gráfica utilizando Tkinter e banco de dados SQLite.

## 📌 Funcionalidades

- 📋 Cadastro de jogadores (com nome, idade, telefone, e-mail e time)
- ⚔️ Registro de partidas entre dois times
- 🧾 Consulta de partidas realizadas (com vencedor)
- 📅 Consulta de partidas futuras (pendentes)

## 🗃️ Estrutura do Projeto

vem-no-fut-vem/
│
├── backend.py # Lógica de banco de dados e regras de negócio
├── criacao.py # Criação das tabelas do banco de dados
├── frontend.py # Interface gráfica (Tkinter)
├── main.py # Ponto de entrada da aplicação
├── vem no fut vem/
│ └── db/
│ └── torneio.db # Banco de dados SQLite (criado automaticamente)
├── README.md # Este arquivo

bash
Copiar
Editar

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
(Opcional) Crie um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências (nenhuma externa obrigatória para esse projeto):

bash
Copiar
Editar
pip install -r requirements.txt  # Arquivo opcional se você for usar dependências futuras
Execute a aplicação:

bash
Copiar
Editar
python main.py
🏗️ Tecnologias Utilizadas
Python 3.x

Tkinter (GUI nativa do Python)

SQLite (banco de dados leve e local)

os e sqlite3 (bibliotecas padrão)

📂 Banco de Dados
O banco torneio.db será criado automaticamente na pasta vem no fut vem/db/ na primeira execução. Ele contém as seguintes tabelas:

jogadores

times

categorias_jogo

time_categoria

competicoes

jogadores_partida

📝 Exemplo de Uso
Abra o programa e clique em "Cadastrar Jogador" para inserir dados.

Registre partidas com IDs dos times e data.

Consulte partidas realizadas ou pendentes por meio de popups.

📌 Observações
O campo "Vencedor" pode ser deixado em branco ao registrar partidas futuras.

IDs de times devem existir previamente no banco de dados.

A interface é simples, mas funcional — ideal para evoluir para versões com mais funcionalidades como: criação de times, categorias, ou rankings.

🛡️ Licença
Este projeto é de uso livre para fins educacionais e pessoais. Para uso comercial, verifique a licença ou entre em contato com o autor.

Feito com um teclado barulhento, muito café e zero sono. 🚀☕