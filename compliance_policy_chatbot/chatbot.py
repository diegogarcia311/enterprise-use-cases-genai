from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from memory_with_logging import CustomMemory

llm = ChatOpenAI()
memory = CustomMemory()

chat = ConversationChain(llm=llm, memory=memory)

while True:
    prompt = input("🧑‍💼 You: ")
    print("🤖 Bot:", chat.run(prompt))
