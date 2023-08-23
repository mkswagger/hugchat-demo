from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login('mathangykrishna16@gmail.com', 'ALKXS3u))Q5sjNR')
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookiesToDir('COOKIES')

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

# Create a new conversation
conversation_id = chatbot.new_conversation()

# Conversation loop
while True:
    user_input = input("You: ")  # Get user input
    
    # Prepend the topic to the user input
    user_input_with_topic = "vegetables: " + user_input
    
    response = chatbot.chat(user_input_with_topic)  # Get bot response
    
    print("Bot:", response)  # Print bot response
    
    if response == "Conversation Ended":
        print("Conversation ended.")
        break
