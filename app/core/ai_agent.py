from langchain_groq import ChatGroq
from langchain_community.tools import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config import settings

def system_prompt(messages):
    # Add your system message logic here
    return messages


def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    llm = ChatGroq(model=llm_id, temperature = 0.6)
    tools = [TavilySearchResults(max_results = 2)] if allow_search else []

    agent = create_react_agent(
        model = llm,
        tools = tools,
        # state_modifier = system_prompt
    )

    state = {"messages":query}

    response   = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]



if __name__ == "__main__":
    responseing = get_response_from_ai_agents("llama-3.3-70b-versatile","Who is Narendra Modi?",allow_search=True,system_prompt=system_prompt("You are a personality finder"))
    print(responseing)