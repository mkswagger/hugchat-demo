from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login('mathangykrishna16@gmail.com', 'ALKXS3u))Q5sjNR')
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookiesToDir('COOKIES')

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# Create a new conversation and set the context to "restaurants in Chennai"
conversation_id = chatbot.new_conversation()
chatbot.change_conversation(conversation_id)
chatbot.chat("Chennai")  # Set the context to "restaurants in Chennai"

# Conversation loop
while True:
    user_input = input("You: ")  # Get user input
    response = chatbot.chat(user_input)  # Get bot response
    
    print("Bot:", response)  # Print bot response
    
    if response == "Conversation Ended":
        print("Conversation ended.")
        break
