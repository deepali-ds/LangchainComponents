from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

#Schema

class Review(BaseModel):

    key_themes: list[str] = Field(description= "Write down all the key themes discussed in the review in a list")
    summary: str = Field(description=" Write a brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Recently added three lovely bracelets to my collection, and each has its own charm. First, the Rose Gold Adjustable Bracelet dazzles with its warm hue and tiny cubic zirconia accents—it’s lightweight, slips on easily, and feels elegant whether you’re at the office or out for dinner. Next, the Sterling Silver Charm Bracelet features a delicate chain dotted with meaningful charms; its cool sheen complements both casual and formal outfits, though the charms can sometimes jingle more than you’d expect. Finally, the Leather Wrap Bracelet offers a boho twist with its soft, braided leather and subtle metal clasp—it’s perfect for weekend wear, though you’ll want to keep it dry to preserve the leather’s supple texture.

Overall, these pieces strike a great balance between style and affordability, but they’re not without minor drawbacks. On the plus side, each bracelet boasts an eye-catching design and comfortable fit, making them versatile additions to any wardrobe; they arrive in attractive packaging that’s gift-ready and feel surprisingly durable for their price. On the flip side, the leather wrap needs a bit of extra care to avoid water damage, the charm bracelet’s dangling pieces can catch on fabrics, and the rose gold finish, while stunning, may show light wear if subjected to rough handling. """)

print(result)
