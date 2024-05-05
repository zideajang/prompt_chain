import ollama
from local_model import build_ollama_model as ask_llama3

from rich.console import Console

console = Console()


def write_blog(base_info):
    base_info = base_info
    
    snowball_prompt_1 = f"Generate a clickworthy title about this topic:'{base_info}'Respond in JSON format {{title: 'title', topic: '{base_info}'}}"

    snowball_response_1 = ask_llama3("llama3",snowball_prompt_1)

    snowball_prompt_2 = f"Generate a compelling 3 section outline given this information: '{snowball_response_1}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>']}}"

    snowball_response_2 = ask_llama3("llama3",snowball_prompt_2)

    snowball_prompt_3 =  f"Generate 1 paragraph of content for each section outline given this information: '{snowball_response_2}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>'], content: ['<content1>', '<content2>', '<content3>']}}"

    snowball_response_3 = ask_llama3("llama3",snowball_prompt_3)
    

    console.print(":robot:")
    console.print(snowball_response_1)

    console.print(":robot:"*2)
    console.print(snowball_response_2)

    console.print(":robot:"*3)
    console.print(snowball_response_3)

    snowball_markdown_prompt = f"Generate a markdown formatted blog post given this information: '{snowball_response_3}'. Respond in JSON format {{markdown_blog: '<entire markdown blog post>'}}"


    snowball_markdown_response = ask_llama3("llama3",snowball_markdown_prompt)
    console.print(snowball_markdown_response)

    with open("snowball_prompt_chain.txt", "w") as file:
        file.write(snowball_markdown_response)