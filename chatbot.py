!pip install transformers sentencepiece accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a free chatbot model
model_name = "microsoft/DialoGPT-medium"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chat_history_ids = None

def chatbot_response(user_input):
    global chat_history_ids

    # Encode new user input
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append to chat history
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
    else:
        bot_input_ids = input_ids

    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=500,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode and return
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# --- Simple chat loop ---
print("Chatbot Ready! Type 'exit' to stop.\n")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    reply = chatbot_response(user)
    print("Bot:", reply)
