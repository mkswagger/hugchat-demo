from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login('mathangykrishna16@gmail.com', 'ALKXS3u))Q5sjNR')
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookiesToDir('COOKIES')

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
print(chatbot.chat("how can i use you as an alternative to openai api"))

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Get conversation list
conversation_list = chatbot.get_conversation_list()