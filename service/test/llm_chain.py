"""LLM Chain specifically for generating examples for QCM (Question Choix Multiples) answering."""
from __future__ import annotations

from typing import Any

from langchain.chains.llm import LLMChain
from langchain.llms.base import BaseLLM
from langchain.output_parsers.regex import RegexParser
from langchain.prompts import PromptTemplate
from langchain.vectorstores.base import VectorStore

template = """You are a teacher preparing questions for a quiz. Given the following document, please generate 10 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document.The response only bellow example 

''Example:
Question1: What is the individual's name who stated they want to be a DevOps Engineer?
CHOICE_A: Huynh Ngoc Huy
CHOICE_B: VietHan Korea
CHOICE_C: DevOps Engineer
CHOICE_D: Feature
Answer: A''

<Begin Document>
{doc}
<End Document>"""



output_parser = RegexParser(
    regex=r"Question\s?\d+:\s+(.*?)\nCHOICE_A: (.*?)\nCHOICE_B: (.*?)\nCHOICE_C: (.*?)\nCHOICE_D: (.*?)(?:\n)+Answer:\s?(.*)\n\nQuestion\s?\d+:\s+(.*?)\nCHOICE_A: (.*?)\nCHOICE_B: (.*?)\nCHOICE_C: (.*?)\nCHOICE_D: (.*?)(?:\n)+Answer:\s?(.*)",
    output_keys=["Question1", "A_1", "B_1", "C_1", "D_1", "reponse1", "question2", "A_2", "B_2", "C_2", "D_2", "reponse2"]
)

PROMPT = PromptTemplate(
    input_variables=["doc"],template=template
)

class QCMGenerateChain(LLMChain):
    """LLM Chain specifically for generating examples for QCM answering."""

    @classmethod 
    def from_llm(cls, llm: BaseLLM, **kwargs: Any) -> QCMGenerateChain:
        print("Hello QCM chain")
        """Load QA Generate Chain from LLM."""
        return cls(llm=llm, prompt=PROMPT, **kwargs)