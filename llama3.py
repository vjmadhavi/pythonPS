import ollama
with open('groceries.txt', 'r') as file:
    groceries = file.read()

response = ollama.chat(model = 'llama3', messages=[
    {
        'role':'user',
        'content': "preparing a grocery list, organising them in the order" + groceries,
    }
])

with open('sorted.txt', 'w') as file:
    file.write(response['message']['content'])