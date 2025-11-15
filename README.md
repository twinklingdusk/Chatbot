# Advanced Python Chatbot

A Python based chatbot implemented in Google Colab using the HuggingFace Transformers library. This chatbot supports conversational responses, context retention, and can operate entirely for free using an open source model.

This project demonstrates how to build a moderately advanced generative chatbot without needing paid APIs. It is suitable for academic assignments, demonstrations, and beginner level AI development projects.

## Features

* Fully free to use.
* Runs directly in Google Colab with no installations beyond standard pip packages.
* Uses an open source language model from HuggingFace.
* Supports multi turn conversation.
* Designed as a simple interactive CLI chatbot.
* Ready to be published on GitHub for public access.

## Technologies Used

* Python 3
* HuggingFace Transformers
* Google Colab
* GitHub for hosting

---

## Folder Structure

```
/project-root
    chatbot.py
    README.md
```
## Setup Instructions

### 1. Clone or download the repository

If using GitHub, click Code and download ZIP or use

```
git clone <your-repository-link>
```

### 2. Upload the chatbot.py file to Google Colab

* Open Colab
* Click File
* Click Upload Notebook or start a new notebook
* Upload chatbot.py using the left side Files panel if needed

### 3. Install required libraries

Run this in a Colab cell

```python
!pip install transformers
```

### 4. Run the Chatbot

```python
from chatbot import chatbot_loop
chatbot_loop()
```

The chatbot will start responding to user inputs interactively.

## Code Overview

The core logic for the chatbot resides in chatbot.py.

The model used is

```
microsoft/DialoGPT-medium
```

The script maintains conversation history and generates responses based on previous turns. The system loops until the user types exit.

## Example Chat

```
You: hello
Bot: Hi there. How can I help you today  

You: tell me something interesting
Bot: Did you know that the deepest point on Earth is the Mariana Trench

```

## Academic Use

This chatbot can be used for

* Artificial Intelligence coursework
* Chatbot development assignments
* NLP demonstrations
* Basic conversational model implementation

## Notes

* This model runs locally in Colab.
* No API key is required.
* HuggingFace models may take a few seconds to load.

