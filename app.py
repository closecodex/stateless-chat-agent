from datetime import datetime
from typing import TypedDict, List
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph

@tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO‑8601 format."""
    return {"utc": datetime.utcnow().isoformat() + "Z"}

llm = ChatOllama(model="llama3")

class AgentState(TypedDict):
    messages: List[BaseMessage]

def agent_step(state: AgentState) -> AgentState:
    messages = state["messages"]
    user_message = messages[-1].content.lower()
    if "time" in user_message:
        tool_result = get_current_time.invoke({})
        reply = f"Current UTC time is: {tool_result['utc']}"
        return {"messages": messages + [AIMessage(content=reply)]}
    else:
        ai_response = llm.invoke(messages)
        return {"messages": messages + [ai_response]}

builder = StateGraph(AgentState)
builder.add_node("agent", agent_step)
builder.set_entry_point("agent")
builder.set_finish_point("agent")
app = builder.compile()

if __name__ == "__main__":
    print("Minimal stateless chat, type 'What time is it?' to trigger tool.\n")
    messages = []
    while True:
        user_input = input("You: ")
        messages.append(HumanMessage(content=user_input))
        state = {"messages": messages}
        result = app.invoke(state)
        last_ai = result["messages"][-1]
        print("Bot:", last_ai.content)
        messages.append(last_ai)
