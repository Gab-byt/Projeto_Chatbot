Chatbot Baseado em PDFs 📊

Visão Geral

Este projeto consiste em um chat interativo que responde perguntas com base no conteúdo de arquivos PDF. Ele utiliza IA e embeddings para interpretar os documentos e fornecer respostas relevantes, simulando um assistente virtual personalizado.

Objetivo do Projeto

Carregar PDFs com informações relevantes.

Implementar busca vetorial para indexar e recuperar informações.

Gerar respostas baseadas no conteúdo dos PDFs.

Criar um chat interativo para fazer perguntas e receber respostas fundamentadas.
--------------------------------------------------------------------------------------
Estrutura do Projeto
chatbot-pdf/
|
├─ inputs/             
│   └─ exemplo.pdf
├─ main.py             
├─ requirements.txt    
└─ README.md           
-----------------------------------------------------------------------------------------------------------
Como Rodar

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


Entre na pasta do projeto:

cd chatbot-pdf


Crie e ative um ambiente virtual (opcional, mas recomendado):

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python -m venv venv
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Coloque seus PDFs na pasta inputs.

Execute o chatbot:

python main.py


Digite perguntas no terminal e receba respostas. Para sair, digite sair, exit ou quit.


