from config_data.config import AU_DATA
from langchain_community.chat_models.gigachat import GigaChat
from llm_agent.utils.web_parser import get_body
from langchain.chains import create_extraction_chain
import pprint


def get_answer(url: str):
    giga = GigaChat(credentials=AU_DATA, verify_ssl_certs=False, scope="GIGACHAT_API_CORP", model='GigaChat-Pro', profanity_check=False, temperature=0, verbose=True)

    parsed_text = get_body(url)

    prompt = f"""
        Тебе предоставлен текст с веб-страницы, который послужил основой для написания научной статьи.
        Твоя задача состоит в определении типа веб-страницы, по содержащейся информации в данном тексте и в извлечении названия статьи,авторов статьи,года написания статьи из данного текста. Текст:{parsed_text}
        Максимальная длина ответа: 5 слов.
        Думай пошагово.
        Ответ дай строго в виде: Название статьи : тип -- автор, год написания -- URL : {url}, (дата обращения: 24.04.2024) — Текст : электронный.
        """

    return giga.invoke(prompt).content
