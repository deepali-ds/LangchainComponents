from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions=32)

docs =[
    "Washington DC is the capital of USA",
    "Rome is the capital of Italy",
    "Paris is the capital of France"
]

result = embedding.embed_documents(docs)

print(str(result))