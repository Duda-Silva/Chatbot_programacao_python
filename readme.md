# 🤖 Chatbot de Programação com Interface Gráfica (Tkinter)
Este projeto é um chatbot educativo desenvolvido em Python com Tkinter que responde dúvidas sobre programação. Ele utiliza banco de dados SQLite para armazenar conceitos, exemplos, interações com o usuário e agora conta com busca semântica em arquivos PDF.

## 📌 Funcionalidades
- ✅ Interface gráfica com Tkinter.

- ✅ Base de conhecimento armazenada em SQLite (conceito_programacao).

- ✅ Registro de interações do usuário (interacoes_usuario).

- ✅ Respostas com explicações e exemplos de código.

- ✅ Mensagens de aviso e validação de entrada.

- ✅ Busca de respostas diretamente de um arquivo PDF usando embeddings semânticos com sentence-transformers.

## 🛠️ Tecnologias Utilizadas
- Python 3.x

- SQLite3

- Tkinter (GUI)

- datetime, messagebox e scrolledtext (módulos padrão do Python)

- sentence-transformers, pymupdf, scrolledtext

## 📦 Instalação
- Clone este repositório ou copie os arquivos para seu ambiente local.

instalção no promp: pip install sentence-transformers pymupdf

- Execute o script Python:
Certifique-se de que você possui Python instalado (versão 3.6 ou superior).

## ✅ Como Usar
- Inicie o programa.

- Digite uma pergunta sobre programação (ex: "O que é uma função lambda?").

- E escolhar entre Perguntar no Banco de Dados ou Perguntar no PDF.

- O chatbot buscará na base de dados ou PDF e responderá com uma explicação e exemplo.

- O histórico das interações é salvo automaticamente no banco de dados chatbot.db.

## 🗂 Organização
- chatbot.py: Arquivo principal com interface gráfica, lógica e banco de dados.

- chatbot.db: Banco de dados SQLite (gerado automaticamente na primeira execução).

caminho_pdf: Arquivo PDF utilizado como base alternativa de conhecimento.

## 🗃️ Estrutura do Banco de Dados
- conceito_programacao: contém os conceitos, exemplos e níveis de dificuldade.

- interacoes_usuario: registra perguntas feitas, respostas geradas, data/hora e se a resposta foi útil.

## 📌 Exemplos de Perguntas do Banco 
O que é uma lista em Python e como ela é declarada?

Qual a principal característica de uma tupla em Python?

Como um dicionário funciona em Python?

Para que serve um conjunto em Python e qual sua principal característica?

Como se define uma função simples em Python?

Qual é o papel dos parâmetros em uma função?

## ⚠️ Observações
A busca por respostas é feita de forma simples, com base na ocorrência de palavras-chave.

A inserção dos dados é feita automaticamente na primeira execução do código.

O botão "Perguntar" envia a pergunta e exibe a resposta no campo inferior.

## 📜 Licença
Este projeto é de uso educacional e livre para modificações.

