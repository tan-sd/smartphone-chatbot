from tools import check_stock, get_price, recommend_phone
from llm_wrapper import ask_llm

def route_query(user_input: str) -> str:
    user_input_lower = user_input.lower()

    if "stock" in user_input_lower or "available" in user_input_lower:
        for model in ["iPhone 15 Pro Max", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15", "iPhone 14"]:
            if model.lower() in user_input_lower:
                tool_result = check_stock(model)
                prompt = f"A user asked whether the {model} is in stock. Here's what the database returned:\n\n{tool_result}\n\nPlease reply to the user in a helpful tone."
                return ask_llm(prompt)
    
    if "price" in user_input_lower or "cost" in user_input_lower or "$" in user_input_lower:
        for model in ["iPhone 15 Pro Max", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15", "iPhone 14"]:
            if model.lower() in user_input_lower:
                tool_result = get_price(model)
                prompt = f"A user asked about price. Here's what the database returned:\n\n{tool_result}\n\nPlease reply to the user in a helpful tone."
                return ask_llm(prompt)
    
    return ask_llm(user_input)

def main():
    print("Welcome to the Smartphone Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        reply = route_query(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    main()