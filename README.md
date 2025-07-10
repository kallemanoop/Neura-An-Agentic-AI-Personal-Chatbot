# LangGraph Agentic Chatbot

## Overview

LangGraph Agentic Chatbot is a stateful, interactive chatbot framework built with LangGraph and powered by Groq's high-speed LLM inference. It allows users to select different language models, initiate dynamic multi-turn conversations, and view real-time responses within a Streamlit interface.

## Features

- Model selection from Groq-hosted LLMs: `gemma2-9b-it`, `llama3-70b-8192`, `llama3-8b-8192`
- Modular architecture with isolated components for model config, graph setup, and UI rendering
- Graph-based execution flow using LangGraph nodes
- Real-time inference using Groq API
- Stateful chat experience with multi-turn history using Streamlit session state

## Technologies Used

- Python
- LangGraph
- LangChain
- Streamlit
- Groq API
- Models: `gemma2-9b-it`, `llama3-70b-8192`, `llama3-8b-8192`

## How It Works

1. Users select an LLM and use case from the Streamlit sidebar and provide their Groq API key.
2. The application initializes a Groq-backed LangChain LLM instance.
3. A dynamic graph is constructed based on the selected use case using LangGraph.
4. The chatbot node processes user input and invokes the model to generate a response.
5. The response is displayed in the Streamlit UI along with full chat history.
6. All interactions are managed using LangGraph’s StateGraph and preserved via session state.

## Future Additions

- File uploads with retrieval-augmented generation (RAG)
- Integration of tool usage via LangChain agents
- Persistent memory modules
- Deployment on Hugging Face Spaces or similar platforms
