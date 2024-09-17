from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM
from Content.content1 import getContent

"""
* = All


"""

llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=Provider.MetaAI
)

content = getContent("https://www.shiksha.com/college/st-mary-s-college-kottayam-194551")

template = f"""
 rewrite the below content
 {content}
 Note: Output should be in json
"""

print(llm.invoke(template))
