from config_data.config import AU_DATA
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_gigachat_functions_agent
from langchain_community.chat_models.gigachat import GigaChat
from llm_agent.retrieval_tool import get_retrieval_tool
from langchain import hub


def get_agent_response(user_query: str):
    giga = GigaChat(credentials=AU_DATA, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")

    retriever_tool = get_retrieval_tool('https://mc21.ru/blog/shchitovidka-i-zuby-kakaya-svyaz-mezhdu-patologiey-polosti-rta-i-shchitovidnoy-zhelezy/')
    tools = [retriever_tool]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Ты полезный ассистент, который помогает найти ответы на вопросы",
            ),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_gigachat_functions_agent(giga, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    result = agent_executor.invoke({"input": user_query})["output"]

    return result
