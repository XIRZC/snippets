import openai

openai.api_key = 'YOUR_CHATGPT_API_KEY'

# define system role
messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]

while True:
    # user input
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    
    # contruct api request
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # response
    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')

    # append previous chat response by assitant to avoid repetitive response between several continual chats
    messages.append({"role": "assistant", "content": chat_response})
