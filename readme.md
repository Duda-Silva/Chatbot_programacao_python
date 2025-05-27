# 💬 Chatbot de Programação com SQLite e Tkinter
Este projeto é um chatbot educacional em Python focado em responder dúvidas sobre programação. Ele possui uma base de dados local com explicações e exemplos sobre diversos conceitos da linguagem Python, apresentados por meio de uma interface gráfica construída com Tkinter.

## 🧠 Funcionalidades
- Interface gráfica para interação com o usuário.

- Base de dados com conceitos organizados por tópicos e níveis (básico, intermediário, avançado).

- Registro de interações do usuário para futura análise de uso.

- Retorno de explicações e exemplos práticos com base na pergunta feita.

- Integração com banco de dados SQLite.

## 🛠️ Tecnologias Utilizadas
- Python 3.x

- SQLite3

- Tkinter (GUI)

- datetime, messagebox e scrolledtext (módulos padrão do Python)

## 📦 Instalação
- Clone este repositório ou copie os arquivos para seu ambiente local.

- Execute o script Python:
Certifique-se de que você possui Python instalado (versão 3.6 ou superior).

## ✅ Como Usar
- Inicie o programa.

- Digite uma pergunta sobre programação (ex: "O que é uma função lambda?").

- O chatbot buscará na base de dados e responderá com uma explicação e exemplo.

- O histórico das interações é salvo automaticamente no banco de dados chatbot.db.

## 🗃️ Estrutura do Banco de Dados
- conceito_programacao: contém os conceitos, exemplos e níveis de dificuldade.

- interacoes_usuario: registra perguntas feitas, respostas geradas, data/hora e se a resposta foi útil.

## 📌 Exemplos de Perguntas
- Como funciona o if-else em Python?

- O que é herança na programação orientada a objetos?

- Para que serve o Flask?

## ⚠️ Observações
A busca por respostas é feita de forma simples, com base na ocorrência de palavras-chave.

A inserção dos dados é feita automaticamente na primeira execução do código.

O botão "Perguntar" envia a pergunta e exibe a resposta no campo inferior.

## 📜 Licença
Este projeto é de uso educacional e livre para modificações.

