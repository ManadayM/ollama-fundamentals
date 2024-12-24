import ollama

response = ollama.list()

# print(response)

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)
print(res["message"]["content"])