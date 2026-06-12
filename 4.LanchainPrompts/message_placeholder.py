from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful AI Assistant"),
    MessagePlaceholder(variable_name="messages"),
    ('human', '{question}')
])

chat_history = []
# load chat history
with open('chat_history.txt')

prompt = chat_template.invoke({
    "messages":[
        "HumanMessage(content='Hi, my name is Arpit')",
        "AIMessage(content='Hi Arpit, how are you?')"
    ],
    'question':"What is LangChain?"
})