import pandas as pd

# Load the database from csv
df = pd.read_csv('data/smartphone_inventory_sgd.csv')

# Standardize the column names
df.columns = [col.strip().lower() for col in df.columns]

def check_stock(model_name: str) -> str:
    match = df[df["model"].str.lower() == model_name.lower()]
    if match.empty:
        return f"Sorry, I couldn't find the model '{model_name}' in our inventory."
    stock_status = match.iloc[0]["stock_status"]
    return f"The model '{model_name}' is {stock_status}."

def get_price(model_name: str) -> str:
    match = df[df["model"].str.lower() == model_name.lower()]
    if match.empty:
        return f"Sorry, I couldn't find the model '{model_name}' in our inventory."
    price = match.iloc[0]["price"]
    return f"The price of '{model_name}' is ${price}."

def recommend_phone(budget: float) -> str:
    filtered = df[
        (df["price"] <= budget) &
        (df["stock_status"].str.lower() == "in stock")
    ].sort_values(by="price", ascending=True)

    if filtered.empty:
        return "Sorry, no phones are available within that budget."
    
    top = filtered.iloc[0]
    return f"I recommend the {top['model']} by {top['brand']} for ${top['price']} — it's currently in stock."

# Test
print(check_stock("iphone 13"))
print(get_price("iphone 13"))
print(recommend_phone(1000))