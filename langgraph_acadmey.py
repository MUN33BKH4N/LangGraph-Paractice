from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph.state import StateGraph
from langgraph.graph import START, END

import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GEMINI_API"),
    model = "gemini-2.0-flash",
    temperature=0,
)

messages = []
# while True:
#     ask = input("You :")
#     messages.append(HumanMessage(content=ask))
#     result = llm.invoke(messages)
#     print(result.content)
#     messages.append(AIMessage(content=result.content))

tavily_search = TavilySearchResults(max_results=100,api_key= os.getenv("TAVILY_API_KEY"))
search_results = tavily_search.invoke("Who is umair tiktok wala")
print(search_results)
