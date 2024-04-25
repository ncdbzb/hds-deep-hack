from config_data.config import AU_DATA
from langchain_community.chat_models.gigachat import GigaChat
from llm_agent.utils.web_parser import get_body
from langchain.chains import create_extraction_chain
import pprint


def get_answer(url: str):
    giga = GigaChat(credentials=AU_DATA, verify_ssl_certs=False, scope="GIGACHAT_API_CORP", model='GigaChat-Pro', profanity_check=False, verbose=True)

    prompt = (f'Тебе дан текст с сайта, который использовался для написания научной статьи. Тебе нужно извлечь название статьи. Текст:{get_body(url)}')

    return giga.invoke(prompt).content
