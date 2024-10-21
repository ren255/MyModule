import time,os

from langchain_community.chat_models import ChatOpenAI
from typing import Optional


class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(
        self,
        model_name: str,
        openai_api_key: Optional[str] = None,
        openai_api_base: str = "https://openrouter.ai/api/v1",
        **kwargs
    ):
        openai_api_key = openai_api_key or os.getenv("OPENROUTER_API_KEY")
        super().__init__(
            openai_api_base=openai_api_base,
            openai_api_key=openai_api_key,
            model_name=model_name,
            **kwargs
        )

from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenRouter(
    model_name="qwen/qwen-2.5-7b-instruct"
)
prompt = ChatPromptTemplate.from_template("")
openrouter_chain = prompt | llm

result = openrouter_chain.invoke({})
print(result.content)

