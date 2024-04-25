from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.gigachat import GigaChatEmbeddings
from config_data.config import AU_DATA
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import Tool


embeddings = GigaChatEmbeddings(credentials=AU_DATA, scope="GIGACHAT_API_CORP", verify_ssl_certs=False)


def get_retrieval_tool(url: str) -> Tool:
    loader = WebBaseLoader(url, encoding='utf-8')
    docs = loader.load()
    documents = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200
    ).split_documents(docs)
    db = FAISS.from_documents(documents, embeddings)
    # retriever = vector.as_retriever()

    return db

    retriever_tool = create_retriever_tool(
        retriever,
        "data_search",
        "Поиск определенных данных по содержимому сайта",
    )

    return retriever_tool
