import streamlit as st
from utils.googlesheet import sheet_to_dict
from utils.chatbot_gemini import get_gemini_response
from utils.wordpress import wordpress_post

    # Set page layout
st.set_page_config(layout="wide")

    # Fetch data
dict_data = sheet_to_dict()
    
    # Page title
st.title("Google Sheet API Integration with WordPress")
st.subheader("Choose a title for your WordPress post")

    # Selectbox for titles
selected_key = st.selectbox("choose", list(dict_data.keys()), key="selected_key")
  
    # checking if the selected title session exists or not 
submit = st.button("submit")

if submit:
     with st.spinner("Processing"):
         if selected_key:
             st.success(f"You selected title: {selected_key}")
                
             response_gemini = get_gemini_response(selected_key,dict_data[selected_key])
            
             st.write(response_gemini["text"])  
             wordpress_post(selected_key,response_gemini)
             
         else:
              st.warning("No values selected. Please choose at least one.")


