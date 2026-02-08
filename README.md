# 🤖 Stateful AI Chatbot using LangGraph & Streamlit

This project is a **stateful AI chatbot** built using **LangGraph**, **LangChain**, and **Streamlit**, powered by **LLaMA 3.3 (70B) via Groq**.  
It demonstrates how to design **graph-based LLM workflows** with memory and a clean frontend.

---

## 🚀 Features

- ✅ **Stateful Conversations**
  - Maintains chat history across multiple turns
  - Uses LangGraph checkpointing for memory management

- 🔁 **Graph-based Workflow (LangGraph)**
  - Chat logic implemented as a `StateGraph`
  - Easy to extend into multi-node or agentic workflows

- ⚡ **High-Performance LLM**
  - Powered by **LLaMA 3.3 – 70B**
  - Fast inference using **Groq**

- 💬 **Interactive Streamlit UI**
  - Real-time chat interface
  - Session-based message history
  - Clean and minimal frontend

- 🔒 **Secure Configuration**
  - Environment variables for API keys
  - `.env` file excluded using `.gitignore`

---

## 🧠 Project Architecture

ChatbotProject/
│
├── streamlit_frontend.py # Streamlit-based chat UI
├── langgraph_backend.py # LangGraph state & chat logic
├── .env # Environment variables (not pushed)
├── .gitignore
├── README.md

📌 Use Cases

AI Chatbots

Customer Support Assistants

Conversational AI Prototypes

Learning Agentic AI & LangGraph

Base for multi-agent systems

🔮 Future Enhancements

🔀 Multi-node routing

🧩 Tool calling & function execution

🤝 Multi-agent collaboration

💾 Persistent memory (DB-based)

📊 Analytics & logging

👤 Author

Abbas
AI / Agentic AI Enthusiast
Building scalable, graph-based LLM systems

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
