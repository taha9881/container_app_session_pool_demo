from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_azure_dynamic_sessions import SessionsPythonREPLTool
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()
POOL_MANAGEMENT_ENDPOINT = os.getenv("POOL_MANAGEMENT_ENDPOINT")

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

tool = SessionsPythonREPLTool(pool_management_endpoint=POOL_MANAGEMENT_ENDPOINT)
prompt = hub.pull("hwchase17/openai-functions-agent")
agent = create_tool_calling_agent(llm, [tool], prompt)

agent_executor = AgentExecutor(
    agent=agent, tools=[tool], verbose=True, handle_parsing_errors=True
)

response = agent_executor.invoke(
    {
        "input": "what is the sum of 5 + 10? Please calculate it using python code.",
    }
)
print(response)