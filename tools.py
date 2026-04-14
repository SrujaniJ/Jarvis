import os
import requests
from dotenv import load_dotenv
from elevenlabs.conversational_ai.conversation import ClientTools
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()
search = DuckDuckGoSearchRun()

def search_web(parameters):
    query = parameters.get('query')
    return search.run(query)

def save_to_txt(parameters):
    filename = parameters.get('filename')
    content = parameters.get('content')
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')
    return f'Saved to {filename}'

def create_html_file(parameters):
    filename = parameters.get('filename')
    html_content = parameters.get('html_content')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    return f'HTML file created: {filename}'

def generate_image(parameters):
    prompt = parameters.get('prompt')
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
    return url


def save_to_txt(parameters):
    print(f"DEBUG: save_to_txt called with {parameters}")
    filename = parameters.get('filename')
    content = parameters.get('content')
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')
    return f'Saved to {filename}'

client_tools = ClientTools()
client_tools.register('search_web', search_web)
client_tools.register('save_to_txt', save_to_txt)
client_tools.register('create_html_file', create_html_file)
client_tools.register('generate_image', generate_image)
