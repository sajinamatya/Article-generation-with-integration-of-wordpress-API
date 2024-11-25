import streamlit as st
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, dotenv_values
from langchain import LLMChain, PromptTemplate
load_dotenv()



def load_prompt():
    try:
        with open("utils//prompt.txt", "r") as prompt_read:
            prompt = prompt_read.read()
    except FileNotFoundError:
        print("Error: 'prompt.txt' file not found.")
    except PermissionError:
        print("Error: Permission denied when accessing file  'prompt.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return prompt

# Intialization of the Gemini model
try: 
    gemini_model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.5)
except Exception as e:
    print("An error has occured in initalization of the gemini model", str(e))


    
def get_gemini_response(article_title,SEO_keyword):
    """Get response from Gemini API using the .invoke() method."""
    prompt = load_prompt()
    SEO_keywords= ", ".join(SEO_keyword)
    prompt_template = PromptTemplate(template=prompt, input_variables=["article_title","SEO_keywords"])
     
    # Use the new .invoke() method
    try:
        chain = LLMChain(llm=gemini_model, prompt=prompt_template)
        # Invoke the Gemini model
        response = chain.invoke({"article_title": article_title,"SEO_keywords":SEO_keywords})
        
       
        return response
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None


    






