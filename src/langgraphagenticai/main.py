import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResult

def load_langgraph_agenticai_app():
    st.set_page_config(page_title="LangGraph Agentic Chatbot", layout="wide")

    
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.stop()  

    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    
    for user_msg, assistant_msg in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(assistant_msg)

    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            
            with st.chat_message("user"):
                st.write(user_message)

            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            usecase = user_input.get("selected_usecase")
            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usecase)

            for event in graph.stream({'messages': ("user", user_message)}):
                for value in event.values():
                    msg = value.get("messages")

                    if isinstance(msg, list):
                        for m in msg:
                            assistant_text = getattr(m, "content", str(m))
                            with st.chat_message("assistant"):
                                st.write(assistant_text)
                            st.session_state.chat_history.append((user_message, assistant_text))
                    elif hasattr(msg, "content"):
                        assistant_text = msg.content
                        with st.chat_message("assistant"):
                            st.write(assistant_text)
                        st.session_state.chat_history.append((user_message, assistant_text))
                    elif isinstance(msg, str):
                        with st.chat_message("assistant"):
                            st.write(msg)
                        st.session_state.chat_history.append((user_message, msg))
                    else:
                        with st.chat_message("assistant"):
                            st.write("⚠️ Unexpected response format.")
                        st.session_state.chat_history.append((user_message, "⚠️ Unexpected response format."))

        except Exception as e:
            st.error(f"Error: {e}")
