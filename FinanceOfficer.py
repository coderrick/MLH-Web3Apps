from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferWindowMemory
from Key import key


def chatbot(user_input):
    llm = ChatOpenAI(api_key = key)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a financial tax refund specialist. You will recieve an income value from the W2 form, and to the best of your ability will calculate the refund tax for the user: Start by deducting 12550 from the income, and the refund will be the income tax of the (income - 12550) subtracted from a multiple of 5000 depending on how high the income tax is. Your response should ONLY be a number. "),
        ("user", "{input}")
    ])
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return(chain.invoke({"input": user_input}))
    

memory = ConversationBufferWindowMemory(k = 20)



#conversation = ConversationChain(llm=llm)
'''while True:
    user_input = input("User: ")
    if user_input in ['quit', 'exit']:
        break
    chatbot(user_input)'''

chatbot("50000")







