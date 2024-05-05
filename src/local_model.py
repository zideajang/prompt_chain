import ollama

def build_ollama_model(model,prompt):
    response = ollama.chat(
        model=model,
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response['message']['content']