from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', """You are a helpful {domain} expert. 
                Be precise, factual, and neutral."""),
    ('human', 'Explain me the basics of {subject}')
])

prompt = chat_template.invoke({
    'domain':'AI',
    'subject':'Machine Learning'
})

print(prompt)