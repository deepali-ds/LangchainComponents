from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI()
#model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template= 'Generate short and simple naotes from the following text \n {text}',
    input_variables=['text']
)

prompt2= PromptTemplate(
    template= 'Generate 3 short questions and answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables= ['notes', 'quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain


text = """
The urban heat island (UHI) effect describes the phenomenon where cities are significantly warmer than their surrounding rural areas, primarily due to changes in the land surface and human-generated heat. This is because cities replace natural vegetation and soils with buildings, roads, and other infrastructure that absorb and re-emit solar heat. Additionally, human activities like vehicle use, air conditioning, and industrial processes contribute waste heat. 
Key Factors Contributing to UHI:
Reduced Green Spaces:
The replacement of vegetation with pavement and buildings reduces shade and the cooling effect of evapotranspiration (water released from plants), leading to higher temperatures. 
Dense Buildings and Infrastructure:
Buildings, roads, and other structures absorb and re-emit solar heat, contributing to increased urban temperatures. 
Urban Layout:
Tall buildings and narrow streets can trap warm air, further exacerbating the UHI effect. 
Human-Generated Heat:
Vehicles, air conditioning, and industrial processes release waste heat into the urban environment. 

Impacts of UHI:
Increased Heat-Related Illnesses:
UHI can lead to heatstroke, heat exhaustion, and other heat-related illnesses, particularly among vulnerable populations like children and the elderly. 
Increased Energy Consumption:
Cities with UHI require more energy for cooling, contributing to higher electricity bills and potential strain on power grids. 
Air Pollution:
High temperatures can worsen air quality and increase the levels of ground-level ozone. 
Infrastructure Damage:
Extreme heat can damage pavement, bridges, and other infrastructure, leading to higher maintenance costs. 
Social and Economic Impacts:
UHI disproportionately affects low-income communities and can lead to social disparities. 
Mitigation Strategies:
Green Infrastructure:
Increasing tree cover, planting vegetation, and using green roofs can help cool urban areas. 
Reflective Surfaces:
Using lighter-colored building materials and pavements can reflect more sunlight and reduce heat absorption. 
Improved Urban Design:
Varying building heights, implementing zoning regulations, and creating open spaces can improve airflow and reduce heat. 
Public Awareness and Education:
Educating the public about the impacts of UHI and promoting cooling strategies can help individuals make informed decisions. 
"""

result = chain.invoke({'text': text})

print(result)

