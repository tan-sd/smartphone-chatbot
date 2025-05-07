from llm_wrapper import ask_llm

question = "Is the iPhone 15 in stock?"

print("User: ", question)
print("Bot: ", ask_llm(question))