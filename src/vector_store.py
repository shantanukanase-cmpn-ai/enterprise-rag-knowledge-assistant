from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vectorstore(documents,persist_directory='db'):
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
