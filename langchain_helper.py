# main.py
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in .env")

    llm = OpenAI(temperature=0.7)
    
    prompt = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a pet {animal_type} and I want a cool name for it. "
                 "It is {pet_color} in color. Suggest me five cool names for my pet."
    )
    
    chain = prompt | llm
    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response

if __name__ == "__main__":
    result = generate_pet_name("caw", "black")
    print(result)