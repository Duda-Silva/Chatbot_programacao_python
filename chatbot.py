import sqlite3
import tkinter as tk
from tkinter import scrolledtext
from tkinter import scrolledtext, messagebox # Importa messagebox para mensagens de erro/confirmação
from datetime import datetime # Para obter a data e hora atual

# Configuração do banco de dados
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()



# Criando tabela para armazenar conceitos de programação
cursor.execute("""
    CREATE TABLE IF NOT EXISTS conceito_programacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topico TEXT NOT NULL,
        termo TEXT NOT NULL,
        explicacao text NOT NULL,
        exemplo text,
        nivel TEXT NOT NULL
    )
    """)

    # Criando tabela para estatísticas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS interacoes_usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TEXT NOT NULL,
        pergunta_usuario TEXT NOT NULL,
        resposta_chatbot TEXT NOT NULL,
        foi_util INTEGER, 
        conceito_associado integer,
        FOREIGN KEY (conceito_associado) REFERENCES conceito_programacao(id)
    )
    """)

conn.commit()

respostas = [
    ('Estruturas de Controle', 'O que a estrutura condicional "if" permite fazer em Python?', 'Permite a execução condicional de um bloco de código.', 'if x > 0:\n    print("Positivo")', 'Básico'),
    ('Estruturas de Controle', 'Qual a diferença entre "if" e "if-else" em Python?', 'Permite executar diferentes blocos de código com base em uma condição.', 'if x > 0:\n    print("Positivo")\nelse:\n    print("Negativo")', 'Básico'),
    ('Estruturas de Controle', 'Como o loop "for" funciona em Python?', 'Executa um bloco de código repetidamente por um número definido de vezes.', 'for i in range(10):\n    print(i)', 'Intermediário'),
    ('Estruturas de Controle', 'Quando utilizar o loop "while" em vez de "for"?', 'Executa um bloco de código enquanto a condição for verdadeira.', 'x = 0\nwhile x < 5:\n    print(x)\n    x += 1', 'Intermediário'),
    ('Estruturas de Controle', 'Para que serve a instrução "break" em um loop?', 'Interrompe um loop prematuramente.', 'for i in range(10):\n    if i == 5:\n        break\n    print(i)', 'Intermediário'),
    ('Estruturas de Controle', 'Qual o efeito da instrução "continue" dentro de um loop?', 'Pula uma iteração específica de um loop.', 'for i in range(10):\n    if i == 5:\n        continue\n    print(i)', 'Intermediário'),
    ('Estruturas de Dados', 'O que é uma lista em Python e como ela é declarada?', 'Estrutura de dados que armazena múltiplos valores de diferentes tipos.', 'numeros = [1, 2, 3, 4, 5]', 'Básico'),
    ('Estruturas de Dados', 'Qual a principal característica de uma tupla em Python?', 'Estrutura de dados imutável que armazena múltiplos valores.', 'dados = (1, 2, 3, "Texto")', 'Básico'),
    ('Estruturas de Dados', 'Como um dicionário funciona em Python?', 'Estrutura de dados que armazena pares de chave e valor.', 'alunos = {"Alice": 8, "Bob": 9, "Carol": 7}', 'Intermediário'),
    ('Estruturas de Dados', 'Para que serve um conjunto em Python e qual sua principal característica?', 'Estrutura de dados que não permite duplicatas.', 'numeros = {1, 2, 3, 3, 4}', 'Intermediário'),
    ('Funções', 'Como se define uma função simples em Python?', 'Cria uma função reutilizável.', 'def saudacao():\n    print("Olá!")', 'Básico'),
    ('Funções', 'Qual é o papel dos parâmetros em uma função?', 'Permite passar valores para uma função.', 'def soma(a, b):\n    return a + b', 'Intermediário'),
    ('Funções', 'O que é uma função lambda e quando ela é usada?', 'Cria funções anônimas.', 'quadrado = lambda x: x * x', 'Intermediário'),
    ('POO', 'Como se define uma classe em Python?', 'Define uma estrutura de classe em Python.', 'class Pessoa:\n    def __init__(self, nome):\n        self.nome = nome', 'Intermediário'),
    ('POO', 'O que é um objeto em programação orientada a objetos?', 'Instância de uma classe.', 'p = Pessoa("Alice")', 'Intermediário'),
    ('POO', 'O que é herança em programação orientada a objetos?', 'Permite que uma classe adquira propriedades e comportamentos de outra classe.', 'class Animal:\n    def som(self):\n        print("Som genérico")\n\nclass Cachorro(Animal):\n    def som(self):\n        print("Latido")', 'Avançado'),
    ('POO', 'O que significa polimorfismo em POO?', 'Permite que métodos tenham comportamentos diferentes dependendo da classe.', 'class Forma:\n    def area(self):\n        return 0\n\nclass Quadrado(Forma):\n    def area(self):\n        return lado * lado', 'Avançado'),
    ('POO', 'Como o encapsulamento protege os dados de um objeto?', 'Restringe o acesso direto aos dados.', 'class Conta:\n    def __init__(self, saldo):\n        self.__saldo = saldo', 'Avançado'),
    ('Banco de Dados', 'O que é o SQLite e como ele é utilizado em Python?', 'Banco de dados embutido em Python.', 'import sqlite3\nconn = sqlite3.connect("banco.db")', 'Intermediário'),
    ('Banco de Dados', 'Qual é a função de uma chave primária em um banco de dados?', 'Identificador único de um registro em uma tabela.', 'CREATE TABLE usuarios (\n    id INTEGER PRIMARY KEY,\n    nome TEXT\n);', 'Intermediário'),
    ('Tratamento de Erros', 'Como o bloco try-except trata erros em Python?', 'Captura e trata erros no código.', 'try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print("Erro!")', 'Intermediário'),
    ('Manipulação de Arquivos', 'Como se faz a leitura de arquivos em Python?', 'Lê o conteúdo de um arquivo.', 'with open("arquivo.txt") as f:\n    conteudo = f.read()', 'Intermediário'),
    ('Manipulação de Arquivos', 'Como escrever dados em arquivos usando Python?', 'Escreve dados em um arquivo.', 'with open("arquivo.txt", "w") as f:\n    f.write("Texto")', 'Intermediário'),
    ('Módulos', 'Como importar módulos em Python?', 'Importa funcionalidades externas.', 'import math\nprint(math.sqrt(16))', 'Básico'),
    ('Módulos', 'Como criar e utilizar um módulo próprio em Python?', 'Define um módulo próprio.', '# modulo.py\ndef saudacao():\n    print("Olá!")', 'Intermediário'),
    ('Expressões Regulares', 'O que são expressões regulares e para que servem?', 'Manipula padrões em strings.', 'import re\nresultado = re.search(r"\d+", "123abc")', 'Avançado'),
    ('Threads', 'Como criar uma thread em Python?', 'Executa tarefas simultaneamente.', 'import threading\ndef tarefa():\n    print("Executando")\nt = threading.Thread(target=tarefa)\nt.start()', 'Avançado'),
    ('Desenvolvimento Web', 'Para que serve o framework Flask em Python?', 'Criação de APIs web.', 'from flask import Flask\napp = Flask(__name__)\n@app.route("/")\ndef home():\n    return "Olá, mundo!"', 'Avançado'),
    ('Automação', 'Como ler arquivos Excel com Python?', 'Manipula planilhas.', 'import pandas as pd\ndf = pd.read_excel("dados.xlsx")', 'Avançado')
]

for topico, termo, explicacao, exemplo, nivel in respostas:
    cursor.execute("INSERT INTO conceito_programacao (topico, termo, explicacao, exemplo, nivel) VALUES (?, ?, ?, ?, ?)", (topico, termo, explicacao, exemplo, nivel))
conn.commit()

# Função para obter resposta do chatbot
def obter_resposta(pergunta):
    # Normalizando a pergunta para facilitar a busca
    pergunta = pergunta.lower()
    cursor.execute("SELECT explicacao, exemplo FROM conceito_programacao WHERE LOWER(termo) LIKE ?", (f"%{pergunta}%",))
    resultado = cursor.fetchone()

    if resultado:
        
        explicacao, exemplo = resultado
        resposta = f"📚Explicação: {explicacao}\n💡Exemplo: {exemplo if exemplo else 'Nenhum exemplo disponível.\n'}"

        # Registrando a interação do usuário na tabela interacoes_usuario
        cursor.execute("""
            INSERT INTO interacoes_usuario (data_hora, pergunta_usuario, resposta_chatbot, foi_util, conceito_associado)
            VALUES (datetime('now'), ?, ?, NULL, 
                    (SELECT id FROM conceito_programacao WHERE Lower(termo) LIKE ? LIMIT 1))
            """, (pergunta, resposta, f"%{pergunta}%"))
            
        conn.commit()

        # Obter o ID da interação recém-inserida
        cursor.execute("SELECT id FROM interacoes_usuario ORDER BY id DESC LIMIT 1")
        interacao_id = cursor.fetchone()[0]

        return resposta, interacao_id
    else:
        return "Não encontrei uma resposta para essa pergunta. Talvez você possa reformular?", None


# Função chamada ao clicar no botão
def enviar_pergunta():
    pergunta = entrada.get()
    if not pergunta.lower():
        messagebox.showwarning("Aviso", "Digite uma pergunta.")
        return
    resposta = obter_resposta(pergunta)
    txt_resposta.config(state='normal')
    txt_resposta.delete("1.0", tk.END)
    txt_resposta.insert(tk.END, resposta)
    txt_resposta.config(state='disabled')
    


# Interface gráfica
janela = tk.Tk()
janela.title("Chatbot de Programação")
janela.geometry("800x450")

label_titulo = tk.Label(janela, text="Chatbot de Programação", font=("Arial", 16, "bold"))
label_titulo.pack(pady=5)

entrada = label_instrucao = tk.Label(janela, text="Digite sua pergunta sobre programação(ou 'sair' para encerrar):")
label_instrucao.pack()
if entrada.lower() == 'sair':
    janela.destroy()
    
entrada = tk.Entry(janela, width=60)
entrada.pack(pady=5)
#botão para enviar a pergunta
btn_enviar = tk.Button(janela, text="Perguntar", command=enviar_pergunta)
btn_enviar.pack(pady=5)
  
txt_resposta = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=10, state='disabled')
txt_resposta.pack(pady=10)

janela.mainloop()




