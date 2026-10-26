
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
chatbot = ChatBot(
    "Student Chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbot.sqlite3",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)

# Train chatbot
trainer = ListTrainer(chatbot)

conversations = [
    ["Hello", "Hi! How can I help you?"],
    ["Good morning", "Good morning! How are you doing?"],
    ["How are you?", "I am doing very well, thank you for asking."],
    ["What is your name?", "My name is Student Chatbot."],
    ["What is Python?", "Python is a programming language."],
    ["What is Django?", "Django is a Python web framework."],
    ["What is AI?", "AI stands for Artificial Intelligence."],
    ["Thank you", "You're welcome!"],
    ["Goodbye", "Goodbye! Have a great day!"]
]

for conversation in conversations:
    trainer.train(conversation)

# Start terminal chatbot
print("Welcome to Student Q&A Chatbot!")
print("Type 'exit' to stop chatting.")

while True:
    user_input = input("User: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not user_input:
        print("Bot: Please enter a question.")
        continue

    response = chatbot.get_response(user_input)
    print("Bot:", response)
