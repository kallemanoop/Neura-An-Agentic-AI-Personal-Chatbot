from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START,END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using the provided LLM model.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. The chatbot note is set as both the entry
        and exit point of the graph.
        """

        self.basic_chatbout_node=BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbout_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        This method checks the use case and builds the corresponding graph.
        If the use case is not recognized, it raises a ValueError.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()