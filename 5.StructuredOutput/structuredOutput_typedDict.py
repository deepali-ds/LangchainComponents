from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(TypedDict):
    summary: Annotated[str, "Write  a brief summary of the review"]
    sentiment: Annotated[str, "Return the sentiment of the review either positive, negative or neutral"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Absolutely love this ladies bracelet! The rose gold finish gives it a chic and elegant look, perfect for both everyday wear and special occasions. It's lightweight, comfortable, and the adjustable clasp ensures a perfect fit. The tiny sparkling stones add just the right touch of glamour without being over the top. It also came beautifully packaged, making it a great gift option. Highly recommended for anyone looking for a stylish yet affordable accessory!""") 

print(result)
print(result['summary'])
print(result['sentiment'])