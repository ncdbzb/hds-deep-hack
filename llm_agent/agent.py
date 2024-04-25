from config_data.config import AU_DATA
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_gigachat_functions_agent
from langchain_community.chat_models.gigachat import GigaChat
from llm_agent.retrieval_tool import get_retrieval_tool
from langchain_core.tools import tool
from langchain import hub


def get_agent_response(user_query: str):
    giga = GigaChat(credentials=AU_DATA, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")

    @tool
    def multiply(first_int: int, second_int: int) -> int:
        """Multiply two integers together."""
        return first_int * second_int

    llm_with_tools = giga.bind_tools([multiply])
    msg = llm_with_tools.invoke("whats 5 times forty two")
