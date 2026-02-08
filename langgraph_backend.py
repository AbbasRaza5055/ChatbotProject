from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict, Annotated
from langchain_groq import ChatGroq
from langgraph.graph.message import BaseMessage, add_messages
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model = 'llama-3.3-70b-versatile')

class ChatState(TypedDict):

    messages : Annotated[list[BaseMessage],add_messages ]


graph = StateGraph(ChatState)

def chat_node(state : ChatState):
    message = state['messages']

    response = llm.invoke(message)

    return {'messages' : [response]}

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node',END)

checkpointer = InMemorySaver()



chat_bot = graph.compile(checkpointer)

# for message_chunk, metadata in chat_bot.stream(
#     {'messages' : [HumanMessage(content = 'Write a 500 words blog on Cricket')]},
#     config={'configurable': {'thread_id' : 'thread_1'}},
#     stream_mode='messages',
# ):
#     if message_chunk.content:
#         print(message_chunk.content, end="", flush=True)
