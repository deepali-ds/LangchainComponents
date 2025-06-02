from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')

result = model.invoke("Write a 5 line poem on ChatGPT", temperature=0.5, max_completion_tokens= 50)

print(result.content)