import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType

from tools import get_price, check_stock, recommend_phone

tools = [
    Tool(
        name="GetPrice",
        func=get_price,
        description="Use this to get the price of a phone by model name."
    ),
    Tool(
        name="CheckStock",
        func=check_stock,
        description="Use this to check if a phone is in stock."
    ),
    Tool(
        name="RecommendPhone",
        func=lambda x: recommend_phone(float(x)),
        description="Use this to recommend a phone based on a budget."
    )
]

llm = OllamaLLM(
    model="llama3",
    temperature=0,
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# st.title("📱 Smartphone Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt:= st.chat_input("Ask about stock, price, or get a recommendation:"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent.invoke(prompt)

            tool_output = result["output"] if isinstance(result, dict) else result

            rephrase_prompt = f"""
                You are a friendly and helpful tech assistant. 
                Please turn the following message into a natural, conversational reply suitable for a user. 
                Avoid saying things like "The final answer is" or "Observation".
                Add emojis only if it enhances the reply, and keep the tone clear and friendly.

                Original response:
                {tool_output}
            """

            response = llm.invoke(rephrase_prompt)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

