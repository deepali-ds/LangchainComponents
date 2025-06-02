#from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


# Define the model
#llm = HuggingFaceEndpoint(
#    repo_id="google/gemma-2-2b-it",
#    task = 'text-generation'
#)


#model = ChatHuggingFace(llm=llm)

model = ChatOpenAI()

class Person(BaseModel):

    name : str = Field(description='Name of the person')
    age : int = Field(gt=18, description= ' The person should be over 18 years')
    city : str = Field(description='Name of the city person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= 'Generate the name, age and city of a frictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result =  chain.invoke({'place' : 'Indian'})

print(result)