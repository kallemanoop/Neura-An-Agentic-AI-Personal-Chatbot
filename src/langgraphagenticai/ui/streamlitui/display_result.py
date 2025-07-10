import streamlit as st
from langchain_core.messages import BaseMessage

class DisplayResult:
    """
    Class to display the result of the LangGraph Agentic AI application.
    """

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        graph = self.graph
        user_message = self.user_message

        if self.usecase == "Basic Chatbot":
            with st.chat_message("user"):
                st.write(user_message)

            for event in graph.stream({'messages': ("user", user_message)}):
                for value in event.values():
                    msg = value.get("messages", None)

                    # Handle list of messages
                    if isinstance(msg, list):
                        for m in msg:
                            with st.chat_message("assistant"):
                                st.write(getattr(m, "content", str(m)))

                    # Handle single message
                    elif isinstance(msg, BaseMessage):
                        with st.chat_message("assistant"):
                            st.write(msg.content)

                    # Fallback
                    elif isinstance(msg, str):
                        with st.chat_message("assistant"):
                            st.write(msg)

                    else:
                        with st.chat_message("assistant"):
                            st.write("⚠️ Could not parse assistant response.")
