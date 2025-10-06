import os
import PyPDF2
from openai import OpenAI
import faiss
import numpy as np

# Configuração da OpenAI
client = OpenAI(api_key="SUA_API_KEY_AQUI")

# Função para ler PDFs
def ler_pdfs(pasta):
    textos = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)
            with open(caminho, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                texto = ""
                for page in reader.pages:
                    texto += page.extract_text()
                textos.append(texto)
    return textos

# Função para criar embeddings
def criar_embeddings(textos):
    embeddings = []
    for t in textos:
        resp = client.embeddings.create(
            input=t,
            model="text-embedding-3-small"
        )
        embeddings.append(resp.data[0].embedding)
    return np.array(embeddings, dtype="float32")

# Inicializa FAISS
def criar_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

# Função para buscar respostas
def buscar_resposta(pergunta, index, textos):
    embedding_pergunta = client.embeddings.create(
        input=pergunta,
        model="text-embedding-3-small"
    ).data[0].embedding
    embedding_pergunta = np.array([embedding_pergunta], dtype="float32")
    D, I = index.search(embedding_pergunta, k=1)
    return textos[I[0][0]]

# Executando
if __name__ == "__main__":
    textos = ler_pdfs("inputs")
    embeddings = criar_embeddings(textos)
    index = criar_index(embeddings)

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        resposta = buscar_resposta(pergunta, index, textos)
        print("Chatbot:", resposta[:500])  # mostra os primeiros 500 caracteres
