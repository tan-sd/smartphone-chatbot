import pandas as pd
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

df = pd.read_csv("smartphone_inventory_sgd.csv")

docs = []
for _, row in df.iterrows():
    text = (
        f"Smartphone Model: {row['Brand']} {row['Model']}\n"
        f"Price: ${row['Price']}\n"
        f"Stock Status: {row['Stock_Status']}"
    )
    metadata = {
        "brand": row["Brand"],
        "model": row["Model"].lower(),
    }
    docs.append(Document(page_content=text, metadata=metadata))

embedding = OllamaEmbeddings(model="llama3.2")

vectorstore = FAISS.from_documents(docs, embedding)
vectorstore.save_local("faiss_index")

print("✅ Vector saved to 'faiss_index' with structured chunks.")