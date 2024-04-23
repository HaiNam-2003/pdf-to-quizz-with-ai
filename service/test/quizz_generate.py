    
from llm_chain import QCMGenerateChain
from llm import QaLlm
from langchain.llms.base import BaseLLM
import asyncio

async def llm_call(qa_chain: QCMGenerateChain, text: str):
    
    print(f"llm call running...")
    print(text)
    batch_examples = await qa_chain.ainvoke(text)
    print(f"llm call done.")

    return batch_examples

async def generate_quizz(content:str):
    """
    Generates a quizz from the given content.
    """
    print("hello quizz")
    qa_llm = QaLlm()
    qa_chain = QCMGenerateChain.from_llm(qa_llm.get_llm())
    print(f"huy {content}")
    print("hello quizz 2")
    return await llm_call(qa_chain, [{"doc": "My name is huy"}])
    