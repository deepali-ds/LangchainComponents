from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in review list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return the sentiment of the review either positive or negative"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside the list"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Recently added three lovely bracelets to my collection, and each has its own charm. First, the Rose Gold Adjustable Bracelet dazzles with its warm hue and tiny cubic zirconia accents—it’s lightweight, slips on easily, and feels elegant whether you’re at the office or out for dinner. Next, the Sterling Silver Charm Bracelet features a delicate chain dotted with meaningful charms; its cool sheen complements both casual and formal outfits, though the charms can sometimes jingle more than you’d expect. Finally, the Leather Wrap Bracelet offers a boho twist with its soft, braided leather and subtle metal clasp—it’s perfect for weekend wear, though you’ll want to keep it dry to preserve the leather’s supple texture.

Overall, these pieces strike a great balance between style and affordability, but they’re not without minor drawbacks. On the plus side, each bracelet boasts an eye-catching design and comfortable fit, making them versatile additions to any wardrobe; they arrive in attractive packaging that’s gift-ready and feel surprisingly durable for their price. On the flip side, the leather wrap needs a bit of extra care to avoid water damage, the charm bracelet’s dangling pieces can catch on fabrics, and the rose gold finish, while stunning, may show light wear if subjected to rough handling. """)

print(result)