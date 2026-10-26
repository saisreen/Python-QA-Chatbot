# Simple Q&A Chatbot Using Python

## Hands-On Assignment 3

### Project Overview

This project is a simple Question and Answer (Q&A) chatbot developed using Python, Django, and ChatterBot. The chatbot allows users to interact through a terminal by entering questions and receiving responses.

The chatbot is trained using predefined conversations and uses the ChatterBot library to generate responses based on the training data.

### Technologies Used

- **Python 3.12** – Programming language
- **Django 4.2** – Python web framework used for project setup
- **ChatterBot 1.2.8** – Conversational chatbot library
- **spaCy** – Natural language processing
- **SQLite** – Database for storing chatbot conversations
- **Visual Studio Code** – Development environment

### Features

- Simple terminal-based chatbot
- Responds to greetings and basic questions
- Uses ChatterBot's ListTrainer for training
- Stores conversation data using SQLite
- Supports continuous conversations
- Allows users to exit by typing `exit`
- Handles empty user input

### Project Structure

```text
Chatbot_Assignment3/
│
├── chatbot_project/
│   ├── chatbot.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/Python-QA-Chatbot.git
cd Python-QA-Chatbot
```

**Step 2: Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Install the spaCy English language model**

```bash
python -m spacy download en_core_web_sm
```

**Step 5: Apply Django database migrations**

```bash
python manage.py migrate
```

**Step 6: Run the chatbot**

```bash
python chatbot_project/chatbot.py
```

### Sample Input and Output

```text
Welcome to Student Q&A Chatbot!
Type 'exit' to stop chatting.

User: Hello
Bot: Hi! How can I help you?

User: what is python?
Bot: Python is a programming language.

User: how are you ?
Bot: I am doing very well, thank you for asking.

User: exit
Bot: Goodbye!
```

### How It Works

1. The chatbot is initialized using the ChatterBot library.
2. Sample questions and answers are provided for training.
3. ListTrainer trains the chatbot using these conversations.
4. The user enters a question through the terminal.
5. The chatbot processes the input and generates a response.
6. The conversation continues until the user types `exit`.

### Testing

The chatbot was successfully tested in the Visual Studio Code terminal.

The following test cases were completed:

- Greeting response – Passed
- Python-related question – Passed
- General conversation – Passed
- Exit command – Passed

### Conclusion

This project demonstrates the basic implementation of a conversational chatbot using Python and ChatterBot. It provides practical experience with chatbot training, natural language processing, database storage, and terminal-based user interaction.

### Author

Sai Sree Narla

**Project:** Simple Q&A Chatbot Using Python