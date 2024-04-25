from bs4 import BeautifulSoup
import requests
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_extraction_chain


def get_body(url: str) -> str:
    response = requests.get(url)

    body_text = ''
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        body_tag = soup.find('body')

        if body_tag:
            body_text = body_tag.get_text()[:5000]
            print(len(body_text))

    return body_text
