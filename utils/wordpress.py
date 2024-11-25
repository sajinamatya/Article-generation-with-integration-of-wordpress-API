import requests
from dotenv import load_dotenv, dotenv_values
from requests.auth import HTTPBasicAuth
import base64
load_dotenv()
config = dotenv_values(".env")

username = config.get('username')
password = config.get('password')

def wordpress_post(selected_key,response_gemini):
    site_url = 'https://public-api.wordpress.com/wp/v2/sites/sajin2.wordpress.com/posts'  
   
    creds = username + ':' + password
    token = base64.b64encode(creds.encode())
    header = {'Authorization':'Basic' + token.decode('utf-8')}
    post_data = {
        "title": selected_key,
        "content": response_gemini.get('text'),
        "status": 'publish'  
    }


    try:
        response = requests.post(site_url, json=post_data,  headers = header )
    except :
        print("error has occured")

    if response.status_code == 201:
        print("Post created and published successfully!")
       
    else:
        print("Failed to create post. Status code:", response.status_code)
     
