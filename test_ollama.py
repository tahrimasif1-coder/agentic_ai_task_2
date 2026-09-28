from ollama import chat

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain Agentic AI in 2 simple sentences."
        }
    ]
)

print(response.message.content)
